from rest_framework.decorators import api_view
from bs4 import BeautifulSoup
from django.http.response import JsonResponse
from rest_framework.response import Response
import json, requests

# Create your views here.

@api_view(['POST'])
def days(request):

    request.method =='POST'
    mymonth=request.data.get('month')
    mydate=request.data.get('date')
    url=("https://nationaltoday.com/{}-{}-holidays/").format(mymonth, mydate)
    print(url)
    n_url = requests.get(url)
    n_soup = BeautifulSoup(n_url.content, 'html5lib')

    n_headings = n_soup.find_all("h3",{"class","holiday-title"})
    print(n_headings)

    #n_headings = n_headings[1:]

    n_days = []
    print(n_days)

    for th in n_headings:
        n_days.append(th.text)

        day=("national_day_{}-{}").format(mydate,mymonth)

    return JsonResponse(
        {day:n_days},safe=False)
