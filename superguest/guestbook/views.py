from django.shortcuts import render
from django.http import HttpResponse

def home_page(request):
    return render(request, 'home.html', {
        'new_comment_text' : request.POST.get('comment_text', ''),
        })
        
