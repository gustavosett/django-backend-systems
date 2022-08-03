from django.shortcuts import render

def index(request):
    teste = 'a cor da pedrinho q hj tem campeonato'
    context = {
        "teste": teste
    }
    return render(request, 'paginas/index.html', context)

def sobre(request):
    return render(request, 'paginas/sobre.html')