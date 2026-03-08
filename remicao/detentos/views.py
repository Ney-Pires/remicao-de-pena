from django.shortcuts import render, get_object_or_404
from .models import Detento
from django.contrib.auth.decorators import login_required


# HOME (SEM login obrigatório)
def home(request):
    return render(request, 'detentos/home.html')


# FUNÇÃO AUXILIAR (SEM decorator)
def calcular_remicao(detento):

    dias_remidos = 0

    for atividade in detento.atividades.all():

        if atividade.tipo == 'TRABALHO':
            dias_remidos += atividade.quantidade // 3

        elif atividade.tipo == 'ESTUDO':
            dias_remidos += atividade.quantidade // 12

        elif atividade.tipo == 'LEITURA':
            dias_remidos += atividade.quantidade // 4

    pena_restante = detento.pena_total_dias - dias_remidos

    return dias_remidos, pena_restante


# VIEW lista
@login_required
def lista_detentos(request):

    detentos = Detento.objects.all()

    dados = []

    for d in detentos:

        dias_remidos, pena_restante = calcular_remicao(d)

        dados.append({

            "detento": d,
            "dias_remidos": dias_remidos,
            "pena_restante": pena_restante

        })

    return render(request, "detentos/lista.html", {"dados": dados})


# VIEW detalhe
@login_required
def detalhe_detento(request, detento_id):

    detento = get_object_or_404(Detento, pk=detento_id)

    dias_remidos, pena_restante = calcular_remicao(detento)

    return render(request, "detentos/detalhe.html", {

        "detento": detento,
        "dias_remidos": dias_remidos,
        "pena_restante": pena_restante

    })


# VIEW consulta
@login_required
def consulta_detento(request):

    resultado = None

    if request.method == "POST":

        nome = request.POST.get("nome")

        try:

            detento = Detento.objects.get(nome__iexact=nome)

            dias_remidos, pena_restante = calcular_remicao(detento)

            resultado = {

                "detento": detento,
                "dias_remidos": dias_remidos,
                "pena_restante": pena_restante

            }

        except Detento.DoesNotExist:

            resultado = "Detento não encontrado."

    return render(request, "detentos/consulta.html", {"resultado": resultado})
