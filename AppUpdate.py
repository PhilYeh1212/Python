import os
import time
import shutil
import paramiko
import mysql.connector
from mysql.connector import Error
from ftplib import FTP

with open(r'C:\DDS Data\Logger.ini', 'r') as f:
    sitecode = f.readline()
    sitecode = sitecode.split(':')
    sitecode = sitecode[1].replace('\n', '')
    print(sitecode)


SQLdate = time.strftime('%Y/%m/%d')
#sqlread = "SELECT site_code, AppUpdate FROM FS_Logger_Global.Site_list where site_code = 'TW160004'"
sqlread = "%s'%s'" % ('SELECT site_code, AppUpdate FROM FS_Logger_Global.Site_list where site_code = ', sitecode)
sqlwrite = "%s'%s'" % ('UPDATE Site_list SET AppUpdate = 0 where site_code = ', sitecode)
#testSelect = 'SELECT * FROM vena_dds_global.machines limit 1;'
host = "35.189.175.5"
port = 22
username = 'playplus'
password = 'extel2019'


try:
    # 連接 MySQL/MariaDB 資料庫
    mydb = mysql.connector.connect(host="localhost", user="root", password="Oerlikon;1234", port=3306, database="FS_Logger_Global")

    if mydb.is_connected():
       db_Info = mydb.get_server_info()
       print("Connected to MySQL Server version ", db_Info)
       #查詢資料庫
       cursor = mydb.cursor()
       cursor.execute(sqlread)     #執行SQL碼
       # 列出查詢的資料
       for (site_code, AppUpdate) in cursor:
           print("DasID: %s, DAS2_APP_update: %s" % (site_code, AppUpdate))

except Error as e:
       print('Error while connecting to MySQL',e)

print(site_code,AppUpdate)

# myresult = cursor.fetchall()
# print(myresult)
try:
    if AppUpdate > 0:
        print('shutdwon application')
        command = 'taskkill /F /IM application.exe'
        os.system(command)
        print('backup old file')
        oldfile = r"C:\app\application.exe"
        date = '%s.%s' % (time.strftime('%Y%m%d%H%M%S'), 'exe')
        tobackupfile = (r"C:\app\AP_back\application_back_" + date)
        shutil.copyfile(oldfile, tobackupfile)
        print('Downloading a new application on FTP')
        transport = paramiko.Transport((host, port))
        transport.connect(username=username, password=password)
        sftp = paramiko.SFTPClient.from_transport(transport)
        sftp.get("/home/playplus/www/estpower/public/uploads/DDS_Pic/App_with_Normal/Application.exe", r"C:\app\Application.exe")
        print('Download Done')
        print('Running a new application')
        os.system(r"start C:\app\Application.exe")
        print('Update SQL value')
        cursor.execute(sqlwrite)
        mydb.commit()
    else:
        print('no need to update application')
        cursor.execute(sqlwrite)
        mydb.commit()
except Exception as e:
    print(e)
