from django.shortcuts import render
from django.shortcuts import HttpResponse

def index(request):
    return HttpResponse("Pagrindinis library puslapis, library homepage")


def books(request):
    return HttpResponse("Čia yra library puslapio, books skyrelis")
