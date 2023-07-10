from django.shortcuts import render
from django.http import HttpResponse
from django.views import View


def teste_redirecionamento_view(request, *args, **kwargs):
    return HttpResponse("Teste com sucesso!")

class testeCBView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("Testando Novamente!")
