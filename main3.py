class NewsSourse:
    def get_news(self):
        pass
class GoogleNewsAPI(NewsSourse):
    def get_news(self):
        return ['Новость1', 'новость2']
class LocalNewsAPI(NewsSourse):
    def get_news(self):
        return ["Местная новость A", "Местная новость B"]
class NewsWidget:
    def __init__(self, source: NewsSourse):
        self.source = source  # Зависит от абстракции, не от реализации
    def render(self):
        news = self.source.get_news()
        print(news)
class2