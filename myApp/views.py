from django.http import JsonResponse
from django.shortcuts import render
from .untils import (getCenterData,getPublicData,getCenterleftData,
                     getBottomLeftData,getCenterRightData,getCenterRightChange,
                     getbottomRightData)
# Create your views here.
def center(request):
    if request.method == 'GET':
        sumCar, highVolume, topCar, mostModel, mostBrand, averagePrice = getCenterData.getBaseData()
        lastSortList = getCenterData.getRollData()
        oilRate, electricRate, mixRate = getCenterData.getTypeRate()
        return JsonResponse({
            'sumCar': sumCar,
            'highVolume': highVolume,
            'topCar': topCar,
            'mostModel': mostModel,
            'mostBrand': mostBrand,
            'averagePrice': averagePrice,
            'lastSortList': lastSortList,
            'oilRate': oilRate,
            'electricRate': electricRate,
            'mixRate': mixRate
        })

def centerLeft(request):
    if request.method == 'GET':
        lastPieList = getCenterleftData.getPieBrandData()
        return JsonResponse({
            'lastPieList': lastPieList
        })

def bottomLeft(request):
    if request.method == 'GET':
        brandList,volumeList,priceList = getBottomLeftData.getSquarData()
        return JsonResponse({
            'brandList': brandList,
            'volumeList': volumeList,
            'priceList': priceList
        })

def centerRight(request):
    if request.method == 'GET':
        realData = getCenterRightData.getPriceSortData()
        return JsonResponse({
            'realData': realData
        })

def centerRightChange(request,energyType):
    if request.method == 'GET':
        oilData, electricData = getCenterRightChange.getCircleData()
        realData = []
        if energyType == 1:
            realData = oilData
        else:
            realData = electricData
        return JsonResponse({
            'realData': realData
        })

def bottomRight(request):
    if request.method == 'GET':
        carData = getbottomRightData.getRankData()
        return JsonResponse({
            'carData': carData
        })