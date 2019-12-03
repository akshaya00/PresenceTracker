This project provides a server for faster predictions of faces. It is based on the insightface project.

This project avoids reloading of the prediction model for every call rather runs dedicated process that utilise a shared queue

Dependencies:
1. Install mxnet according to system configuration
2. Install insighface
3. Install flask

Change value of the variables in __settings.py__ to set the number of process launch for the tasks 
```
Number_of_prediction_threads
Number_of_responding_threads 
```

Also change the values of the database server

Currently it just processes videos on the local storage.

Sample for the json used in post request 
```
{
	"deviceId":"1aefcd232",
	"path":"/home/user/Desktop/ML/tracking_video_data/stay.mp4"
}
``` 