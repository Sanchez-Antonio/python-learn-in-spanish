import argparse

import requests

parser = argparse.ArgumentParser(description="***Avaliable Arguments***")

parser.add_argument('-t',dest="object",type=str,help="Enter web adress-> Url https://example.com/" )

parser = parser.parse_args()

if parser.object:
    try:
       url=requests.get(url=parser.objetc)
       cabezera=dict(url.headers)
       
       for value,key in cabezera.items():
       
           print(f"{key} : {value}")
    except:
           print("Connection Error")
else:
    print("the data was not entered")

