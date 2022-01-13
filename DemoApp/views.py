from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import status
from .serializers import RestaurantSerializer
from .models import Restaurant
# Create your views here.
import requests
import json
import datetime

weekDay=dict()
weekDay[1]='monday'
weekDay[2]='tuesday'
weekDay[3]='wednesday'
weekDay[4]='thursday'
weekDay[5]='friday'
weekDay[6]='saturday'
weekDay[0]='sunday'


def timeconvert(str1):
    print(str1)
    if str1[1]==':':
        str1='0'+str1

    
    if str1[-2:] == "AM" and str1[:2] == "12":
        return "00" + str1[2:-2]
    elif str1[-2:] == "AM":
        return str1[:-2]
    elif str1[-2:] == "PM" and str1[:2] == "12":
        return str1[:-2]
    else:
        return str(int(str1[:2]) + 12) + str1[2:8]

def extract_time(str):
    time=list()
    if str[2]==':':
        time.append(int(str[0:2]))
        time.append(int(str[3:5]))
    else:
        time.append(int('0'+str[0:1]))
        time.append(int(str[2:4]))

    return time      

class RestaurantViewSet(viewsets.ViewSet):
    def list(self, request):
        params=request.GET.get('type','')
        	
        # using now() to get current time
        current_time = datetime.datetime.today()
        day=current_time.weekday()
        curr_time=current_time.today().strftime("%I:%M %p")
        query_set=Restaurant.objects.filter(res_type=params)
        serializer=RestaurantSerializer(query_set,many=True)
        res_data=list()

        

        for x in serializer.data:
            time=extract_time(x['hours'][weekDay[day]]['opens_at'])
            d1 = datetime.datetime(current_time.year, current_time.month, current_time.day, time[0], time[1], 00) 
            time=extract_time(x['hours'][weekDay[day]]['closes_at'])
            d2= datetime.datetime(current_time.year, current_time.month, current_time.day, time[0], time[1], 00)
            d3 = datetime.datetime(current_time.year, current_time.month, current_time.day, current_time.hour, current_time.minute, current_time.second,00)
            time1=timeconvert(d1.strftime("%H:%M:%S %p"))
            time2=timeconvert(d2.strftime("%H:%M:%S %p"))
            time3=timeconvert(d3.strftime("%H:%M:%S %p"))

            print(time1, time2, time3)
            print(x['hours'][weekDay[day]])

            if(time1<=time3 and time2>=time3):
                res_data.append(x)   

        
        return Response(res_data)
   
    def create(self,request):
        URL = "https://random-data-api.com/api/restaurant/random_restaurant"

        r = requests.get(url = URL)
        data=r.json()
        tmp=dict()
        tmp['name']=data['name']
        tmp['res_type']=data['type']
        tmp['description']=data['description']
        tmp['hours']=data['hours']

        print(tmp)

        serializer = RestaurantSerializer(data=tmp)
        if serializer.is_valid():
            serializer.save()
        else:
            print("invalid")
        
        return Response("Data Created!!", status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        id = pk
        if id is not None:
            stu = Restaurant.objects.get(id=id)
            serializer = RestaurantSerializer(stu)
        return Response(serializer.data)
        
