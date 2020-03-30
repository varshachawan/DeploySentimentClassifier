import tensorflow as tf
from flask import Flask, jsonify, request, make_response
from healthcheck import HealthCheck,EnvironmentDump

import tensorflow_datasets as tfds
# import google.cloud.logging as glog
#
# client = glog.Client()
# client.setup_logging()


import logging

model = tf.keras.models.load_model('sentiment_analysis.hdf5')
logging.info("model loaded")
text_encoder = tfds.features.text.TokenTextEncoder.load_from_file('sa_encoder.vocab')

app = Flask(__name__)
health = HealthCheck()
envdump = EnvironmentDump()
app.add_url_rule("/health", "healthcheck", view_func=lambda: health.run())
app.add_url_rule("/environment", "environment", view_func=lambda: envdump.run())

def application_data():
    return {"maintainer": "Varsha Chawan",
            "git_repo": "https://github.com/varsharanichawan"}

envdump.add_section("application", application_data)

# add your own check function to the healthcheck
def model_available():
    if model and text_encoder:
        return True, "Model and Vocab ok"


health.add_check(model_available)


def pad_to_size(vec, size):
    zeros = [0] * (size - len(vec))
    vec.extend(zeros)
    return vec


def predict_fn(pred_text):
    encoded_pred_text = text_encoder.encode(pred_text)
    print(encoded_pred_text)
    encoded_pred_text = pad_to_size(encoded_pred_text, 32)
    encoded_pred_text = tf.cast(encoded_pred_text, tf.float32)
    predictions = model.predict(tf.expand_dims(encoded_pred_text, 0))
    return predictions.tolist()


@app.route('/predict', methods=['POST'])
def predict_sentiment():
    text = request.get_json()['text']
    print(text)
    predict = predict_fn(text)
    sentiment = 'positive' if float(''.join(map(str, predict[0]))) > 0 else 'Negative'
    return jsonify({'predictions': predict, 'sentiment': sentiment})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
