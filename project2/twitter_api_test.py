import tweepy



client = tweepy.Client(bearer_token=bearer_token, consumer_key=consumer_key, consumer_secret=consumer_secret,
                       access_token=access_token, access_token_secret=access_token_secret)


def search(m):
    response = client.search_recent_tweets(m, max_results=10)
    tweets = response.data
    for tweet in tweets:
        print('The id is :' + str(tweet.id))
        print('The text is :' + tweet.text)


def create(m):
    response = client.create_tweet(text=m)


def follow_usr(m):
    client.follow_user(m)
