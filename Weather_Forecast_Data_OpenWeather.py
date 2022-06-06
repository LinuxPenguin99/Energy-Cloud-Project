import requests
import json
import datetime
import logging
import time
import pandas as pd

interval = 60 * 24

paramDict = {
    'APPID' : '27f1e1d159dfea276d0324b12f46b902',
    'mode' : 'json',
    'lat' : '37.551066',
    'lon' : '127.075696',
    'units' : 'metric',
    'cnt' : '40'
}

def wait(min):
    now = datetime.datetime.now()
    remain_second = 60 - now.second + 1
    remain_second += 60 * (min - (now.minute % min + 1))
    time.sleep(remain_second)
    
def main():
    while True:
        url = 'http://api.openweathermap.org/data/2.5/forecast?'
        
        res = requests.get(url,params=paramDict)

        result = json.dumps(res.json(), indent=4, sort_keys=True)
        now_time = datetime.datetime.now().strftime('%Y%m%d %H:%M:%S')
        
        with open(now_time.split(" ")[0]+" "+now_time.split(" ")[1].split(":")[0]+".json", "w") as json_file:
            json.dump(result, json_file)

        print(now_time)
        print("File save complete")
        wait(interval)
    
    

if __name__ == '__main__':
    main()