import json
import time
from . getPublicData import *

def getRankData():
    cars = list(getAllcars())
    carData = []
    for car in cars:
        carData.append({
            'brand': car.brand,
            'rank': car.rank,
            'carName': car.carName,
            'carImg': car.carImg,
            'manufacturer': car.manufacturer,
            'carModel': car.carModel,
            'price': car.price,
            'saleVolume': car.saleVolume,
            'marketTime': car.marketTime,
            'insure': car.insure,
        })
    return carData