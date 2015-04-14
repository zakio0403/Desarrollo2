from django.shortcuts import render
from django.views.generic import TemplateView
from django.template import loader, Context
from django.http import HttpResponse
from main.models import BodyPanelAdmin
# Create your views here.

class HomeView(TemplateView):
	template_name = 'home.html'

def cuerpo(request):
	cuerpo = BodyPanelAdmin.objects.all()
	mi_template =loader.get_template("cuerpo.html")
	mi_contexto = Context({'posts': cuerpo})
	return HttpResponse(mi_template.render(mi_contexto))