import json
import re
import time
from collections import namedtuple

from myApp.untils.getPublicData import getAllcars


def getBaseData():
    cars = list(getAllcars())
    sumCar = len(cars)
    highVolume = cars[0].saleVolume
    topCar = cars[0].carName
    carModels = {}
    maxModel = 0
    mostModel = ''
    for i in cars:
        if carModels.get(i.carModel,-1) == -1 :
            carModels[str(i.carModel)] = 1
        else:
            carModels[str(i.carModel)] += 1
    carModels = sorted(carModels.items(), key=lambda x: x[1], reverse=True)
    mostModel = carModels[0][0]
    carBrands ={}
    maxBrand = 0
    mostBrand = ''
    for i in cars:
        if carBrands.get(i.brand,-1) == -1 :
            carBrands[str(i.brand)] = 1
        else:
            carBrands[str(i.brand)] += 1
    for k, v in carBrands.items():
        if v > maxBrand:
            maxBrand = v
            mostBrand = k
    carPrices ={}
    averagePrice = 0
    sumPrice = 0
    for i in cars:
        price_str = i.price
        match = re.match(r'(\d+\.?\d*)-(\d+\.?\d*)万', price_str)
        if match:
            # 获取价格范围
            min_price = float(match.group(1))
            max_price = float(match.group(2))
            average_price = (min_price + max_price) / 2
            sumPrice += average_price
        else:
            print(f"无法解析价格: {price_str}")
        # print(i.price)
        # x = json.loads(i.price)[0] + json.loads(i.price)[1]
        # sumPrice += x
    averagePrice = sumPrice / sumCar
    #保留两位小数
    averagePrice = round(averagePrice, 2)
    return sumCar,highVolume,topCar,mostModel,mostBrand,averagePrice

def getRollData():
    cars = list(getAllcars())
    carBrands = {}
    for i in cars:
        if carBrands.get(i.brand,-1) == -1 :
            carBrands[str(i.brand)] = 1
        else:
            carBrands[str(i.brand)] += 1
    brandList = [(value,key)for key,value in carBrands.items()]
    #排序取前10
    brandList = sorted(brandList, reverse=True)[:10]
    sortDict = {i[1]:i[0] for i in brandList}
    lastSortList = []
    for k,v in sortDict.items():
        lastSortList.append({
            'name': k,
            'value': v
        })
    return lastSortList

def getTypeRate():
    cars = list(getAllcars())
    carTypes = {}
    for i in cars:
        if carTypes.get(i.energyType,-1) == -1 :
            carTypes[str(i.energyType)] = 1
        else:
            carTypes[str(i.energyType)] += 1
    totalCars = sum(carTypes.values())
    oilRate = round(carTypes['汽油'] / totalCars * 100, 2)
    electricRate = round(carTypes['纯电动'] / totalCars * 100, 2)
    mixRate = round(((totalCars - carTypes['汽油'] - carTypes['纯电动']) / totalCars * 100), 2)
    print(f"汽油车数量: {carTypes['汽油']}")
    print(f"纯电动车数量: {carTypes['纯电动']}")
    print(f"总和: {carTypes['汽油'] + carTypes['纯电动']}")
    return oilRate, electricRate, mixRate