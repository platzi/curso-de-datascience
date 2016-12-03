from tweepy import StreamListener


class FiniteStreamListener(StreamListener):
    
    def __init__(self, number_of_tweets):
        self.number_of_tweets = number_of_tweets
        self.tweets = []
        super(FiniteStreamListener, self).__init__()
        
    def on_status(self, status):
        if len(self.tweets) < self.number_of_tweets:
            self.tweets.append(status.text)
        else:
            return False
