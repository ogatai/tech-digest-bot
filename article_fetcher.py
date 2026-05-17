from newspaper import Article


def fetch_article_text(url):
    try:
        article = Article(url)
        article.download()
        article.parse()

        text = article.text
        return text[:3000]   # 長すぎるのでまず3000文字まで

    except Exception as e:
        print("本文取得失敗:", e)
        return ""