from django.shortcuts import render
from guestbook.models import Comment


def home_page(request):
    if request.method == 'POST' :
        new_comment_text = request.POST['comment_text']
        Comment.objects.create(text=new_comment_text)
    else:
        new_comment_text = ''
        
    return render(request, 'home.html', {
        'new_comment_text' : new_comment_text,
        })
        
