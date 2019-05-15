from django.shortcuts import render

# Create your views here.

# navbar
def gamemain(request):
    return render(request, "gamemain.html")

def main(request):
    return render(request, "main.html")

def wordmain(request):
    return render(request, "wordmain.html")
# navbar