from django.shortcuts import render, HttpResponse

# Create your views here.
def hello(request, nome, idade):
	return HttpResponse('<h1>Hello, {} de {} anos</h1>'.format(nome, idade))

def addition(request, v1, v2):
	sum = v1 + v2
	return HttpResponse('Sum: <b>{}</b>'.format(sum))

def subtraction(request, v1, v2):
	subtract = v1 - v2
	return HttpResponse('Subtraction: <b>{}</b>'.format(subtract))

def multiplication(request, v1, v2):
	multiply = v1 * v2
	return HttpResponse('Product: <b>{}</b>'.format(multiply))

def division(request, v1, v2):
	divide = v1 / v2
	return HttpResponse('Quotient: <b>{}</b>'.format(divide))

