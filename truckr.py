#!/usr/bin/python

import requests, json

headers = {'Content-Type': 'application/json'}

#login to api
def loginResponse():
    url = "http://api.amber360.com/api/user/login"
    params = {'name':'Adam123', 'pass':'Muhideen@1adam', 'appId':'6', 'language':'en-us', 'loginType':0}
    response = requests.post(url, data=json.dumps(params), headers=headers)

#queries api for device list
def deviceListResponse(userID, accessToken):
    url = "http://api.amber360.com/api/device/listdevice"
    params = {'id':userID, 'type':0, 'pageNo':1, 'pageCount':100, 'loginType':0, 'mapType':'google', 'lastTime':'2017-01-09T12:01:05.9776787 08:00', 'token':accessToken, 'language':'en-us', 'appId':'6'}
    response = requests.post(url, data=json.dumps(params), headers=headers)
    return json.loads(response.text)


#queries api for tracking details of the device id given
def trackingResponse(deviceID, accessToken):
    url = "http://api.amber360.com/api/location/tracking"
    params = {'deviceId':deviceID, 'mapType':'google', 'token':accessToken, 'language':'en-us', 'appId':'6'}
    response = requests.post(url, data=json.dumps(params), headers=headers)
    return json.loads(response.text)
