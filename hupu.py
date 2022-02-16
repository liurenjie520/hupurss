import dicttoxml as dicttoxml
import requests as requests
import xmltodict
import json
import os
from flask import *
import AddXML

def hupuapi():
    res = requests.get("https://api.tophub.fun/v2/GetAllInfoGzip?id=2&page=0&type=pc")

    fg = res.text
    data_dict = json.loads(fg)['Data']['data']
    # data_dict=data_dict.json()
    print(type(data_dict))
    print((data_dict))
    for i in data_dict:
        # print(i)
        Title = i['Title']
        Url = i['Url']
        # print(i['Title'])
        AddXML.add_newxml(Title, Title, Url)
    return "ok"



if __name__ == '__main__':
    hupuapi()
