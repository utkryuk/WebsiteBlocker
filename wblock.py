#website blocker

import time as t
from datetime import datetime as dt
hostPath = r"C:\Windows\System32\drivers\etc\HOSTS"
reDirect = "127.0.0.1"
blockList = ["www.facebook.com","www.instagram.com","www.youtube.com"]
codingTimeStarts = dt(dt.now().year,dt.now().month,dt.now().day,10)
codingTimeEnds= dt(dt.now().year,dt.now().month,dt.now().day,23)
funTimeStarts = dt(dt.now().year,dt.now().month,dt.now().day,0)
funTimeEnds = dt(dt.now().year,dt.now().month,dt.now().day,9)
while True:
    if codingTimeStarts<dt.now()<codingTimeEnds:
        with open(hostPath+'\hosts','r+') as file:
            content = file.read()
            for restrictedWebsite in blockList:
                if restrictedWebsite in content:
                    pass
                else:
                    file.write('\n'+reDirect+' '+restrictedWebsite)
    else:
        with open(hostPath,'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(restrictedWebsite in line for restrictedWebsite in blockList):
                    file.write(line)
                file.truncate()
    t.sleep(10)