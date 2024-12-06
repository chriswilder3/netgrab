from django.shortcuts import render,redirect

from bs4 import BeautifulSoup
import requests

from .models import LinkAdress

# Create your views here.

def scrape( request):
    # url = request.POST.get('url')

    if request.method == 'POST':
        url = request.POST.get('url', '') 
            # Either get url if available or assign '' to url

        page = requests.get(url)
        soup = BeautifulSoup(page.text, 'html.parser')
        
        for link in soup.find_all('a'):
            link_address = link.get('href') # Gets the link attr of a tags
            link_name = link.string # Content inside a tag, which is usually
                                    # the name of that link in most sites
            link = LinkAdress( name = link_name, address = link_address)
            link.save()
            # We can also use LinkAdress.create( field =val...)

        return redirect('/')

    # If its get request
    links = LinkAdress.objects.all()

    return render(request, 'index.html', {'links': links})

def delete(request):
    LinkAdress.objects.all().delete()

    return render(request, 'index.html')


