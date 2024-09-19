import requests
from lxml import etree
import csv,os,time,json,re,django
import pandas as pd
from sqlparse.utils import offset

os.environ.setdefault('DJANGO_SETTINGS_MODULE', '车辆大屏可视化.settings')
django.setup()
from myApp.models import *

class spider(object):
    def __init__(self):
        self.spiderUrl = "https://www.dongchedi.com/motor/pc/car/rank_data?aid=1839&app_name=auto_web_pc&city_name=%E8%A5%BF%E5%AE%89&count=10&month=&new_energy_type=&rank_data_type=11&brand_id=&price=&manufacturer=&outter_detail_type=&nation=0"
        self.headers = {
            'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'
        }
    def init(self):
        if not os.path.exists('./tmp.csv'):
            with open('./tmp.csv','a',newline='',encoding='utf-8') as wf:
                writer = csv.writer(wf)
                writer.writerow(["brand",
                                "carName",
                                "carImg",
                                "saleVolume",
                                "price",
                                "manufacturer",
                                "rank",
                                "carModel",
                                "energyType",
                                "marketTime",
                                "insure"
                               ])
    def getpage(self):
        with open('./spiders.txt','r') as r_f:
            return r_f.readlines()[-1].strip()
    def setpage(self,newpage):
        with open('./spiders.txt','a') as a_f:
            a_f.write('\n'+str(newpage)+'\n')
    def main(self):
        count = self.getpage()
        params ={
            'offset':int(count)
        }
        print("数据从{}开始爬取".format(int(count)+1))
        pageJosn = requests.get(self.spiderUrl, headers=self.headers, params=params).json()
        pageJosn = pageJosn["data"]["list"]
        # print(pageJosn)
        # self.setpage(int(count)+10)
        try:
            for index, car in enumerate(pageJosn):
                carData = []
                print("正在爬取第%d" % (index + 1) + "条数据")
                # print(car["brand_name"])
                carData.append(car["brand_name"])
                carData.append(car["series_name"])
                carData.append(car["image"])
                carData.append(car["count"])
                price = []
                price.append(car["min_price"])
                price.append(car["max_price"])
                carData.append(car["price"])
                carData.append(car["sub_brand_name"])
                carData.append(car["rank"])
                carNumber = car["series_id"]
                infoHTML = requests.get("https://www.dongchedi.com/auto/params-carIds-x-%s" % carNumber,
                                        headers=self.headers)
                infoHTMLpath = etree.HTML(infoHTML.text)
                carModel = infoHTMLpath.xpath("//div[@data-row-anchor='jb']/div[2]/div/text()")[0]
                carData.append(carModel)
                energyType = infoHTMLpath.xpath("//div[@data-row-anchor='fuel_form']/div[2]/div/text()")[0]
                carData.append(energyType)
                marketTime = infoHTMLpath.xpath("//div[@data-row-anchor='market_time']/div[2]/div/text()")[0]
                carData.append(marketTime)
                insure = infoHTMLpath.xpath("//div[@data-row-anchor='period']/div[2]/div/text()")[0]
                carData.append(insure)
                # print(carData)
                self.save_to_csv(carData)
        except:
            pass
        self.setpage(int(count)+10)
        self.main()
            #break
    def save_to_csv(self,resultData):
        with open('./tmp.csv','a',newline='',encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(resultData)
    def clear_csv(self):
        df = pd.read_csv('./tmp.csv')
        #去除空值,去重
        df.dropna(inplace=True)
        df.drop_duplicates(inplace=True)
        print("总数量为%d"%df.shape[0])
        return df.values
    def save_to_sql(self):
        data = self.clear_csv()
        for car in data:
            CarInfo.objects.create(
                brand=car[0],
                carName=car[1],
                carImg=car[2],
                saleVolume=car[3],
                price=car[4],
                manufacturer=car[5],
                rank=car[6],
                carModel=car[7],
                energyType=car[8],
                marketTime=car[9],
                insure=car[10]
            )


if __name__ == '__main__':
    spiderObj=spider()
    #spiderObj.init()
    #spiderObj.main()
    spiderObj.save_to_sql()