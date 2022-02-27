from facenet_pytorch import MTCNN
import torch
import numpy as np
import mmcv, cv2
import pdb
from PIL import Image, ImageDraw
from resnet import ResNet
import torchvision.transforms as tt
from fernet import get_model, get_prediction
import time
from dataupload import upload_emotion


device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
print('Running on device: {}'.format(device))

mtcnn = MTCNN(keep_all=True, device=device)

cap = cv2.VideoCapture(0)

cv2.namedWindow('video', cv2.WINDOW_AUTOSIZE)

class_labels = ["Angry", "Happy", "Neutral", "Sad", "Suprise"]
class_onehot = {"Angry":np.array([1.0,0.0,0.0,0.0,0.0]), \
        "Happy":np.array([0.0,1.0,0.0,0.0,0.0]), \
        "Neutral":np.array([0.0,0.0,1.0,0.0,0.0]), \
        "Sad":np.array([0.0,0.0,0.0,1.0,0.0]), \
        "Suprise":np.array([0.0,0.0,0.0,0.0,1.0])
        }
class_mappings = {"Angry":"Sad", "Happy":"Happy", "Neutral":"Neutral", "Sad":"Sad", "Suprise":"Happy"}
class_weights = {"Angry":10, "Happy":1, "Neutral":1, "Sad":10, "Suprise":50}

model_state = torch.load("./models/emotion_detection_model_state.pth")
model = ResNet(1, len(class_labels))
model.load_state_dict(model_state)

### Using Keras model
#class_labels = ["Angry", "Disgust", "Fear", "Happy", "Neutral", "Sad", "Surprise"]
#model = get_model((48,48,1), len(class_labels))
#model.load_weights("models/ferNet.h5")


def get_binned_label(labels_list):
    result = np.array([0.0 for _ in range(len(class_labels))])
    for label in labels_list:
        result += class_weights[label]*class_onehot[label]
    label = class_labels[result.argmax()]
    return class_mappings[label]


t0 = time.time()
labels_bin = []
while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    frame = Image.fromarray(frame)

    # Detect faces
    boxes, _ = mtcnn.detect(frame)

    if boxes is not None:
        # get box with maximum area
        areas = [(box[2]-box[0])*(box[3]-box[1]) for box in boxes]
        max_box_idx = max(enumerate(areas), key=lambda x: x[1])[0]
        max_box = boxes[max_box_idx]

        # extract face and detect emotion
        x1, y1, x2, y2 = max_box.astype(int).tolist()
        face = np.array(frame)[y1:y2+1, x1:x2+1]

        if areas[max_box_idx] > 0 and face.sum()>0:
            # Draw face
            frame_draw = frame.copy()
            draw = ImageDraw.Draw(frame_draw)
            draw.rectangle(max_box.tolist(), outline=(255, 0, 0), width=6)
            cv2.imshow("video", np.array(frame_draw))

            gray_face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
            gray_face = cv2.resize(gray_face, (48, 48), interpolation=cv2.INTER_AREA)

            gray_face = tt.functional.to_pil_image(gray_face)
            gray_face = tt.functional.to_grayscale(gray_face)
            gray_face = tt.ToTensor()(gray_face).unsqueeze(0)

            tensor = model(gray_face)
            pred = torch.max(tensor, dim=1)[1].tolist()
            label = class_labels[pred[0]]
            
            ### Using Keras model
            #label = get_prediction(model, gray_face, class_labels)
            
            labels_bin.append(label)
            #print(label)

    else:
        #print("Face not Detected!")
        cv2.imshow("video", np.array(frame))
    cv2.waitKey(1)
    t1 = time.time()
    if t1-t0 > 10.0:
        binned_label = get_binned_label(labels_bin)
        print("Binned label:", binned_label)
        upload_emotion(binned_label)
        t0 = time.time()
        labels_bin = []

print('\nDone')

cv2.destroyAllWindows()


