import json
from typing import Dict

import requests


BLANK_EMOTION_RESPONSE = {
    "anger": None,
    "fear": None,
    "joy": None,
    "sadness": None,
    "disgust": None,
    "dominant_emotion": None,
}


def dominant_emotion(emotions: Dict[str, float]) -> str:
    return max(emotions, key=emotions.get)


def emotion_detector(text_to_analyze: str) -> Dict[str, float | str]:
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    data = {"raw_document": {"text": text_to_analyze}}
    response = requests.post(url, headers=headers, json=data, timeout=10)
    if response.status_code == 400:
        return BLANK_EMOTION_RESPONSE
    response_json = json.loads(response.text)
    emotions = response_json["emotionPredictions"][0]["emotion"]
    emotions.update({"dominant_emotion": dominant_emotion(emotions)})
    return emotions
