import requests
import json
import time
import datetime

def api_call(old_response): # parameter : previous response
    now = datetime.datetime.now()
    date = str(now).split(' ')[0]
    time = str(now).split(' ')[1]
    basedate = date.split('-')[0] + date.split('-')[1] + date.split('-')[2]
    basetime = time.split(':')[0] + '00'
    url = 'http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getVilageFcst'
    params ={'serviceKey' : '', 'pageNo' : '1', 'numOfRows' : '1000', 'dataType' : 'json', 'base_date' : basedate, 'base_time' : basetime, 'nx' : '', 'ny' : '' } # serviceKey : 서비스키, nx : x좌표, ny : y좌표
    
    response = requests.post(url, params=params)
    
    
    if response.json() == old_response: # Compare response
        print('Same Data as Before')
        return old_response

    # Error Exception (Server Data not Renewed or Server's Problem)
    try:
        result = json.dumps(response.json(), indent=4, sort_keys=True)
        with open('./' + basedate + '_' + time.split(':')[0] +'.json', 'w', encoding="UTF-8") as json_file:
            json.dump(result, json_file)
        print('New Response Save Complete')
        return response.json()
    except:
        print('Server Data is not Renewed')
        return old_response
    
if __name__ == '__main__':
    old_response = ''
    while True:
        old_response = api_call(old_response)
        time.sleep(600) # 10 minutes
        
'''
New Code
1. Server Data renew time is irregular
2. Work every 0.1s waste memory
3. Prevent Data overlapping

Previous Code
1. Work every 0.1s
2. Request only set time
3. Data overlapping is possible
4. Error occurred, code stopped

Changed Logic
1. Repeat Time : 0.1 sec -> 10 min == Memory Resource Save
2. Make exception function -> Prevent Code stopped
3. Compare Response with previous Code 
4. Previous Code Flag = Time
5. New Code Flag = Previous Response
'''