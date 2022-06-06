import os
import requests
import json

year = []
for i in range(1970, 2023):
    year.append(i)

day = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 

# Measured Point
point = {'90' : '속초', '93' : '북춘천', '95' : '철원', '98' : '동두천', '99' : '파주','100' : '대관령', '101' : '춘천', '102' : '백령도', '104' : '북강릉', '105' : '강릉', '106' : '동해', '108' : '서울', '112' : '인천', '114' : '원주', '115' : '울릉도', '119' : '수원', '121' : '영월', '127' : '충주', '129' : '서산', '130' : '울진', '131' : '청주', '133' : '대전','135' : '추풍령', '136' : '안동', '137' : '상주', '138' : '포항', '140' : '군산', '143' : '대구', '146' : '전주', '152' : '울산', '155' : '창원', '156' : '광주', '159' : '부산', '162' : '통영', '165' : '목포', '168' : '여수', '169' : '흑산도', '170' : '완도', '172' : '고창', '174' : '순천', '177' : '홍성', '184' : '제주', '185' : '고산', '188' : '성산', '189' : '서귀포', '192' : '진주', '201' : '강화', '202' : '양평', '203' : '이천', '211' : '인제', '212' : '홍천', '216' : '태백', '217' : '정선군', '221' : '제천', '226' : '보은', '232' : '천안', '235' : '보령', '236' : '부여', '238' : '금산', '239' : '세종', '243' : '부안', '244' : '임실', '245' : '정읍', '247' : '남원', '248' : '장수', '251' : '고창군', '252' : '영광군', '253' : '김해시', '254' : '순창군', '255' : '북창원', '257' : '양산시', '258' : '보성군', '259' : '강진군', '260' : '장흥', '261' : '해남', '262' : '고흥', '263' : '의령군', '264' : '함양군', '266' : '광양시', '268' :'진도군', '271' : '봉화', '272' : '영주', '273' : '문경', '276' : '청송군', '277' : '영덕', '278' : '의성', '279' : '구미', '281' : '영천', '283' : '경주시', '284' : '거창', '285' : '합천', '288' : '밀양', '289' : '산청', '294' : '거제', '295' : '남해'}


for k in point:
    os.makedirs('./Weather_Actual Data/{}_json'.format(str(point[k])))
    for i in year:
        for j in range(1,13):

                dic = {1:'31', 2:'28', 3:'31', 4:'30', 5:'31', 6:'30', 7:'31', 8:'31', 9:'30', 10:'31', 11:'30', 12:'31'}
                if i == 2022 and dic[j] == 5:
                    dic[j] = '25'
                if i == 2022 and dic[j] == 6:
                    break
                paramDict = {

                    'serviceKey' : '', # Certificate key
                    'numOfRows' : '744',
                    'pageNo' : '1',
                    'dataType' : 'JSON',
                    'dataCd' : 'ASOS',
                    'dateCd' : 'HR',
                    'startDt' : str(i) + str('%02d' %j) + '01',
                    'startHh' : '00',
                    'endDt' : str(i) + str('%02d' %j) + dic[j],
                    #'endDt' : str(i) + str('%02d' %j) + '23', # If download specific date

                    'endHh' : '23',
                    'stnIds' : k

                }

                url = 'http://apis.data.go.kr/1360000/AsosHourlyInfoService/getWthrDataList' # Meteorological Agency API

                res = requests.get(url, params=paramDict)

                result = json.dumps(res.json(), indent=4, sort_keys=True)

                with open('./Weather_Actual Data/' + '{}_json/'.format(point[k]) + str(i) + '_' + str('%02d' %j) +'.json', 'w', encoding="UTF-8") as json_file:
                    json.dump(result, json_file)
                # Change Path you want to save
                
                
                print(result) # Optional