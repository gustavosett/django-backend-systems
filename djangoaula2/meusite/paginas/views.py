from django.shortcuts import render

def index(request):
    teste = 'kkkkkkkkkkkkk eh isso ai tio'
    context = {
        "teste": teste
    }
    return render(request, 'paginas/index.html', context)

def sobre(request):
    return render(request, 'paginas/sobre.html')