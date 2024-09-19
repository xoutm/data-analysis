import jieba
from matplotlib import pylab as plt
from wordcloud import WordCloud
import numpy as np
from PIL import Image
from pymysql import *
import json

def get_img(field,targetImageSrc,resImageSrc):
    conn = connect(host='127.0.0.1', user='root', passwd='123456', db='cardata',port=3306,charset='utf8mb4')
    cursor = conn.cursor()
    sql = f"select {field} from myApp_carinfo"
    cursor.execute(sql)
    data = cursor.fetchall()

    text = ''
    for i in data:
        if i[0] != '':
            tagArr = i
            for j in tagArr:
                text += j
    cursor.close()
    conn.close()
    data_cut = jieba.cut(text, cut_all=False)
    string = ' '.join(data_cut)

    #img
    img = Image.open(targetImageSrc)
    img_array = np.array(img)
    wc = WordCloud(
        #查找电脑字体
        font_path='Arial Unicode.ttf',
        mask=img_array,
        background_color= '#04122c'
    )
    wc.generate_from_text(string)
    #绘制图片
    fig = plt.figure(1)
    plt.imshow(wc)
    plt.axis('off')
    plt.savefig(resImageSrc,dpi=800,bbox_inches='tight',pad_inches=-0.1)

get_img('manufacturer','./big-screen-vue-datav-master/public/carcloud.png','./big-screen-vue-datav-master/public/car_cloud.png')
