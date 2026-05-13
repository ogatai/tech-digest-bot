from export_html import export_html
from database import init_db, save_article
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

    if not parsed.entries:
        print("取得失敗 or 記事なし")
        return

    saved_count = 0

    for entry in parsed.entries[:5]:
        print(f"- {entry.title}")

        saved = save_article(
            title=entry.title,
            url=entry.link,
            source=feed["name"],
            published=getattr(entry, "published", "")
        )

        if saved:
            saved_count += 1

    print(f"保存件数: {saved_count}")

def main():
    init_db()

    feeds = load_feeds()

    for feed in feeds:
        fetch_articles(feed)

    export_html()


if __name__ == "__main__":
    main()