from django.shortcuts import render

# Create your views here.

# navbar
def main(request):
    return render(request, "main.html")

def wordmain(request):
    return render(request, "wordmain.html")
    
def gamemain(request):
    return render(request, "gamemain.html")
# navbar