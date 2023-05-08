import time
import shutil
import requests
import mysql.connector

#jWldN1JVeqTJEFDKDwKN4wUegiBlI6LXmBNGQXqCayi --extel內部群
token = '4cwTgoUM0Npnnob1D0aUHCYWxN6huiqVF9poI0G1Efe' #extel工程部

def lineNotifyMessage(token, msg):
    headers = {
        "Authorization": "Bearer " + token,
        "Content-Type": "application/x-www-form-urlencoded"
    }
    payload = {'message': msg}
    r = requests.post("https://notify-api.line.me/api/notify", headers=headers, params=payload)
    return r.status_code

with open(r'C:\DDS Data\Logger.ini', 'r') as f:
    sitecode = f.readline().replace('\n', '').replace('Side_ID:', '')

total, used, free = shutil.disk_usage("/")

free = (free // (2 ** 30))

if free < 5:
    message = sitecode + '容量不足5G'
    lineNotifyMessage(token, message)
