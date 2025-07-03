from unittest import TestCase

from EmotionDetection import emotion_detector


class TestEmotionDetector(TestCase):

    def test_returns_joy(self):
        dominant_emotion = emotion_detector("I am glad this happened").get(
            "dominant_emotion"
        )
        self.assertEqual(dominant_emotion, "joy")

    def test_returns_anger(self):
        dominant_emotion = emotion_detector("I am really mad about this").get(
            "dominant_emotion"
        )
        self.assertEqual(dominant_emotion, "anger")

    def test_returns_disgust(self):
        dominant_emotion = emotion_detector(
            "I feel disgusted just hearing about this"
        ).get("dominant_emotion")
        self.assertEqual(dominant_emotion, "disgust")

    def test_returns_sadness(self):
        dominant_emotion = emotion_detector("I am so sad about this").get(
            "dominant_emotion"
        )
        self.assertEqual(dominant_emotion, "sadness")

    def test_returns_fear(self):
        dominant_emotion = emotion_detector(
            "I am really afraid that this will happen"
        ).get("dominant_emotion")
        self.assertEqual(dominant_emotion, "fear")
