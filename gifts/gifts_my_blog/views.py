from django.shortcuts import render, redirect
from .models import Feedbacks

def index(request):
    title = "Gifts Blog"
    data = {"title": title}
    return render(request, 'index.html', data)

def blog(request):
    title = "blog"
    data = {"title": title}
    return render(request, 'blog.html', data)

def about(request):
    title = "about"
    data = {"title": title}
    return render(request, 'about.html', data)


def feedback(request):
    title = "feedback"
    feedbacks = Feedbacks.objects.filter(verified=True).order_by('-id')
    data = {"feedbacks": feedbacks, "title": title}
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        text = request.POST.get('feedback')
        Feedbacks.objects.create(name=name, email=email, text=text)
        return redirect('feedback')
    return render(request, 'feedback.html', data)
