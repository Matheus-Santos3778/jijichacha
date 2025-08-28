import tweepy
import pandas as pd

with open('access/access', 'r') as file:
    bearer_token = file.readlines()[0].strip()

client = tweepy.Client(bearer_token=bearer_token)

query = "#Tarcisio -is:retweet lang:pt"  #Tópico, sem retweets, apenas português
tweets = client.search_recent_tweets(query=query, max_results=100, tweet_fields=['created_at', 'public_metrics', 'author_id'])

dados = []
for tweet in tweets.data:
    dados.append({
        "id": tweet.id,
        "texto": tweet.text,
        "autor_id": tweet.author_id,
        "data": tweet.created_at,
        "curtidas": tweet.public_metrics['like_count'],
        "retweets": tweet.public_metrics['retweet_count'],
        "replies": tweet.public_metrics['reply_count'],
        "quotes": tweet.public_metrics['quote_count']
    })

df = pd.DataFrame(dados)

df.to_csv("data/tweets_python.csv", index=False)
print("Arquivo CSV gerado com sucesso!")