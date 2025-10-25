from django.shortcuts import render

# Create your views here.
def home_page(request):
    return render(request, 'website/index.html')

def about_page(request):
    return render(request, "website/about_page.html")
