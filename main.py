import requests
import json
import validators
from flask import Flask, request, Response, render_template
from colors import color_choice


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
            # using teammates scraping service
            response = requests.post("https://wikiscraperproject.herokuapp.com/", data = url)
            cloud_text = response.text

        if len(cloud_text) > 1800:
            cloud_text = cloud_text[:1800]

        colors = color_choice(color)
        if colors == "custom":
            colors = request.get_json()["custom_colors"]

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