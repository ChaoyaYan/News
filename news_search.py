import requests
import datetime
from newsplease import NewsPlease
from http.client import IncompleteRead,RemoteDisconnected
from newspaper.article import ArticleException
from urllib.error import HTTPError
from sentiment import sentiment
from plot import plot
class news_search(object):
    def __init__(self, number = 20, key = "9646f106e49143afa034e4d770ce5779", key_word = "WeWork", country = "CN"):
        """
        :param country: the news source, China : "CN", USA : "US"
        :param number: number of news to search
        :param key_word: The topic of news you want to read, initial topic is WeWork
        :param key: Api_key for Microsoft news Api
        """
        self.country = country
        self.number = number
        self.key_word = key_word
        self.key = key

        self.sentiment = []



    def get_url(self):
        headers = {"Ocp-Apim-Subscription-Key": self.key}
        params = {"q": self.key_word, "textDecorations": True, "textFormat": "HTML", "cc": self.country, "count": self.number * 10}
        response = requests.get("https://api.cognitive.microsoft.com/bing/v7.0/news/search", headers=headers, params=params)
        response.raise_for_status()
        search_results = response.json()
        url = [u["url"] for u in search_results["value"]]
        return url





    def search_url(self):
        fileName = "news_" + str(datetime.datetime.now()) + ".txt"

        f = open(fileName, 'a+', encoding='utf-8')

        url = self.get_url()
        #print (url)
        n = 0


        for u in url:
            try:
                article = NewsPlease.from_url(u)
            except IncompleteRead:
                continue
            except RemoteDisconnected:
                continue
            except ArticleException:
                continue
            except HTTPError:
                continue
            #print(type(article.title), type(article.date_publish), type(article.text))

            if article.text is None or article.title  is None:
                continue
            else:
                n = n + 1

                message = article.title
                s = sentiment()
                score = s.calculate_score(str(message))
                print(str(n - 1) + ": " + u)
                self.sentiment.append(score)
                #s.calculate_score(str(article.text))

                context = str(n) + ':'  + article.title + '\n' + '\n' + str(
                   article.date_publish) + '\n' +'\n' + article.text + '\n' + '\n' + '\n'
                f.write(context)
               #print(context)
                if n == self.number:
                    break

        print("done")

    def graph(self):
        p = plot(self.sentiment)
        p.graph()



if __name__ == '__main__':
   serach = news_search(country = "US", number = 10, key_word = "WeWork")
   serach.search_url()
   serach.graph()