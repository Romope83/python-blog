from django.shortcuts import render
#from .models import Recipe  # Exemplo de modelo

def index(request):
    # Recupera dados do banco de dados (exemplo)
    #receitas = Recipe.objects.all()

    # Cria um dicionário para enviar ao template
    # context = {
    #     'receitas': receitas
    # }

    return render(request, 'index.html')#, context)

def lista_posts(request):
    return render(request, 'lista_posts.html')#, context)