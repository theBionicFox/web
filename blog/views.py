from django.shortcuts import render
from django.http import HttpResponse

posts = [
	{
		'author': 'jimk12',
		'title': 'Blog Post 1',
		'content': 'This is the first ever blog post.',
		'datePosted': 'April 28, 2019'
	},
	{
		'author': 'danielleket17',
		'title': 'Blog Post 2',
		'content': 'This post is from danielleket17.',
		'datePosted': 'April 29, 2019'
	}
]


def home(request):
	context = {
		'posts': posts
	}
	return render(request, 'blog/home.html', context)

def about(request):
	return render(request, 'blog/about.html', {'title': 'About'})