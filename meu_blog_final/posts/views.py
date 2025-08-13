
from django.shortcuts import render,get_object_or_404
from .models import Post,LINGUAGENS

def index(request):
    # Recupera todos os objetos Post do banco de dados
    posts = Post.objects.all()

    # Cria um dicionário para enviar ao template
    context = {
        'posts': posts
    }

    # Renderiza o template 'index.html' com o contexto
    return render(request, 'index.html', context)


def lista_posts(request):
    return render(request, 'lista_posts.html')#, context)

def pagina_python(request):
    return render(request, 'python.html')#, context)

def post_detalhe(request, pk):
    post = get_object_or_404(Post, pk=pk)
    context = {'post': post}
    return render(request, 'post_detalhe.html', context)

def posts_por_linguagem(request, linguagem):
    linguagem_codigo = linguagem.upper()
    posts = Post.objects.filter(linguagem=linguagem_codigo)

    linguagem_nome = dict(LINGUAGENS).get(linguagem_codigo, 'Linguagem Desconhecida')

    context = {
        'posts': posts,
        'linguagem_nome': linguagem_nome
    }
    return render(request, 'lista_posts.html', context)