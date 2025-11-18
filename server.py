"""
Flask web application for emotion detection"
"""

from flask import Flask, request, render_template

from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)


@app.route('/emotionDetector', methods=['GET'])
def route_emotion_detector():
    """
    Handles route '/emotionDetector.
    """
    text_to_analyse = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyse)
    if response["dominant_emotion"] is None:
        return "<b>Invalid text! Please try again!</b>"
    dominant_emotion = response.pop('dominant_emotion', 'unknown')
    formatted_response = "For the given statement, the system response is "
    for emotion, value in response.items():
        formatted_response += f"'{emotion}': {value}, "
    formatted_response = formatted_response.removesuffix(", ")
    formatted_response += f". The dominant emotion is <b>{dominant_emotion}.</b>"
    return formatted_response


@app.route("/")
def route_root():
    """
    Handles route for applications home page.
    """
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
