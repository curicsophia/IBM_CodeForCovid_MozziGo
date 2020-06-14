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
### Our Problem
Dengue is a large and prevailing problem in SouthEast Asian countries such as Singapore. Circuit breaker due to COVID-19 is another factor, making this situation worse. When more people stay at home all day, there could be more residential mosquito breeding and more opportunities for 'blood meals'." Effective monitoring is one of the most important factors in preventing dengue from spreading in our community.
### How can technology help?
Here technology and big data are used to better visualize dengue hotspots and effectively target pest control.  It is an upstream solution for preventing the spread.
### Our Idea
Our solution is to introduce an app called MozzieGo which allows us to crowdsource mosquito sightings from the general public. Data is then sent to IBM cloud foundry which then returns the data in the form of a map.
## Our Demo
https://youtu.be/7eYQQLM63iA
## The Arcitecture
The project has 2 main componets:
1. User application, running on mobile phone
2. Data processing server, setup using cloud foundry and running on **IBM Cloud**
## The Long description
The long description of our project an be found at https://docs.google.com/document/d/1hbgReQhugyP_LoH-JBmeS0kD3nk_brT0FU1I2KtGonQ/edit?usp=sharing
## Our Project Roadmap
This is our project's roadmap.
https://docs.google.com/presentation/d/1eeWZ2JvRmoypdHL7c7zSHHGMNnslv40GaT8cyIdjgUQ/edit?usp=sharing
## Getting Started
There are 2 commponents: user mobile phone application and data server
### Mobile Phone application:
This is the link to the apk file which you can use to download our app. https://drive.google.com/file/d/1bovsgcI7Vx_0asrQeSmuO8mwrBFcIxZJ/view?usp=sharing
Download the APK file to your Android mobile phone (eg. email or data transfer) and open it to install our application
To view our thunkable code go to https://x.thunkable.com/projectPage/5ee5a8d0a68c746165237a1f.
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
To view our thunkable code go to https://x.thunkable.com/projectPage/5ee5a8d0a68c746165237a1f.

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
