from django.shortcuts import render

from bs4 import BeautifulSoup
import requests

# Create your views here.

def scrape( request):
    url = 'https://www.google.com'
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    links = []

    for link in soup.find_all('a'):
        links.append(link.get('href'))
    
    return render(request, 'index.html', {'links': links})

