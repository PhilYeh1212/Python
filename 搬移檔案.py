import os
import time
import shutil
import paramiko

try:
    files = os.listdir(r'C:\_Phil\02_Project\_FS100\巡檢報告\Photo')
    for x in files:
        print(x)
        files1 = os.listdir('%s\%s' % (r'C:\_Phil\02_Project\_FS100\巡檢報告\Photo', x))
        print(files1)
        for y in files1:
            print(y)
            files2 = '%s\%s\%s' % (r'C:\_Phil\02_Project\_FS100\巡檢報告\Photo', x, y)
            try:
                destinationpath = r'C:\_Phil\02_Project\_FS100\巡檢報告\AllPhoto'
                shutil.move(files2, destinationpath)
            except Exception as e:
                print(e)
except Exception as e:
    print(e)
