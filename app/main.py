import datetime
from typing import Optional, List
from fastapi import FastAPI
from pydantic import BaseModel
from faker import Faker
from textblob import TextBlob

app = FastAPI()
class Tweet(BaseModel):
    user: str
    date_created: datetime.date
    num_likes: int
    source: str
    content: str
    sentiment: str
    polarity: float


fake = Faker()

def get_sentiment(text: str) -> str:
    """
    Helper function to determine sentiment category based on polarity score.
    """
    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity

    if polarity > 0:
        return polarity,"positive"
    elif polarity == 0:
        return polarity,"neutral"
    else:
        return polarity,"negative"

@app.get("/tweets")
def get_tweets(
    #query: str,
    start_date: Optional[datetime.date] = None,
    end_date: Optional[datetime.date] = None,
) -> List[Tweet]:
    attributes_container = []

    # In this example, we'll generate fake data regardless of the date range
    if start_date and end_date:
        # Use start_date and end_date to filter the tweets
        tweet_date = fake.date_between_dates(date_start=datetime.datetime.strptime(start_date,'%Y-%m-%d'), date_end=datetime.datetime.strptime(end_date,'%Y-%m-%d'))
    else:
        tweet_date = fake.date_between(start_date="-1y", end_date="today")

    tweet_list=[]
    for _ in range(10):
        tweet_content=fake.text(max_nb_chars=280)
        polarity,sentiment = get_sentiment(tweet_content)

        tweet = Tweet(
            user=fake.user_name(),
            date_created=tweet_date,
            num_likes=fake.random_int(min=0, max=100),
            source=fake.random_element(elements=("Twitter Web App", "TweetDeck", "Mobile App")),
            content=tweet_content,
            sentiment=sentiment,
            polarity=polarity,
        )
        tweet_list.append(tweet)

    return tweet_list
