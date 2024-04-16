"""
Flask application for emotion detection.

This application provides routes for emotion detection and rendering the main
application page.

Author: Dianze Liu
Date: April 15, 2024
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

#Initiate the flask app
app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emo_detector():
    ''' This code receives the text from the HTML interface and
        runs emotion detector over it using emotion_detector()
        function. The output returned shows the emotions score and dominant emotion.
    '''
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)

    anger = response.get('anger', None)
    disgust = response.get('disgust', None)
    fear = response.get('fear', None)
    joy = response.get('joy', None)
    sadness = response.get('sadness', None)
    dominant_emotion = response.get('dominant_emotion', None)

    if dominant_emotion is None:
        return "Invalid input ! Try again."

    return f"For the given statement, the system response is " \
       f"'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, " \
       f"'joy': {joy}, and 'sadness': {sadness}.\nThe dominant emotion is {dominant_emotion}."

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')

if __name__ == "__main__":
    # ''' This functions executes the flask app and deploys it on localhost:5000 '''
    app.run(host="0.0.0.0", port=5007)


if __name__ == "__main__":
    # ''' This functions executes the flask app and deploys it on localhost:5000 '''
    app.run(host="0.0.0.0", port=5000)
