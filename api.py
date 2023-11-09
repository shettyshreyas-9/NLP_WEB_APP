import pandas

import os
import paralleldots

class API:
    def __init__(self):
        paralleldots.set_api_key('VYHSNYk4wCdXfMIYEnNUc3sq6oNDI9Tyg2Db4HSEblE')

    # sentiment analysis
    def sentiment_analysis(self,text):
        response = paralleldots.sentiment(text)
        return response

    # named entity recognition
    def ner(self,text):
        response = paralleldots.ner(text)
        return response

    # Emotion Detection
    def emotion_detection(self,text):
        response = paralleldots.emotion(text)
        return response


