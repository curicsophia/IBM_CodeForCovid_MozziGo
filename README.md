# MozziGo
This github repository contains our **IBM Code for Covid** project and its documentation files.
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
2. Date processign server, running on **IBM Cloud**
## The Long description
TODO
## Our Project Roadmap
This is our project's roadmap.
![Roadmap](Capture12.png)
## Getting Started
There are 2 commponents: user mobile phone application and data server
### Mobile Phone application:
The github repostiory contains an **Android APK** file:
```
TODO location of APK
```
Download the APK file to your Android mobile phone (eg. email or data transfer) and open it to install our application
### Data server on IBM Cloud
The data server is already live, managed by **IBM Cloud Foundry**
The main database entry points are:
- Map request:  
http://coolvest-persistent-platypus-ec.mybluemix.net/map  
- Event declaration. The `<latitude>`, `<longitude>`, `<event_type>` parameters must be set to the values observed by the user:
```
http://coolvest-persistent-platypus-ec.mybluemix.net/point?key=<latitude>,<longitude>,<event_type>
```
Example:
```
http://coolvest-persistent-platypus-ec.mybluemix.net/point?key=1.36,103.82,MosquitoLarva
```
A full description on how to create an **IBM CLoud** account and push a project to the **IBM Cloud Foundry** can be found in out github repository file:
```
TODO Full install walkthrough file
```
## Running the Tests
There are no automated tests associated with this project.
The mobile application was developped using **Thunkable** and the web server was developed using **Python** and **Flask**.
Application testing was done in the development environment.

## Live Demo
The folowing scenario will demonstrate some basic project functionalities:
1. Use the warning visualisation map. Browse to:  
http://coolvest-persistent-platypus-ec.mybluemix.net/map  
You can pan and zoom the map to see the mosquito sighting points.
Event selection controls (top right corner of the map) allow you to filter and browse specific sighting types.

2. Open your **MozziGo** Android phone application.
The application can be installed by downloading the **Android APK** `MozziGo.apk` from this git repository.
Follow application menus to add a new mosquito warning. The application will set the warning location to your phone location.

3. Return to the visualisation map and refresh it. You will be able to see that the warning you created has been added to the database. 
## Built With
- IBM Cloud Foundry - https://www.ibm.com/sg-en/cloud/cloud-foundry
- Thunkable - https://thunkable.com/home/
- Python - https://www.python.org/
- Flask - https://flask.palletsprojects.com/en/1.1.x/
- Folium - https://pypi.org/project/folium/
- Pandas - https://pandas.pydata.org/
- Numpy - https://numpy.org/
## Authors
Sophia Curic
Anjali Curic
Dayanita Saminathan
Kaela Teh
