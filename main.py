import feedparser

RSS_URL = "https://techcrunch.com/feed/"


def fetch_articles():
    feed = feedparser.parse(RSS_URL)

    print("TechCrunch の最新記事")
    print("-" * 30)

    for entry in feed.entries[:10]:
        print(f"- {entry.title}")


if __name__ == "__main__":
    fetch_articles()