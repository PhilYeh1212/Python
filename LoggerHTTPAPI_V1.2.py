import os
import csv
import time
import requests

lastTI = 0
URL1 = 'https://pmsdata.formosasolar.com.tw/realtime/extel'
URL2 = 'https://pmsdata.formosasolar.com.tw/realtime/extel/alarm'
RAWline = ''
ALMline = ''
try:
    inTI = time.time()
    today = time.strftime('%y_%m_%d', time.localtime())
    if (inTI - lastTI > 300):
        lastTI = time.time()

        datafiles = os.listdir(r'C:\HTTPUpload')
        datafileslen = len(datafiles)
        for datafileslen in datafiles:
            if os.path.isfile('%s_%s.%s' % (r'C:\HTTPpy\temp\temp_raw', datafileslen, 'txt')):
                with open('%s_%s.%s' % (r'C:\HTTPpy\temp\temp_raw', datafileslen, 'txt'), 'r') as filesRAW:
                    RAWdata = filesRAW.readlines()
                    lenRAW = len(RAWdata)
                    for lenRAW in RAWdata:
                        RAWline = RAWline + lenRAW
                with open('%s_%s.%s' % (r'C:\HTTPpy\temp\temp_alm', datafileslen, 'txt'), 'r') as filesALM:
                    ALMdata = filesALM.readlines()
                    lenALM = len(ALMdata)
                    for lenALM in ALMdata:
                        ALMline = ALMline + lenALM
                RAWpaths = os.listdir('%s\%s' % (r'C:\HTTPUpload', datafileslen))
                with open('%s\%s\%s' % (r'C:\HTTPUpload', datafileslen, RAWpaths[1]), 'r') as filesRAW:
                    RAWdata = filesRAW.readlines()
                    lenRAW = len(RAWdata)
                    for lenRAW in RAWdata:
                        RAWline = RAWline + lenRAW
                with open('%s\%s\%s' % (r'C:\HTTPUpload', datafileslen, RAWpaths[0]), 'r') as filesALM:
                    ALMdata = filesALM.readlines()
                    lenALM = len(ALMdata)
                    for lenALM in ALMdata:
                        ALMline = ALMline + lenALM
                try:
                    print(datafileslen)
                    timenow = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
                    uploadlist1 = requests.post(URL1, RAWline)
                    print(timenow, URL1, uploadlist1)
                    uploadlist2 = requests.post(URL2, ALMline)
                    print(timenow, URL2, uploadlist2)
                    RAWline = ''
                    ALMline = ''
                    os.remove('%s_%s.%s' % (r'C:\HTTPpy\temp\temp_raw', datafileslen, 'txt'))
                    os.remove('%s_%s.%s' % (r'C:\HTTPpy\temp\temp_alm', datafileslen, 'txt'))
                except Exception as e:
                    with open('%s_%s.%s' % (r'C:\HTTPpy\temp\temp_raw', datafileslen, 'txt'), 'w') as RAWwrite:
                        RAWwrite.write(RAWline)
                    RAWline = ''
                    with open('%s_%s.%s' % (r'C:\HTTPpy\temp\temp_alm', datafileslen, 'txt'), 'w') as ALMwrite:
                        ALMwrite.write(ALMline)
                    ALMline = ''

            else:
                RAWpaths = os.listdir('%s\%s' % (r'C:\HTTPUpload', datafileslen))
                with open('%s\%s\%s' % (r'C:\HTTPUpload', datafileslen, RAWpaths[1]), 'r') as filesRAW:
                    RAWdata = filesRAW.readlines()
                    lenRAW = len(RAWdata)
                    for lenRAW in RAWdata:
                        RAWline = RAWline + lenRAW
                with open('%s\%s\%s' % (r'C:\HTTPUpload', datafileslen, RAWpaths[0]), 'r') as filesALM:
                    ALMdata = filesALM.readlines()
                    lenALM = len(ALMdata)
                    for lenALM in ALMdata:
                        ALMline = ALMline + lenALM
                try:
                    print(datafileslen)
                    timenow = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
                    uploadlist1 = requests.post(URL1, RAWline)
                    print(timenow, URL1, uploadlist1)
                    uploadlist2 = requests.post(URL2, ALMline)
                    print(timenow, URL2, uploadlist2)
                    RAWline = ''
                    ALMline = ''
                except Exception as e:
                    with open('%s_%s.%s' % (r'C:\HTTPpy\temp\temp_raw', datafileslen, 'txt'), 'w') as RAWwrite:
                        RAWwrite.write(RAWline)
                    RAWline = ''
                    with open('%s_%s.%s' % (r'C:\HTTPpy\temp\temp_alm', datafileslen, 'txt'), 'w') as ALMwrite:
                        ALMwrite.write(ALMline)
                    ALMline = ''
except Exception as e:
    print(e)