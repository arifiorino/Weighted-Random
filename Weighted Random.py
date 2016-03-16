import random

def weightedRandom(options, weights): #weights is function or list
    if hasattr(weights, '__call__'):
        weights=[weights(option) for option in options]
    r=random.random()*sum(weights)
    for i in range(len(weights)):
        if r<sum(weights[0:i+1]):
            return options[i]

from PIL import Image

def weight(x):
    if x<50:
        return (-abs(x-25)+25)**3
    else:
        return (-abs(x-75)+25)**3

img = Image.new('RGB', (100,100), "white") # create a new black image
pixels = img.load() # create the pixel map

points=[(x,y) for x in range(img.size[0]) for y in range(img.size[1])]
for i in range(5000):
    
    x=weightedRandom(range(0,100), weight)
    y=weightedRandom(range(0,100), weight)
    pixels[x,y] = (0,)*3

img.show()
img.save("Weighted Random.png")