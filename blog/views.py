from django.http import  JsonResponse
from django.shortcuts import get_object_or_404
from .models import Post


# Create your views here.
def all_posts(request):

    posts = {}
    for post in Post.objects.filter(rascunho=False).order_by('-data'):
        
        posts[post.slug] = (
            {
                'titulo': post.titulo,
                'corpo': post.corpo,
                'data': post.data,
                'slug': post.slug,
                'tags' : [tag.nome for tag in post.tags.all()]
            }
        )
    
    return JsonResponse({'posts' : posts})

def post(request, slug):
    post = get_object_or_404(Post, slug=slug)

    return JsonResponse({
        'titulo': post.titulo,
        'corpo': post.corpo,
        'data': post.data,
        'slug': post.slug,
        'tags' : [tag.nome for tag in post.tags.all()]
        })

def all_tags(request):
    pass

def posts_with_tag(request):
    pass