from myApp.models import *


def getAllcars():
    return CarInfo.objects.all()