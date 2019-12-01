import insightface
import urllib
import urllib.request
import cv2
import numpy as np
import time
import multiprocessing
import json


class EmbeddingGenerator:

    def printQueue(self):
        while not self.inputQueue.empty():
            print("thread "+str(self.threadNum)+" path "+str(self.inputQueue.get()))
            time.sleep(0.01)

    def getFaceData(self):
        print("thread "+str(self.threadNum)+" started")
        while True:
            if not self.inputQueue.empty():
                queueElement = self.inputQueue.get()
                deviceId = queueElement['deviceId']
                videoPath = queueElement['path']
                video = cv2.VideoCapture(videoPath)
                #video =cv2.VideoCapture(0)
                ret, frame = video.read()

                while ret:
                    if cv2.waitKey(1) & 0xFF == ord('q'):
                        break

                    faces = self.model.get(frame)
                    for idx, face in enumerate(faces):
                        #print("bbox = "+str(type(face.bbox))+" landmark ="+str(type(face.landmark))+" det_score = "+str(type(face.det_score))+" embedding ="+str(type(face.embedding))+" gender ="+ str(type(face.gender))+" age = "+str(type(face.age))+" normed_embedding="+str(type(face.normed_embedding))+" embedding_norm =" +str(type(face.embedding_norm)))
                        data = {}
                        data['deviceId'] = deviceId
                        data['time'] = video.get(cv2.CAP_PROP_POS_MSEC)
                        #self.outputQueue.put(face)
                        data['faceIndex']=str(idx)
                        data['bbox'] = face.bbox.tolist()
                        data['landmark'] = face.landmark.tolist()
                        data['det_score'] = str(face.det_score)
                        data['embedding']= face.embedding.tolist()
                        data['gender'] = str(face.gender)
                        data['age']= str(face.age)
                        data['normed_embedding'] = face.normed_embedding.tolist()
                        data['embedding_norm']=str(face.embedding_norm)
                        self.outputQueue.put(json.dumps(data))
                        cv2.rectangle(frame, (int(face.bbox[0]), int(face.bbox[1])), (int(face.bbox[2]), int(face.bbox[3])), (0, 0, 255), 5)
                    cv2.imshow('Processing on Thread '+str(self.threadNum), frame)
                    ret, frame = video.read()
                video.release()
                cv2.destroyAllWindows()

    def __init__(self, threadnum, inputQueue, outputQueue):
        self.threadNum = threadnum
        self.inputQueue = inputQueue
        self.outputQueue = outputQueue
        #self.printQueue()
        self.model = insightface.app.FaceAnalysis()
        self.ctx_id = 0
        self.model.prepare(ctx_id=self.ctx_id, nms=0.4)
        #p1= multiprocessing.Process(target=self.getFaceData)
        print("starting thread "+str(threadnum))
        #p1.start()
        self.getFaceData()
