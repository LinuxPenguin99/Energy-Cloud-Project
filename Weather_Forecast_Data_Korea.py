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
    
    # Error Exception (Server Data not Renewed or Server's Problem)
    try:
        response = requests.get(url, params=params)
        data = response.json() # Response to json
        if data == old_response: # Compare response
            print('Same Data as Before')
            return old_response
        elif data['response']['header']['resultMsg'] == 'NO_DATA':
            '''
            RESPONSE TEST
            print(response.json())
            print(data['response']['header']['resultMsg']) # Get response Result Message Content
            '''
            print('NO_DATA')
            return old_response
        # NO_DATA Response is not need to save
        else:
            result = json.dumps(response.json(), indent=4, sort_keys=True)
            with open('./' + basedate + '_' + time.split(':')[0] +'.json', 'w', encoding="UTF-8") as json_file:
                json.dump(result, json_file)
            print('New Response Save Complete')
            return response.json()
    except:
        print('Error occurred. Try again after 10 minutes.')
        return old_response
    
if __name__ == '__main__':
    old_response = ''
    while True:
        old_response = api_call(old_response)
        time.sleep(600) # 10 minutes
        
'''
Changes
1. Move the response into the try -> Code stopped by response issue is solved. 
2. 'NO_DATA' case is added -> NO_DATA response saved issue is solved.
(It caused by change 1)
'''