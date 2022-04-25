import json
import requests

url = "https://data.ntpc.gov.tw/api/datasets/71CD1490-A2DF-4198-BEF1-318479775E8A/json?page=0&size=1000"

source_data = requests.get(url)  #type "byte"
text_data = source_data.text     #type "str"
JS_data = json.loads(text_data)  #type  "list"

name = input("請輸入尋找的區域：")

for i in JS_data:
    if i["sarea"] == name:
        print("站別：",i["sna"])
        print("可停：",i["bemp"])
        print("可借：",i["sbi"])

else:
    print("您輸入的區域不在系統內")
        
        


