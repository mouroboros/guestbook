from django.shortcuts import render
from guestbook.models import Comment


def home_page(request):
    comment = Comment()
    comment.text = request.POST.get('comment_text', '')
    comment.save()
    
    return render(request, 'home.html', {
        'new_comment_text' : comment.text,
        })
        
