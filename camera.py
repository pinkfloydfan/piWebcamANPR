import time 
import requests
import os

from time import sleep
from subprocess import call

from google.cloud import storage


os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = os.getcwd()+"/APIKeys.json"


url = "https://alpr-pdc653u2vq-ew.a.run.app/anpr"
storage_client = storage.Client()
imagePath = os.getcwd()+"/newImage.jpg"

while True:
    call(["fswebcam", "-r 1280x720", "newImage.jpg"]) #takes image w/USB webcam
    with open(imagePath, "rb") as image: #uploads this to api endpoint as a POST request
        payload = {'file': image}
        result = requests.post(url, files = payload)
        print(result.text)
	#upload to GCP bucket
        storage_client = storage.Client()
        bucket = storage_client.get_bucket('carvision-images')
        blob = bucket.blob('newImage')
        blob.upload_from_filename(imagePath)
        sleep(3)


