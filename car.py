"""
detects the car in the image and returns the make and model of the car
use openai api to detect the car make and model
"""

import os
import base64
import cv2
import json
import requests

def get_car_make_model(image):
    """
    detects the car in the image and returns the make and model of the car
    use openai api to detect the car make and model
    """
    # get the image
    img = cv2.imread(image)
    # resize the image
    img = cv2.resize(img, (224, 224))
    # convert the image to base64
    img = base64.b64encode(cv2.imencode('.jpg', img)[1]).decode()
    # get the api key
    api_key = os.environ.get('OPENAI_API_KEY')
    # get the api url
    api_url = 'https://api.openai.com/v1/classifications'
    # get the headers
    headers = { 'Authorization': 'Bearer ' + api_key, 'Content-Type': 'application/json' } 
    # get the data
    data = { 'examples': [ { 'image': { 'base64': img } } ], 'model': 'curie:ft-car-make-model-1' }
    # get the response
    response = requests.post(api_url, headers=headers, data=json.dumps(data))
    # get the response
    response = response.json()
    # get the car make and model
    car_make_model = response['label']
    # return the car make and model
    return car_make_model

if __name__ == '__main__':
    # get the car make and model
    car_make_model = get_car_make_model('car.jpg')
    # print the car make and model
    print(car_make_model)