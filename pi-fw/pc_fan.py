from gpiozero import PWMLED
from time import sleep
import json, requests

fan = PWMLED(18)


while True:
    try:
        r = requests.get('http://54.185.132.179/get_speed')
        r_dict = r.json()
        print('current speed: ' + json.dumps(r_dict['speed']))
        fan.value = float(json.dumps(r_dict['speed']))/100
        sleep(5)
    except:
        pass
