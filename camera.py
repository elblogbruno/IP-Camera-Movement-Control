import requests
from time import sleep

class LEFT_CODE:
    code = 6
class STOP_CODE:
    code = 1
class RIGHT_CODE:
    code = 4
class UP_CODE:
    code = 0
class DOWN_CODE:
    code = 3

class CAMERA:
    def __init__(self,ip):
        self.ip = ip
        self.CONTROL_URL = "http://{0}/decoder_control.cgi?command=".format(self.ip)
        self.headers={
            "Host": "10.42.0.159",
            "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.5",
            "Accept-Encoding": "gzip, deflate",
            "Authorization": "Basic YWRtaW46bWFucmVzYTIx",
            "Connection": "keep-alive",
            "Referer": "http://10.42.0.159/serverpush.htm",
            "Upgrade-Insecure-Requests": "1"
        }
    def move_camera(self,code,time):
        print("Moving camera {0},{1} with this paremeters".format(code,time))
        r = requests.get(self.CONTROL_URL+str(code),headers=self.headers)
        print(r.status_code)
        sleep(time)
        stop = requests.get(self.CONTROL_URL+str(STOP_CODE.code),headers=self.headers)





