from django.shortcuts import render

# Create your views here.

def home_view(request):
    return render(request, 'Library.html')

def book1_view(request):
    return render(request, 'book1.html')

def book2_view(request):
    return render(request, 'book2.html')

def book3_view(request):
    return render(request, 'book3.html')

def book4_view(request):
    return render(request, 'book4.html')

def book5_view(request):
    return render(request, 'book5.html')