from django.shortcuts import render
from testapp.forms import MovieForm
from testapp.models import Movie
def index_view(request):
    return render(request,'index.html')


def add_movie_view(request):
    form=MovieForm()
    if request.method=='POST':
        form=MovieForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
        return index_view(request)
    return render(request,'addmovie.html',{'form':form}) 

def list_movie_view(request):
    movies_list=Movie.objects.all()
    return render(request,'listmovie.html',{'movies_list':movies_list}) 

# Create your views here.
