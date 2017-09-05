from django.shortcuts import render, redirect
from random import shuffle
words = ['kiss daniel', 'johnny drille', 'davido', 'wizkid', 'dbanj', 'justin bieber', 'usher', 'wuraaaa']

# Create your views here.
def index(request):
    print words
    return render(request, 'words_app/index.html')

def result(request):
    shuffle(words)
    number = int(request.session['name'])
    ind = 0
    context = {'some': []}
    while number > 0:
        context['some'].append(words[ind])
        ind += 1
        number -= 1
    print  context['some']
    return render(request, 'words_app/results.html', context)

def surprise(request):
    request.session['name'] = request.POST['number']

    return redirect('/results')
