import json
import time
import re
from . getPublicData import *


def getSquarData():
    cars = list(getAllcars())
    carsVolume = {}
    for i in cars:
        if carsVolume.get(i.carName, -1) == -1:
            carsVolume[i.carName] = int(i.saleVolume)
        else:
            carsVolume[i.carName] += int(i.saleVolume)
    carSortVolume = sorted(carsVolume.items(), key=lambda x: x[1], reverse=True)[:12]
    brandList = []
    volumeList = []
    priceList = []
    for i in carSortVolume:
        brandList.append(i[0])
        volumeList.append(i[1])
    for i in cars[:12]:
        i.price = re.findall('\d+\.\d+', i.price)
        i.price = i.price[0]
        priceList.append(float(i.price))
    return brandList, volumeList, priceList



