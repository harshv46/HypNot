
# HypNot
## Leveraging AI to ensure a Safe Ride
---
### Dependencies
Prerequisites: Python 3.6 or above, Pip, Visual studio (for C++ build systems)

##### Install the following packages: 
* C++ CMake tools for windows from Visual Studio 
* Windows10 SDK from Visual Studio 
* ```pip install numpy scipy PyAudio cmake opencv-contrib-python scikit-image pandas playsound imutils```
---
### Build and Run:
##### Drowsiness Detection Module
```python detect_blinks.py --shape-predictor shape_predictor_68_face_landmarks.dat```
To stop the alarm, press and release space key and then say "turn off".

##### Drift Detection Module
```python detect_drift.py```

---
---
## Project Overview and Idea
**Drivers are Falling Asleep Behind the Wheel!**

**Background:**

According to the National Highway Traffic Safety Administration, every year about 100,000 police-reported crashes involve drowsy driving. These crashes result in more than 1,550 fatalities and 71,000 injuries.

According to the National Sleep Foundation, about half of U.S. adult drivers admit to consistently getting behind the wheel while feeling drowsy. The real number may be much higher, however, as it is difficult to determine whether a driver was drowsy at the time of a crash.

A study by the AAA Foundation for Traffic Safety estimated that 328,000 drowsy driving crashes occur annually. That's more than three times the police-reported number. The same study found that 109,000 of those drowsy driving crashes resulted in an injury and about 6,400 were fatal. The researchers suggest the prevalence of drowsy driving fatalities is more than 350% greater than reported.

**Objective:**

According to the National Safety Council, following are the signs and symptoms of drowsy driving: * Difficulty in keeping eyes open * "Nodding off" or having trouble keeping your head up * Drifting out of your lane

Our objective is to harness the data available to us, namely the facial patterns of the driver and the other data points, to devise a strategy such that we can raise an alert whenever we detect some of the above symptoms.

**Implementation:**

We use Artificial Intelligence to detect facial patterns of the driver to determine whether his eye focus is on the road or not. Soukupova and Cech in  [Real-Time Eye Blink Detection using Facial Landmarks](http://vision.fe.uni-lj.si/cvww2016/proceedings/papers/05.pdf), deduce an interesting expression which accurately estimates an eye blink using related facial landmarks. This implementation, however, needs a Driver Facing Camera to get live video stream for real time analysis. The facial landmark detection and mapping is an implementation of the  [One Millisecond Face Alignment with an Ensemble of Regression Trees](https://www.semanticscholar.org/paper/One-millisecond-face-alignment-with-an-ensemble-of-Kazemi-Sullivan/d78b6a5b0dcaa81b1faea5fb0000045a62513567?p2df)  paper by Kazemi and Sullivan (2014). If the face of the driver couldn't be recognized, and the car is above a specified speed limit, we sound an alert message. The activated alert can be shut off using a voice command. To address the last sign mentioned above, we use the data points available to us to estimate the direction of the vehicle and raise an alert when we detect an unexpected unusual drift.

**Application:**

Implementation of this feature in vehicles has a potential of saving thousands of lives every year. The AI system constantly monitors the driver's facial activity in coherence with the speed and direction of the vehicle to ensure a safe ride by sounding an alert message to intimate the driver and others in the vehicle and forewarn against anticipated mishappenings.

---
