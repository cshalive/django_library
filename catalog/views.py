from django.shortcuts import render, HttpResponse

# Create your views here.

# csh. 5th May 2024. Added below lines of code
def catalog_home(request):
    #return HttpResponse("Hello from Catalog home page")  # works without a home.html/index.html
    # however, urls.py in the parent folder and 
    # [check] a new url.py under current app folder needs to be updated

    return render(request, "catalog_home.html")  # works only if .html is inside templates folder
