from flask import Flask, render_template, request

from EmotionDetection import emotion_detector

app = Flask("Emotions")


@app.route("/emotionDetector")
def analyze_emotion():
    text_to_analyze = request.args.get("textToAnalyze")
    result = emotion_detector(text_to_analyze)
    return f"""For the given statement, the system response is 'anger': {result['anger']},
    disgust': {result['disgust']}, 'fear': {result['fear']}, 'joy': {result['joy']},
    'sadness': {result['sadness']}. The dominant emotion is {result['dominant_emotion']}."""


@app.route("/")
def home():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
