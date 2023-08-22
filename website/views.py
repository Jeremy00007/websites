import requests
from django.shortcuts import render
from django.http import HttpResponseNotFound

# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def blog(request):

    url = 'https://newsapi.org/v2/top-headlines?country=us&category=technology&apiKey=39ae7f77927f4e08bfc981e2a53a1b4f'
    response = requests.get(url)
    data = response.json()
    noticias = []

    for articulo in data['articles']:
        noticia = {}
        noticia['titulo'] = articulo['title']
        
        if articulo.get('urlToImage'):
            noticia['imagen'] = articulo['urlToImage']
        
        if articulo.get('description'):
            noticia['descripcion'] = articulo['description']
        
        noticias.append(noticia)

    context = {
        'noticias': noticias
    }

    return render(request, 'blog.html', context)

def contact(request):
    return render(request, 'contact.html')

def login(request):
    return render(request, 'login.html')

def cursos(request):
    return render(request, 'cursos.html')
def news(request):

  noticia_id = request.GET.get('id')

  if noticia_id is None:
    return HttpResponseNotFound("Noticia no encontrada")

  url = 'https://newsapi.org/v2/top-headlines?country=us&category=technology&apiKey=39ae7f77927f4e08bfc981e2a53a1b4f'
  response = requests.get(url)
  data = response.json()

  noticias = []

  for articulo in data['articles']:
    noticia = {}
    noticia['titulo'] = articulo['title']

    if articulo.get('urlToImage'):
      noticia['imagen'] = articulo['urlToImage']

    if articulo.get('description'):
      noticia['descripcion'] = articulo['description']

    noticias.append(noticia)
    
  context = {
    'noticias': noticias,
    'noticia_id': int(noticia_id)
  }

  noticia_seleccionada = noticias[context['noticia_id']]

  if 'url' in noticia_seleccionada:
    response = requests.get(noticia_seleccionada['url'])
    contenido_noticia = response.text
    context['news_content'] = contenido_noticia

  context['noticia_seleccionada'] = noticia_seleccionada

  return render(request, 'news.html', context)