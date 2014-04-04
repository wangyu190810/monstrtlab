from django.shortcuts import render_to_response,get_object_or_404
from django.views.generic import DetailView
from news.models import News
def news(request):
    return render_to_response('news.html',)

class News(DetailView):
    news=News.objects.all()
