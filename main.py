from decouple import config
import praw
import csv


def get_data():
    keyword = input("KEYWORD TO SEARCH: ")
    ID = config("ID")
    SECRET = config("SECRET")

    reddit = praw.Reddit(
        client_id=ID,
        client_secret=SECRET,
        user_agent="Development stage",
    )

    with open("data.csv", "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["Author", "Subreddit", "Date", "Title", "Text"])
        writer.writeheader()
        for submission in reddit.subreddit("all").search(query=keyword, sort="new", time_filter="month"):
            row = {'Author': submission.author.name, "Subreddit": submission.subreddit.display_name, "Date": str(submission.created_utc), "Title": submission.title, "Text": submission.selftext}
            writer.writerow(row)

get_data()