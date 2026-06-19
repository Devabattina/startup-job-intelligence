import feedparser

RSS_FEEDS = [
    "https://yourstory.com/feed",
    "https://inc42.com/feed"
]

KEYWORDS = [
    "raises",
    "raised",
    "funding",
    "seed",
    "series a",
    "series b",
    "investment",
    "investor",
    "backed"
]

def is_funding_news(title):
    title = title.lower()

    for keyword in KEYWORDS:
        if keyword in title:
            return True

    return False

def fetch_news():
    news = []

    for url in RSS_FEEDS:
        feed = feedparser.parse(url)

        for entry in feed.entries[:20]:

            if is_funding_news(entry.title):

                news.append({
                    "title": entry.title,
                    "link": entry.link
                })

    return news