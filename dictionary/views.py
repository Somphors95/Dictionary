from django.shortcuts import render
from PyDictionary import PyDictionary

def home(request):
    return render(request, 'home.html')

def word(request):
    search = request.GET.get('search')
    dictionay = PyDictionary()
    meaning = dictionay.meaning(search)
    # antonym = dictionay.antonym(search)
    # synonym = dictionay.synonym(search)

    context = {
        'meaning': meaning['Noun'][0],
        # 'antonym': antonym,
        # 'synonym': synonym,
    }
    return render(request, 'word.html', context)