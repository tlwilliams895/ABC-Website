import requests
from django.shortcuts import render


url = 'https://www.themuse.com/api/public/jobs?category=Data%20Science&category=Engineering&level=Entry%20Level&level=Mid%20Level&level=Senior%20Level&level=management&level=Internship&location=Riverview%2C%20FL&location=Tampa%2C%20FL&page=1&descending=True'
x = requests.get(url)
jobs = x.json()['results']


def get_jobs(request):
    index = 0
    for job in jobs:
        while index < len(jobs):
            index += 1
       
    return render(request, 'job_board/job_board.html', {'jobs': jobs})

