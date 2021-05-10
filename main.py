import requests
import json
import validators
from flask import Flask, request, Response, render_template


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('word_cloud.html')

@app.route('/cloud', methods=['POST'])
def cloud_post():
    if request.method == 'POST':
        cloud_text = request.get_json()["text"]
        try:
            img_size = int(request.get_json()["size"]) * 400
        except:
            img_size = 800
        try:
            color = int(request.get_json()["color"])
        except:
            color = 0
        
        if validators.url(cloud_text):
            url = {"url": cloud_text}
            response = requests.post("https://wikiscraperproject.herokuapp.com/", data = url)
            if len(response.text) > 2000:
                cloud_text = response.text[:2000]
            else:
                cloud_text = response.text
        # default
        if color == 0:
            colors = [
                '#375E97',
                '#FB6542',
                '#FFBB00',
                '#3F681C'
                ]

        #blues
        elif color == 1:
            colors = [
                '#6930C3',
                '#5390D9',
                '#48BFE3',
                '#64DFDF',
                '#80FFDB'
                ]

        # balanced
        elif color == 2:
            colors = [
                '#264653',
                '#2a9d8f',
                '#e9c46a',
                '#f4a261',
                '#e76f51'
                ]
        # palewave
        elif color == 3:
            colors = [
                '#d8e2dc',
                '#ffe5d9',
                '#ffcad4',
                '#f4acb7',
                '#9d8189'
                ]

        url = "https://textvis-word-cloud-v1.p.rapidapi.com/v1/textToCloud"
        payload = {
            'text': cloud_text,
            'scale': 1.0,
            'width': img_size,
            'height': img_size,
            'colors': colors,
            'font': 'Tahoma',
            'use_stopwords': True,
            'language': 'en',
            'uppercase': False
        }

        payload_json = json.dumps(payload)

        headers = {
            'content-type': "application/json",
            'x-rapidapi-key': "aa39aee572msh5a3a935f765dbe7p17bc12jsn54f4b3ae7734",
            'x-rapidapi-host': "textvis-word-cloud-v1.p.rapidapi.com"
            }

        resp = requests.request("POST", url, data=payload_json, headers=headers)

        return ({"image": resp.text}, 200)

if __name__ == '__main__':
    app.run(host='127.0.0.2', port=8080, debug=True)