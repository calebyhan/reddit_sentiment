from decouple import config
import praw
import csv
from textblob import TextBlob
import matplotlib.pyplot as plt
import datetime

ID = config("ID")
SECRET = config("SECRET")


def get_data():
    keyword = input("KEYWORD TO SEARCH: ")

    reddit = praw.Reddit(
        client_id=ID,
        client_secret=SECRET,
        user_agent="Development stage",
    )

    with open("data.csv", "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["Author", "Subreddit", "Date", "Title", "Text"])
        writer.writeheader()
        for submission in reddit.subreddit("all").search(query=keyword, sort="new", time_filter="month"):
            row = {'Author': submission.author.name,
                    "Subreddit": submission.subreddit.display_name,
                    "Date": str(submission.created_utc),
                    "Title": submission.title,
                    "Text": submission.selftext
            }
            writer.writerow(row)


def compile_data():
    with open("sentiment.csv", "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["Author", "Subreddit", "Date", "Title", "Text", "Polarity"])
        writer.writeheader()
        with open("data.csv", "r", encoding="utf-8", newline="") as f1:
            reader = csv.DictReader(f1, delimiter=',')
            for row in reader:
                newRow = {'Author': row["Author"],
                        "Subreddit": row["Subreddit"],
                        "Date": row["Date"],
                        "Title": row["Title"],
                        "Text": row["Text"],
                        "Polarity": TextBlob(row["Title"] + row["Text"]).sentiment.polarity
                }
                writer.writerow(newRow)


def analyze_data():
    with open("sentiment.csv", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f, delimiter=',')
        polarity = []
        dates = []
        for row in reader:
            polarity.append(row["Polarity"])
            dates.append(datetime.datetime.fromtimestamp(float(row["Date"])))
        plt.plot(dates, polarity)
        plt.xlabel('Time')
        plt.ylabel('Polarity')
        plt.show()


analyze_data()