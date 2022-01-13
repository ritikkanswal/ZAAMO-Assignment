import requests
import json

URL = "http://127.0.0.1:8000/restaurantapi/"

tmp={}

for i in range(0,100):
    r = requests.post(url = URL,data=tmp)
    print("Successfully Inserted :",i," restaurant data")
