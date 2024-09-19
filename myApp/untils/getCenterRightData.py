import json
import time
import re
from . getPublicData import *

def getPriceSortData():
    cars = list(getAllcars())
    PriceSortList = {'0-5W':0,'5-10W':0,'10-20W':0,'20-30W':0,'30W以上':0,}
    for i in cars:
        price_str = i.price
        match = re.match(r'(\d+\.?\d*)-(\d+\.?\d*)万', price_str)
        if match:
            min_price = float(match.group(1))
            # 根据价格区间将车辆计入相应的区间
            if min_price < 5:
                PriceSortList['0-5W'] += 1
            elif min_price >= 5 and min_price < 10:
                PriceSortList['5-10W'] += 1
            elif min_price >= 10 and min_price < 20:
                PriceSortList['10-20W'] += 1
            elif min_price >= 20 and min_price < 30:
                PriceSortList['20-30W'] += 1
            else:
                PriceSortList['30W以上'] += 1
    realData = []
    for k,v in PriceSortList.items():
        realData.append({
            'name':k,
            'value':v
        })
    return realData

