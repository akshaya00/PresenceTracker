from flask import Flask
from flask import request
from embeddingGenerator import EmbeddingGenerator
import multiprocessing
import settings
import requests
import json

app = Flask(__name__)


def createGenerator(i,inputQueue, outputQueue):
    generator = EmbeddingGenerator(i,inputQueue, outputQueue)


def startPredictionProcesses(inputQueue, outputQueue):
    for generatorCount in range(settings.Number_of_responding_threads):
        process = multiprocessing.Process(target=createGenerator, args=(generatorCount,inputQueue,outputQueue))
        process.start()

def Replier(outputQueue):
    server = settings.database_server
    while True:
        if not outputQueue.empty():
            data = outputQueue.get()
            requests.post(server, json=data)


def startReplyServer(outputQueue):
    process = multiprocessing.Process(target=Replier, args=(outputQueue,))
    process.start()



@app.route('/getpredictions',methods = ['POST','GET'])
def getPredictions():
    content = request.json
    inputQueue.put(content)
    return "Success"


if __name__ == '__main__':
    inputQueue = multiprocessing.Queue()
    outputQueue = multiprocessing.Queue()
    startPredictionProcesses(inputQueue, outputQueue)
    startReplyServer(outputQueue)
    app.run(port=5000)
