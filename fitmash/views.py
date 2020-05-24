from django.shortcuts import render

# Create your views here.
def index(request):
    context={'text':"hello world", 'number':100}
    return render(request,'fitmash/index.html', context)

def other(request):
    return render(request,'fitmash/other.html')

def relative(request):
    return render(request,'fitmash/relative_url.html')
