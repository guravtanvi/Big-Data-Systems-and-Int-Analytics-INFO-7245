try:
    from flask import app,Flask, request, render_template, jsonify
    from flask_restful import Resource, Api, reqparse
    import datetime
    import json
    import os
    import sys
    import ssl
    import os
    import tensorflow_hub as hub
    import tensorflow as tf
    import warnings
    import compute_inference
    from tabulate import tabulate
    import flat_table
    from pandas import json_normalize
except Exception as e:
    print("Error : {} ".format(e))


app = Flask(__name__)
api = Api(app)

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context



def label2str(x):
    if x == 0:
        return ["negative"]
    else:
        return ["positive"]


def predict_online(data):

    print("Predicting sentiment..")

    path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'models', 'sentiment_tf.keras'))
    print("Found model at: "+path)

    model = tf.keras.models.load_model(path,custom_objects={'KerasLayer': hub.KerasLayer})
    pred = [label2str(model.predict_classes([input])) for input in data]

    return {"input": data, "pred": pred}


@app.route('/')
def my_form():
    return render_template('home.html')

@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text']
    file_name=text+'.txt'
    path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'call_transcripts', file_name))
    sentences = compute_inference.annotate(path)
    json_data = predict_online(sentences["data"])
    return json_data

if __name__ == '__main__':
    app.run(debug=True)