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
    
    def test_very_long_text(self):
        long_text = "I am very happy and excited about this wonderful opportunity. " * 50
        result = emotion_detector(long_text)
        self.assertIn('anger', result)
        self.assertIn('disgust', result)
        self.assertIn('fear', result)
        self.assertIn('joy', result)
        self.assertIn('sadness', result)
        self.assertIn('dominant_emotion', result)
        if result['dominant_emotion'] is not None:
            self.assertIn(result['dominant_emotion'], ['anger', 'disgust', 'fear', 'joy', 'sadness'])
    
    def test_mixed_alphanumeric(self):
        result = emotion_detector("I feel happy123 and sad456 at the same time")
        self.assertIn('dominant_emotion', result)
        if result['dominant_emotion'] is not None:
            self.assertIn(result['dominant_emotion'], ['anger', 'disgust', 'fear', 'joy', 'sadness'])
    
    def test_mixed_emotions(self):
        result = emotion_detector("I am happy but also sad and a bit angry about this situation")
        self.assertIn('anger', result)
        self.assertIn('disgust', result)
        self.assertIn('fear', result)
        self.assertIn('joy', result)
        self.assertIn('sadness', result)
        self.assertIn('dominant_emotion', result)
        if result['dominant_emotion'] is not None:
            self.assertIsInstance(result['anger'], (int, float))
            self.assertIsInstance(result['joy'], (int, float))
            self.assertIsInstance(result['sadness'], (int, float))
    
    def test_neutral_ambiguous_statement(self):
        result = emotion_detector("The weather is nice today")
        if result['dominant_emotion'] is not None:
            self.assertIn(result['dominant_emotion'], ['joy', 'sadness', 'anger', 'disgust', 'fear'])
            emotion_values = [result['anger'], result['disgust'], result['fear'], result['joy'], result['sadness']]
            self.assertTrue(all(isinstance(v, (int, float)) for v in emotion_values))
            max_score = max(emotion_values)
            self.assertLess(max_score - min(emotion_values), 0.5)
    

    
    def test_repeated_text_pattern(self):
        result = emotion_detector("sad sad sad sad sad")
        self.assertEqual(result['dominant_emotion'], 'sadness')
        self.assertIsInstance(result['sadness'], (int, float))
        self.assertGreater(result['sadness'], result['anger'])
        self.assertGreater(result['sadness'], result['joy'])
    
    def test_multiple_sentences_different_emotions(self):
        result = emotion_detector("I am so happy today. But yesterday I was sad. Tomorrow I might be angry.")
        self.assertIn('dominant_emotion', result)
        if result['dominant_emotion'] is not None:
            self.assertIn(result['dominant_emotion'], ['anger', 'disgust', 'fear', 'joy', 'sadness'])
    
    def test_case_sensitivity(self):
        result_lower = emotion_detector("i am happy")
        result_upper = emotion_detector("I AM HAPPY")
        result_mixed = emotion_detector("I aM HaPpY")
        self.assertEqual(result_lower['dominant_emotion'], result_upper['dominant_emotion'])
        self.assertEqual(result_lower['dominant_emotion'], result_mixed['dominant_emotion'])