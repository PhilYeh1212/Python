import time
import requests
import mysql.connector

#jWldN1JVeqTJEFDKDwKN4wUegiBlI6LXmBNGQXqCayi --extel內部群
token = '1q0OXJ1DRrrniDXIrGGVnUIkp4MTY4dB195DhbXMpsf'

def lineNotifyMessage(token, msg):
    headers = {
        "Authorization": "Bearer " + token,
        "Content-Type": "application/x-www-form-urlencoded"
    }
    payload = {'message': msg}
    r = requests.post("https://notify-api.line.me/api/notify", headers=headers, params=payload)
    return r.status_code

#mydb = mysql.connector.connect(host="localhost",user="root",passwd="Oerlikon;1234",)
#mydb = mysql.connector.connect(host="35.236.181.75", user="Phil", password="Qwe751212", port=3306)
data = []
mydb = mysql.connector.connect(host="localhost", user="root", password="Oerlikon;1234", port=3306, database="FS_Logger_Global")
Today = time.strftime('%Y/%m/%d', time.localtime())
StartTime = '10:00:00'
EndTime = '10:00:00'
NightPower = []
sitenum = []
NightPowerError =[]
k = 0
#print(Today)

sitecode = []

with open(r'C:\_Phil\FS100.txt', 'r') as f:
    for i in range(0,100):
        sitecode.append(f.readline().replace('\n', ''))
        #sql1 = "%s'%s'" % ('SELECT Extel_code FROM FS_Logger_Global.Site_list where DAQ_DAte != ', Today)
        sql1 = "%s%s.%s %s'%s'%s'%s'%s'%s'" % ('SELECT INVID FROM FSLG_', sitecode[i], 'T2_inv where INVXX08 <= 0', 'and DAQ_DAte =', Today,' and DAQ_Time BETWEEN ', StartTime, ' AND ', EndTime)
        sql2 = "SELECT Site_code, Extel_code FROM FS_Logger_Global.Site_list"
        #sql1 = "SELECT Extel_code FROM FS_Logger_Global.Site_list where Instant_Power = 0"
        print(sql1)
        cursor1 = mydb.cursor()
        cursor1.execute(sql1)
        Online = cursor1.fetchall()
        cursor2 = mydb.cursor()
        cursor2.execute(sql2)
        FS100 = cursor2.fetchall()
        if not Online:
            pass
        else:
            data, Invcode = sitecode[i], Online
            Invcode = ' '.join(str(i) for i in Invcode)
            Invcode = Invcode.replace('(', '').replace(',', '').replace(')', '')
            for q in range(len(FS100)):
                if (FS100[q][0]) == (data):
                    NightPower.append(FS100[q][1]+'_'+data + '_' + Invcode + '\n')
    num = len(NightPower)
    print(NightPower)
    if num <= 0:
        message = "Inverter發電量為零_全案場正常"
        lineNotifyMessage(token, message)
    if num > 0:
        message = ((('Inverter發電量為零案場' + str(num) + '場' + '\n'), sorted(NightPower)))
        #message = '%s\n%s:%s%s:%s\n%s:%s' % ('\n缺資料機台', 'Date', date1, 'ID', DAS1, 'Count', Count1)
        with open(r'C:\_Phil\Test.txt', 'w') as RAWwrite:
            RAWwrite.write(message)

        lineNotifyMessage(token, message)
