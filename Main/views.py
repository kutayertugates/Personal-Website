from django.shortcuts import render

def homepage(request):
    return render(request, 'Main/index.html')