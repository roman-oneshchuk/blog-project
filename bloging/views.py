from django.shortcuts import render, get_object_or_404
from .models import Bloging

# Create your views here.

def showblog(request):
	post = Bloging.objects
	return render(request, 'bloging/bloging.html', {'post':post})

def certain_post(request, post_id):
	id_post = get_object_or_404(Bloging, pk=post_id)
	return render(request, 'bloging/certain_post.html', {'id_post': id_post})