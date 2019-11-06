import insightface
import urllib
import urllib.request
import cv2
import numpy as np
import asyncio
import time

class EmbeddingGenerator:

    def __init__(self):
        self.model = insightface.app.FaceAnalysis()
        self.ctx_id = 0
        self.model.prepare(ctx_id=self.ctx_id, nms=0.4)
        self.isBusy = False

    def addFaceData(self, image, lock):
        lock.acquire()
        print("Is busy to add : " + str(self.isBusy))
        x = []
        if self.isBusy:
            x = [False, None]
        else:
            self.isBusy = True
            x = [True, self.getFaceData(image)]
        lock.release()
        return x

    async def getFaceData(self, image):
        faces = self.model.get(image)

        for idx, face in enumerate(faces):
            print("Face [%d]:" % idx)
            """print("\tage:%d" % (face.age))
            gender = 'Male'
            if face.gender == 0:
                gender = 'Female'
            print("\tgender:%s" % (gender))
            print("\tembedding shape:%s" % face.embedding.shape)
            #	print(face.embedding)
            print("\tbbox:%s" % (face.bbox.astype(np.int).flatten()))
            print("\tlandmark:%s" % (face.landmark.astype(np.int).flatten()))
            print("")
            """
        # print ("Result from getFaceData, isBusy " + str(self.isBusy))
        self.isBusy = False
        return True

    def generatorIsBusy(self):
        return self.isBusy