import unittest
from EmotionDetection import emotion_detector

class TestEmotionDetector(unittest.TestCase):
    
    def test_joy(self):
        result = emotion_detector("I am glad this happened")
        self.assertEqual(result['dominant_emotion'], 'joy')
    
    def test_anger(self):
        result = emotion_detector("I am really mad about this")
        self.assertEqual(result['dominant_emotion'], 'anger')
    
    def test_disgust(self):
        result = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(result['dominant_emotion'], 'disgust')
    
    def test_sadness(self):
        result = emotion_detector("I am so sad about this")
        self.assertEqual(result['dominant_emotion'], 'sadness')
    
    def test_fear(self):
        result = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(result['dominant_emotion'], 'fear')
    
    def test_blank_input(self):
        result = emotion_detector("")
        self.assertIsNone(result['dominant_emotion'])
        self.assertIsNone(result['anger'])
        self.assertIsNone(result['disgust'])
        self.assertIsNone(result['fear'])
        self.assertIsNone(result['joy'])
        self.assertIsNone(result['sadness'])
    
    def test_whitespace_input(self):
        result = emotion_detector("   ")
        self.assertIsNone(result['dominant_emotion'])
    
    def test_response_structure(self):
        result = emotion_detector("I am glad this happened")
        self.assertIn('anger', result)
        self.assertIn('disgust', result)
        self.assertIn('fear', result)
        self.assertIn('joy', result)
        self.assertIn('sadness', result)
        self.assertIn('dominant_emotion', result)
        self.assertIsInstance(result['anger'], (int, float, type(None)))
        self.assertIsInstance(result['disgust'], (int, float, type(None)))
        self.assertIsInstance(result['fear'], (int, float, type(None)))
        self.assertIsInstance(result['joy'], (int, float, type(None)))
        self.assertIsInstance(result['sadness'], (int, float, type(None)))