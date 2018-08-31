
from nltk.sentiment.vader import SentimentIntensityAnalyzer




class sentiment(object):
    def __init__(self):
        pass

    def calculate_score(self, text):
        sid = SentimentIntensityAnalyzer()
        scores = sid.polarity_scores(text)

        for key in sorted(scores):
            print('{0}: {1}, '.format(key, scores[key]), end='')

        return scores["compound"]