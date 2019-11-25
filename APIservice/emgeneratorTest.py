import time
from embeddingGenerator import EmbeddingGenerator
import urllib
import numpy as np
import cv2
import threading
import multiprocessing as mp

def createNewGenerator(i,inputQueue,outputQueue):
    a = EmbeddingGenerator(i, inputQueue,outputQueue)

def printOutput(outputQueue):
    while True:
        if not outputQueue.empty():
            face = outputQueue.get()
            print("age:%d" % (face.age))
            #print("landmark:%s" % (face.landmark.astype(np.int).flatten()))

def test():
    path1 = "/home/akshaya/Desktop/ML/tracking_video_data/go_left.mp4"
    path2 = "/home/akshaya/Desktop/ML/tracking_video_data/go_up.mp4"
    path3 = "/home/akshaya/Desktop/ML/tracking_video_data/stay.mp4"
    videoQueue = mp.Queue()
    for i in range(1):
        videoQueue.put(path1)
        videoQueue.put(path2)
        videoQueue.put(path3)
    outputQueue = mp.Queue()
    p1= mp.Process(target=createNewGenerator, args=(1, videoQueue, outputQueue))
    #p1.daemon = True
    p1.start()
    p2 = mp.Process(target=createNewGenerator, args=(2, videoQueue, outputQueue))
    #p2.daemon = True
    p2.start()
    p3 = mp.Process(target=printOutput, args=(outputQueue,))
    #p3.daemon = True
    p3.start()
    for i in range(1):
        videoQueue.put(path1)
        videoQueue.put(path2)
        videoQueue.put(path3)

test()