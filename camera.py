import time
#import gcloud 
import requests
import os

from time import sleep
from subprocess import call

url = "https://alpr-pdc653u2vq-ew.a.run.app/anpr"

while True:
    call(["fswebcam", "-r 1280x720", "newImage.jpg"])
    with open(os.getcwd()+"/newImage.jpg", "rb") as image:
        payload = {'file': image}
        result = requests.post(url, files = payload)
        print(result.text)
        sleep(3)


