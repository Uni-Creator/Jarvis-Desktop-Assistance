import asyncio
from pygooglenews import GoogleNews
import regex as re


class GoogleApi:
    def __init__(self):
        self._api = self._get_api()
    def _get_api(self):
            return GoogleNews()
    def _get_news_for_word(self, word, top):
            text = self._api.search(word, when='1w')['entries']
            news = list(map(lambda x: self._clean(x['title']) + ' @ (' + x['published'] + ')', text))[:top]
            return news
    def _clean(self, text):
        clean_text = re.sub(r'http\S+', '', text, flags=re.MULTILINE)
        regrex_pattern = re.compile(pattern="["
           u"\U0001F600-\U0001F64F"  # emoticons
           u"\U0001F300-\U0001F5FF"  # symbols & pictographs
           u"\U0001F680-\U0001F6FF"  # transport & map symbols
           u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
           u"\U0001f17a-\U0001f97a"  # flags (iOS)
           "]+", flags=re.UNICODE)
        return regrex_pattern.sub(r'', clean_text)
    
    async def get_news_for_locations(self, target_locations, top=3):
        final = {}
        for location in target_locations:
            text = self._api.geo_headlines(location)['entries']
            news = list(map(lambda x: self._clean(x['title']) + ' @ (' + x['published'] + ')', text))[:top]
            final[location] = news
        return final
        
    async def get_news_for_words(self, target_words, top=3):
        text = {}
        for word in target_words:
            ts = self._get_news_for_word(word, top)
            text[word] = ts
        return text
    
    async def get_topic_headlines(self, topics, top=3):
        topic_news = {}
        for topic in topics:
            try:
                topic_headlines = self._api.topic_headlines(topic)['entries']
                topic_news[topic] = list(
                map(lambda x: self._clean(x['title']) + ' @ (' + x['published'] + ')', topic_headlines))[:top]
            except Exception as e:
                print(topic)
                print(e)
                topic_news[topic] = []
        return topic_news
    
    async def get_top_news(self):
        return self._api.top_news()
    
async def main():
    """
    Main method, call the appropriate methods
    :return:
    """
    google_api = GoogleApi()
    trends = google_api.get_news_for_locations(['United States', 'United Kingdom','India'])
    words = google_api.get_topic_headlines(['BUSINESS'])
    users = google_api.get_news_for_words(['bloomberg', 'cnbc'], 2)
    trends_text, words_text, news_users = await asyncio.gather(trends, words, users)
    print('LOCATION NEWS')
    for location, news in trends_text.items():
        print(f'Location: {location}  \n {news}')
    print('\nWORD NEWS')
    for word, news in words_text.items():
        print(f'Word: {word}  \n {news}')
    print('\nUSER NEWS')
    for user, news in news_users.items():
        print(f'User: {user}  \n {news}')
            
def news():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait([main()]))

#print(GoogleNews().geo_headlines('United States'))