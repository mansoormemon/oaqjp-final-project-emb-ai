import requests


def emotion_detector(text_to_analyse):
    EMPTY_RESULT = {
        "anger": None,
        "disgust": None,
        "fear": None,
        "joy": None,
        "sadness": None,
        "dominant_emotion": None
    }

    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url, json = myobj, headers=headers)
    if response.status_code == 400:
        return EMPTY_RESULT
    data = response.json()
    predictions, *_ = data['emotionPredictions']
    emotion_scores = predictions['emotion']
    dominant_emotion = max(emotion_scores, key=emotion_scores.get)
    result = {**emotion_scores, 'dominant_emotion': dominant_emotion }
    return result