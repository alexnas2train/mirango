from django.http import  HttpResponse
from django.shortcuts import render
from rango.models import Category

def index(request):
    '''Start page view'''
    # Construct a dictionary to pass to the template engine as its context.
    category_list = Category.objects.order_by('-likes')[:5]
    context_dict = {'categories': category_list}

    return render(request, 'rango/index.html', context_dict)

def about(request):
    '''About Rango page'''
    # Some context for template
    context_dict = {'somemessage': "Another one message (about) from the context"}
    return render(request, 'rango/about.html', context_dict)


