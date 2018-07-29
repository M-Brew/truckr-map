#!/usr/bin/python

import truckr
import MySQLdb

#get user id and access token
userID = truckr.loginResponse().get('Item').get('UserId')
accessToken = truckr.loginResponse().get('AccessToken')

#get device id
deviceID = truckr.deviceListResponse(userID, accessToken).get('Items')[8].get('Id')

#get lat and lng
latitude = truckr.trackingResponse(deviceID, accessToken).get('Item').get('Latitude')
longitude = truckr.trackingResponse(deviceID, accessToken).get('Item').get('Longitude')

#inserting lat and lng into database
conn = MySQLdb.connect('localhost', 'root', 'brew', 'truckr')
cursor = conn.cursor()
query = "insert into coordinates(latitude, longitude) values ('%f', '%f')" % (latitude, longitude)
try:
        cursor.execute(query)
        conn.commit()
except:
        conn.rollback()

conn.close()

