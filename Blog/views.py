from django.shortcuts import render

def Detail(request):
    return render(request, 'Blog/detail.html')