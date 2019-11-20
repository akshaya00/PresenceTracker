import time
from embeddingGenerator import EmbeddingGenerator
import urllib
import numpy as np
import cv2
import asyncio
import threading

def url_to_image(url):
    resp = urllib.request.urlopen(url)
    image = np.asarray(bytearray(resp.read()), dtype="uint8")
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)
    return image

async def test():
    #url1 = 'https://d1u4oo4rb13yy8.cloudfront.net/article-eitxocsxxw-1460737394.jpeg'         #30people
    url2 = 'https://www.cbs17.com/wp-content/uploads/sites/29/2019/10/150003.jpg'            #1person
    url3 = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQY7wxkXILmBJEbvLqG1k31Zp9bK3USnlx4D6h1IJjN92wJFqui&s' #3people
    img = []

    #img.append(url_to_image(url1))
    img.append(url_to_image(url2))
    img.append(url_to_image(url3))
    img = img * 5
    print("len of img " + str(len(img)))

    lg = []
    for i in range(0, 2):
        a = EmbeddingGenerator()
        lg.append(a)
        print("is coroutine function "+ str(asyncio.iscoroutinefunction(a.getFaceData(img[0]))))
    #b = EmbeddingGenerator()
    #await asyncio.gather(*l)

    lock = threading.Lock()
    i = 0
    while i < len(img):
        facetask = []
        for j in range(0, 2):
            r = lg[j].addFaceData(img[i], lock)
            print (r)
            if r[0]:
                print("calling object " + str(j))
                facetask.append(r[1])
                i += 1
            else:
                print("busy object " + str(j))
                continue
        await asyncio.wait(facetask)



    """b = EmbeddingGenerator()
    lg = [a,b]
    while True:
        for l in lg:
            if(l.generatorIsBusy):
                continue
            else:
                l.getFaceData(img)
    """

loop = asyncio.get_event_loop()
loop.run_until_complete(test())