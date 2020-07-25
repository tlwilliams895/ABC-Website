import requests
from django.shortcuts import render


def get_jobs(request):
    url = 'https://www.themuse.com/api/public/jobs?level=Entry%20Level&level=Mid%20Level&location=Tampa%2C%20FL&page=1&descending=true'
    x = requests.get(url)
    jobs = x.json()['results']

    context = {
        'jobs': jobs,
        }

    return render(request, 'job_board/job_board.html', context)

