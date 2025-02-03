from bs4 import BeautifulSoup
import requests
import re 
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import string
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

ps = PorterStemmer()


url = 'https://www.theguardian.com/australia-news/2023/apr/06/outcry-as-australian-opposition-refuses-to-back-constitutional-recognition-of-indigenous-people'

def process_text(text):
    text = re.sub(r'[^a-zA-Z]', ' ', text)
    nopunc = [char for char in text if char not in string.punctuation]
    nopunc = ''.join(nopunc)
    clean_words = [word for word in nopunc.split() if word.lower() not in stopwords.words('english')]
    stemmed_words = [ps.stem(word) for word in clean_words]

    return " ".join(stemmed_words)

def timesOfIndiaScraper(url):
    html_text = requests.get(url)
    soup = BeautifulSoup(html_text.text, 'lxml')
    main_text = soup.find('div',class_ = "_s30J clearfix").text
    processed_text = main_text
    return processed_text


def theHinduscraper(url):
    html_text = requests.get(url)
    soup = BeautifulSoup(html_text.text, 'lxml')
    main_text = soup.find('div',class_ = "col-xl-9 col-lg-8 col-md-12 col-sm-12 col-12 storyline").text
    processed_text = main_text
    return processed_text


def newyorktimesScraper(url):
    html_text = requests.get(url)
    soup = BeautifulSoup(html_text.text, 'lxml')
    main_text = soup.find('div',class_ = "css-1ygdjhk evys1bk0").text
    # processed_text = process_text(main_text)
    return main_text


def theguardianscraper(url):
    html_text = requests.get(url)
    soup = BeautifulSoup(html_text.text, 'lxml')
    main_text = soup.find('div',class_ = "dcr-ch7w1w").text
    
    return main_text

theguardianscraper(url)
