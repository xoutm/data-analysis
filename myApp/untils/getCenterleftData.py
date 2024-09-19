import json
import time
from . getPublicData import *

def getPieBrandData():
    cars = list(getAllcars())
    carVolume = {}
    for i in cars:
        if carVolume.get(i.brand,-1) ==-1:
            carVolume[str(i.brand)] = int(i.saleVolume)
        else:
            carVolume[str(i.brand)] += int(i.saleVolume)
    #排序
    carVolume = sorted(zip(carVolume.values(), carVolume.keys()), reverse=True)
    sortDict = {i[1]: i[0] for i in carVolume}
    lastPieList = []
    for k, v in sortDict.items():
        lastPieList.append({
            'name': k,
            'value': v
        })
    return lastPieList[:10]

