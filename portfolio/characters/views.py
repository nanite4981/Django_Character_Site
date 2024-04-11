# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Character

def characters(request):
    mycharacters = Character.objects.all().values()
    template = loader.get_template('all_characters.html')
    context = {
        'mycharacters': mycharacters,
    }
    return HttpResponse(template.render(context, request))

def details(request, id):
  mycharacter = Character.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'mycharacter': mycharacter,
  }
  return HttpResponse(template.render(context, request))