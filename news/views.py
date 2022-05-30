from django.shortcuts import render, redirect
from .models import News
from .forms import NewsForm
from django.views.generic import DetailView, UpdateView, DeleteView

class NewsDetailView(DetailView):
    model = News
    template_name = 'news/details_view.html'
    context_object_name ='article'

class NewsUpdateView(UpdateView):
    model = News
    template_name = 'news/create.html'

    form_class = NewsForm

class NewsDeleteView(DeleteView):
    model = News
    success_url = '/news/'
    template_name = 'news/news_delete.html'


def news_home(request):
    news = News.objects.all().order_by('data')
    return render(request, 'news/news_home.html', {'news': news})
    
def create(request):
    error = ''
    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news_home')
    else:
        error = 'Форма заполнена не верно'


    form = NewsForm()
    data = {
        'form': form,
        'error': error
    }

    return render(request, 'news/create.html', data)