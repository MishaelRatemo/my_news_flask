from multiprocessing import process
from unicodedata import category
import urllib.request
import json

# from webbrowser import get
from .models import NewsArticle, Sources

# get the api key
api_key = None

# get news base url  set to none in the begininng
news_base_url = None

# category source url
category_url = None

# function that takes in the app instance(API_key,news_base_url) and replaces the values of None


def config_request(app):
    global api_key, news_base_url, source
    api_key = app.config['NEWS_API_KEY']
    news_base_url = app.config['NEWS_API_BASE_URL']


def get_sources(news):
    ''' Method gettingt he javascript object notations(JSON) response to url requests'''
    get_sources_url = news_base_url.format(news, api_key)
    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        sources_results = None
        if get_sources_response['articles']:
            sources_results_list = get_sources_response['articles']
            sources_results = process_sources_results(sources_results_list)

    return sources_results


def process_sources_results(sources_list):
    '''
    Method that processes the sourcces result and transform them to a list of Objects

    Args:
       sources_results: A list of dictionaries that contain sources details

    Returns :
       sources_results: A list of sources objects
    '''
    sources_results = []
    for source_item in sources_list:
        source_id = source_item.get('source_id')
        source_name = source_item.get('source_name')
        description = source_item.get('description')
        source_url = source_item.get('source_url')
        if source_id:
            source_obj = Sources(source_id, source_name,
                                 description, source_url)
            sources_results.append(source_obj)

    return sources_results


def get_articles_source(id):
    ''' Function to get the articles object'''
    articles_source_url = 'https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'.format(
        id, api_key)
    print(articles_source_url)
    with urllib.request.urlopen(articles_source_url) as url:
        articles_source_data = url.read()
        articles_source_response = json.loads(articles_source_data)

        article_source_results = None

        if articles_source_response['articles']:
            article_source_list = articles_source_response['articles']
            article_source_results = process_articles_results(
                article_source_list)

    return article_source_results


def process_articles_results(newslist):
    '''
    function that processes the json files of articles from the api key
    '''
    article_source_results = []
    for article in newslist:
        article_id = article.get('article_id')
        article_image = article.get('urlToImage')
        title = article.get('title')
        description = article.get('description')
        author = article.get('author')
        time_published = article.get('publishedAt')
        url = article.get('url')

        if article_image:
            article_objects = NewsArticle(
                article_id, article_image, title, description, author, time_published, url)
            article_source_results.append(article_objects)

    return article_source_results


def get_headlines():
    '''
    function that gets the response to the category json
    '''
    get_headlines_url = 'https://newsapi.org/v2/top-headlines?country=us&apiKey={}'.format(
        api_key)
    print(get_headlines_url)
    with urllib.request.urlopen(get_headlines_url) as url:
        get_headlines_data = url.read()
        headlines_response = json.loads(get_headlines_data)

        headlines_results = None

        if headlines_response['articles']:
            get_headlines_list = headlines_response['articles']
            headlines_results = process_articles_results(get_headlines_list)

    return headlines_results


def article_source(article_id):
    ''' function to get artcles '''
    # art is use to refert o article
    art_source_url = 'https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'.format(
        article_id, api_key)
    print(art_source_url)
    with urllib.request.urlopen(art_source_url) as url:
        art_source_data = url.read()
        art_source_response = json.loads(art_source_data)
        art_source_results = None
        if art_source_response['articles']:
            art_source_list = art_source_response['articles']
            art_source_results = process_articles_results(art_source_list)

    return art_source_results


def get_news_category(category_name):
    ''' function returning news categories in json format'''
    get_category_url = 'https://newsapi.org/v2/everything?q={}&apiKey={}'.format(
        category_name, api_key)
    print(get_category_url)
    with urllib.request.urlopen(get_category_url) as url:
        get_category_data = url.read()
        get_cartegory_response = json.loads(get_category_data)

        cartegory_results = None

        if get_cartegory_response['articles']:
            get_cartegory_list = get_cartegory_response['articles']
            cartegory_results = process_articles_results(get_cartegory_list)

    return cartegory_results
