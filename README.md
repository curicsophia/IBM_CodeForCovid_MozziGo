# MozziGo
Our github repository with all of our code and links to our mobile app
## Contents
- Short description
- Demo video
- The architecture
- Long description
- Project roadmap
- Getting started
- Running the tests
- Live demo
- Built with
- Authors
- License
- Acknowledgments
## Short Description
TODO
### Our Problem
### How can technology help?
### Our Idea
## Our Demo
TODO
## The Arcitecture
The project has 2 main componets:
1. User application, running on mobile phone
2. Date processign server, running on *IBM Cloud*
## The Long description
TODO
## Our Project Roadmap
TODO
## Getting Started
There are 2 commponents: user mobile phone application and data server
### Mobile Phone application:
THe github repostiory contains an *Android APK* file:
```
TODO location of APK
```
Download the APK file to your Android mobile phone (eg. email or data transfer) and open it to install our application
### Data server on IBMCloud
THe data server is already live, manage by *IBM Cloud Foundry*
The main database entry points are:
Map request:
```
http://coolvest-persistent-platypus-ec.mybluemix.net/map
```
Event declaration. The <latitude>, <longitude>, <event_type> parameters must be set to the values boserved by the user:
```
http://coolvest-persistent-platypus-ec.mybluemix.net/point?key=<latitude>,<longitude>,<event_type>
```
Example:
```
http://coolvest-persistent-platypus-ec.mybluemix.net/point?key=1.36,103.82,MosquitoLarva
```

## Running the Tests
## Live Demo
You can find our map at http://coolvest-persistent-platypus-ec.mybluemix.net/map
To use our app download MozziGo.apk (however, our app only works on android)
## Built With
## Authors
## Acknowledgements
