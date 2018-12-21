
from django.http import HttpResponse
from django.shortcuts import render
def homepage(request):
    return render(request,'home.html')

def counted(request):
    data=request.GET['fulltextares']
    word_list= data.split()
    list_length= len(word_list)



    return render(request,'count.html', {'fulltext':data, 'word':list_length})
def about(request):
    return HttpResponse("<h1> This is a about page</h1>")
def aboutus(request):
    return render(request,'aboutus.html')
