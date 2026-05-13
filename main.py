import feedparser
import yaml


def load_feeds():
    with open("config/feeds.yaml", "r", encoding="utf-8") as f:
        config = yaml.safe_load(f)
    return config["rss"]


def fetch_articles(feed):
    print()
    print(f"=== {feed['name']} ===")

    parsed = feedparser.parse(feed["url"])

    for entry in parsed.entries[:5]:
        print(f"- {entry.title}")


def main():
    feeds = load_feeds()

    for feed in feeds:
        fetch_articles(feed)


if __name__ == "__main__":
    main()