from django.shortcuts import render, redirect
from guestbook.models import Comment


def home_page(request):
    if request.method == 'POST' :
        new_comment_text = request.POST['comment_text']
        Comment.objects.create(text=new_comment_text)
        return redirect('/')
        
    return render(request, 'home.html')
        
