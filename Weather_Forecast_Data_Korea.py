import requests
import json
import time
import datetime
import schedule # Module to make code run automatically

def api_call(): # API Call Function
    now = datetime.datetime.now()
    date = str(now).split(' ')[0]
    time = str(now).split(' ')[1]
    basedate = date.split('-')[0] + date.split('-')[1] + date.split('-')[2]
    basetime = time.split(':')[0] + '00'
    url = 'http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getVilageFcst'
    params ={'serviceKey' : '', 'pageNo' : '1', 'numOfRows' : '1000', 'dataType' : 'json', 'base_date' : basedate, 'base_time' : basetime, 'nx' : '73', 'ny' : '67' } 
    # Service Key Needed
    # nx, ny : 지역 좌표
    
    response = requests.get(url, params=params)
    print(response) # Check response for errors
    result = json.dumps(response.json(), indent=4, sort_keys=True)

    with open('./' + basedate + '_' + time.split(':')[0] +'.json', 'w', encoding="UTF-8") as json_file:
        json.dump(result, json_file)
    # Change Path If You Want
    
    print(basedate, basetime, 'Completed!') # Optional


# Work at setted time
schedule.every().day.at('02:11').do(api_call)
schedule.every().day.at('05:11').do(api_call)
schedule.every().day.at('08:11').do(api_call)
schedule.every().day.at('11:11').do(api_call)
schedule.every().day.at('14:11').do(api_call)
schedule.every().day.at('17:11').do(api_call)
schedule.every().day.at('20:11').do(api_call)
schedule.every().day.at('23:11').do(api_call)

# Make sure to run this code at setted time
while True:
    schedule.run_pending()
    print(datetime.datetime.now(), 'status = normal') # Status Check
    time.sleep(0.1) # Delay
