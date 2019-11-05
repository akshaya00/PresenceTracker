from embeddingGenerator import EmbeddingGenerator
import urllib
import numpy as np
import cv2
import asyncio

def url_to_image(url):
    resp = urllib.request.urlopen(url)
    image = np.asarray(bytearray(resp.read()), dtype="uint8")
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)
    return image

async def test():
    #url = 'https://d1u4oo4rb13yy8.cloudfront.net/article-eitxocsxxw-1460737394.jpeg'         #30people
    #url = 'https://www.cbs17.com/wp-content/uploads/sites/29/2019/10/150003.jpg'            #1person
    url ='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQY7wxkXILmBJEbvLqG1k31Zp9bK3USnlx4D6h1IJjN92wJFqui&s' #3people
    img = url_to_image(url)
    lg=[]
    l = []
    for i in range(0,2):
        a = EmbeddingGenerator()
        lg.append(a)
        print("is coroutine function "+ str(asyncio.iscoroutinefunction(a.getFaceData(img))))
    #b = EmbeddingGenerator()
    #await asyncio.gather(*l)
    for i in range(0,5):
        for j in range(0,2):
            if lg[j].generatorIsBusy():
                print("busy object "+str(j))
                continue
            else:
                print("calling object "+str(j))
                #lg[j].setGeneratorBusy()
                asyncio.ensure_future(lg[j].getFaceData(img))



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