import time
from datetime import datetime as dt

#hosts_path = r'C:\Users\Ezone\Documents\hosts'
hosts_path = r'C:\Windows\System32\drivers\etc\HOSTS'
redirect = '127.0.0.1'
block_list = ['facebook.com', 'instagram.com','www.facebook.com','www.instagram.com']
working_hours = {
    'start': dt(dt.now().year, dt.now().month, dt.now().day, 9),
    'stop': dt(dt.now().year, dt.now().month, dt.now().day, 17)
}

while True:
  if working_hours['start'] < dt.now() < working_hours['stop']:
    with open(hosts_path, 'r+') as file:
      content = file.read()
      for website in block_list:
        if website in content:
          pass
        else:
          file.write(redirect + " " + website + "\n")
  else:
    with open(hosts_path, 'r+') as file:
      content = file.readlines()
      file.seek(0)
      for line in content:
        if not any(website in line for website in block_list):
          file.write(line)
      file.truncate()
  time.sleep(5)
  
