from django.shortcuts import render

# Create your views here.
 
# navbar
def main(request):
    return render(request, "main.html")

def wordmain(request):
    return render(request, "wordmain.html")

def gamemain(request):
    return render(request, "gamemain.html")
# navbar fin

def wordresult(request):
    text = request.GET['fulltext']
    lenth = len(text)
    words = text.split()
    dict_word = {}
    
    #딕셔너리 만들기
    for w in words: 
        if w in dict_word:
            #add to dict
            dict_word[w] = dict_word[w] + 1
        else:
            dict_word[w] = 1    
          
    return render(request, "wordresult.html", {'full' : text, 'total' : len(words), 'dict' : dict_word.items(), 'lenth' : lenth})