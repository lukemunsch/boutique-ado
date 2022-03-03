from django.shortcuts import render

# Create your views here.
def index(request):
    """crate view for our index page"""
    return render(request, 'home/index.html')
