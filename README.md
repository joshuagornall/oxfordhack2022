# OxfordHack2022 Contest - The Helpful Cock
`Devpost - https://devpost.com/software/helpfulcock`
### `Made by joshuagornall, alicebarbe, yashbhalgat and nijinskyvich`

#### Context
We had 24 hours to buil this in our Hackathon contest.

#### Inspirtation
What if those moments of frustration, joy, and emotion could launch a dazzling chain of events that spark joy in your life? How do we integrate a squeaking rubber chicken into a hackathon project? These are important questions that we've finally found answers to.

#### What it does
The Helpful Cock is a modular environment that creates chain reactions when you display certain emotions.
In practice, we turn on a crown made of Monster can when you're happy, and make a rubber chicken squawk when you're angry.

#### How we built it
There is a pipeline that connects face detection to emotion detection. In video stream, for each image, we detect the largest face and pass that to the emotion detection neural network which classifies the face into one of six emotion attributes (angry, sad, happy, neutral, etc.). Every five seconds, the detected emotions are binned and sent to a Google Cloud Firebase database,

The motors that we have available are not sufficiently strong to be able to actuate the rubber chicken on their own, so we had to improvise. We use two motors to pull up a glass water bottle with string above the rubber chicken. The motors are mounted to the side of a chair, under which is this entire setup. We've attached an electromagnet to the top of the water bottle, so when it turns on, the electromagnet will stick to the metal bits on the bottom of the chair (more accurately... to a stainless steel cake lifter that we attached with tourist magnets to the bottom of the chair). When the electromagnet turns off and the motors have slackened the string, water bottle violently drops on the rubber chicken, which squawks loudly in response. We call the rubber chicken the Helpful Cock.

The Crown of Enlightenment is a spiralized can of Monster that we molded/hot-glued into the shape of a hairband, covered in delicate string lights.


#### Features:
- Records video
- Analysis of facial expressions
- hardware lights up based on responses

#### Prerequisites:
One important thing is to properly install Python, since our program uses Tensorflow that has some [requirements](https://www.tensorflow.org/install/pip):
- Install Python 3.6(64 Bit) from [here](https://www.python.org/downloads/windows/) for exact versions we used.
- Install and upgrade pip:
```
python get-pip.py
python -m pip install --upgrade pip
```
If you already have Python and pip installed, check their versions with
```
python --version
pip --version
```
and make sure that your Python version is 3.6 – 3.9 and your pip version is at least 19.0 or later.

Now setup the Google Cloud SDK with this [manual](https://cloud.google.com/sdk/docs/downloads-interactive) and install those Python Google libraries using pip:
```
pip install --upgrade google-api-python-client
pip install google-cloud
```

Finally setup the remaining Python-packages by running the command
```
pip install -r requirements.txt
```
from the folder this text file is located in, install pyaudio by following the instruction [here](https://stackoverflow.com/questions/54998028/how-do-i-install-pyaudio-on-python-3-7) and set the PATH environment variable for GOOGLE_APPLICATION_CREDENTIALS with this [instruction](https://cloud.google.com/natural-language/docs/quickstart)

When everything is installed, change your directory to **oxfordhack2022** and run the program:
```
cd to /oxfordhack2022
python emotion_recognition.py
```


#### External Sources:
- https://github.com/timesler/facenet-pytorch
- https://devpost.com/software/helpfulcock
- https://www.kaggle.com/msambare/fer2013

<img width="601" alt="Screenshot 2022-02-27 at 12 33 11" src="https://user-images.githubusercontent.com/62898968/155882545-253db4f7-c6c8-4524-b835-659e5a55e708.png">
<img width="601" alt="Screenshot 2022-02-27 at 12 33 16" src="https://user-images.githubusercontent.com/62898968/155882547-be89e4df-43d7-4ffe-a2c6-80686a744e5c.png">
<img width="601" alt="Screenshot 2022-02-27 at 12 33 22" src="https://user-images.githubusercontent.com/62898968/155882548-72f34fea-22cf-464e-b1dd-918c5d248ab2.png">
<img width="601" alt="Screenshot 2022-02-27 at 12 33 26" src="https://user-images.githubusercontent.com/62898968/155882549-d091d82c-50b7-493a-9c48-cf76f6d32aa8.png">
<img width="601" alt="Screenshot 2022-02-27 at 12 33 30" src="https://user-images.githubusercontent.com/62898968/155882550-27954af7-6a15-40ef-8b22-5a14b8b1a66c.png">
<img width="601" alt="Screenshot 2022-02-27 at 12 33 06" src="https://user-images.githubusercontent.com/62898968/155882557-7ce0cf69-f6c4-4f89-a8d5-fc2468af0104.png">
<img width="601" alt="Screenshot 2022-02-27 at 12 32 58" src="https://user-images.githubusercontent.com/62898968/155882558-9c67fdb3-5143-4289-aab6-03ee2c9d6a1b.png">
