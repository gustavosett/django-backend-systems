from django.shortcuts import render

def index(request):
    teste = 'hmmm será que funciona?? xD'
    context = {
        "teste": teste
    }
    return render(request, 'paginas/index.html', context)

def sobre(request):
    return render(request, 'paginas/sobre.html')