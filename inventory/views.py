# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import Http404

from inventory.models import Item

# Create your views here.

def index(request):	
	# items = Item.objects.exclude(amount=20) # .exclude = $not = $ne 
	items = Item.objects.all()
	return render(request, 'inventory/index.html',{
		'items': items,
	})

def item_detail(request, id):	
	try:
		item = Item.objects.get(id=id)
	except Item.DoesNotExist:
		raise Http404('This item does not exist!')
	return render(request, 'inventory/item_detail.html',{
		'item': item,
	})
	

# def index(request):
# 	return HttpResponse('<p>In index view</p>')

# def item_detail(request, id):
# 	return HttpResponse('<p>In item detail view with id {0}</p>'.format(id))
