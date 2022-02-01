class NewsArticle:
    '''' Class instantiating news objects'''
    def __init__(self,article_id,article_image,title,description,author,time_published,url):
        self.article_id = article_id        
        self.article_image = article_image
        self.title = title
        self.description = description
        self.author = author
        self.time_published = time_published
        self.url = url
        
class Sources:
    ''' Class to define the news sources ojbjects'''
    def __init__(self,source_id,source_name,description, source_url ):
        self.source_id = source_id
        self.source_name = source_name
        self.description = description
        self.source_url = source_url

# class News_Headline:
#     def __init__()
    
    