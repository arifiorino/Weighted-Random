import random

def weightedRandom(options, weights): #weights is function or list
    if hasattr(weights, '__call__'):
        weights=[weights(option) for option in options]
    r=random.random()*sum(weights)
    for i in range(len(weights)):
        if r<sum(weights[0:i+1]):
            return options[i]

from PIL import Image

img = Image.open("Lenna.png")
width,height=img.size[0],img.size[1]
print(img.size)
pixels = img.load()

# for y in range(img.size[1]):
#     for x in range(img.size[0]):
#         r,g,b=pixels[x,y]
#         r=weightedRandom(range(0,255), lambda a:(-abs(a-r)+255)**4)
#         g=weightedRandom(range(0,255), lambda a:(-abs(a-g)+255)**4)
#         b=weightedRandom(range(0,255), lambda a:(-abs(a-b)+255)**4)
#         pixels[x,y] = (r,g,b)
#     print(round(y/img.size[1]*100,2),"%")

for i in range(10000):
    x=weightedRandom(range(0,img.size[0]), lambda a:(-abs(a-width*.5)+width*.5)**3)
    y=weightedRandom(range(0,img.size[1]), lambda a:(-abs(a-height*.5)+height*.5)**3)
    r,g,b=pixels[x,y]
    r=weightedRandom(range(0,255), lambda a:(-abs(a-r)+255)**6)
    g=weightedRandom(range(0,255), lambda a:(-abs(a-g)+255)**6)
    b=weightedRandom(range(0,255), lambda a:(-abs(a-b)+255)**6)
    pixels[x,y] = (r,g,b)
    if i%500==0:
        print(round(i/10000*100,2),"%")

img.save("Lenna Weighted Random2.png")
img.show()