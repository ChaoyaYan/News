import numpy as np
import matplotlib.pyplot as plt

class plot(object):
    def __init__(self,  sentiment):
        self.sentiment = sentiment

    def graph(self):
        N = len(self.sentiment)
        neg = []
        pos = []
        index = []
        for i in range(N):
            index.append(i + 1)
            score = 0.5
            if self.sentiment[i] != 0 :
                score = (1 - self.sentiment[i])/2
            neg.append(score)
            pos.append(1 - score)

        ind = np.arange(N)  # the x locations for the groups
        width = 0.35
        p1 = plt.bar(ind, pos, width)
        p2 = plt.bar(ind, neg, width,
                     bottom=pos)

        plt.ylabel('Scores')
        plt.title('Sentiment score')
        plt.xticks(np.arange(0, N, 1))
        plt.yticks(np.arange(0, 1, 0.1))
        plt.legend((p1[0], p2[0]), ('Positive', 'Negative'))

        plt.show()







