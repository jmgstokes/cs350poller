# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render


# Create your views here.
from django.views.generic import TemplateView
class index(TemplateView):
	template_name = 'index.html'

# from django.http import HttpResponse
# from django.template import Context, loader

# def index(request):
# 	template = loader.get_template('index.html')
# 	return HttpResponse(template.render())