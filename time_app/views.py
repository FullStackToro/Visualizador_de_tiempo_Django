from django.shortcuts import render, HttpResponse
from time import gmtime, strftime
from datetime import datetime


def index(request):
    return HttpResponse("aca va la ruta")

def tiempo(request):
    now = datetime.now()
    mes=['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Sept', 'Oct', 'Nov', 'Dic']
    mes_final=mes[now.month-1]
    if int(now.minute==0):
        minute='00'
    elif int(now.minute)<10:
        minute=str(f"0{now.minute}")
    else:
        minute=now.minute
    context = {
        "time": strftime("%Y-%m-%d %H:%M %p", gmtime()),
        "fecha": strftime("%b %d, %Y", gmtime()),
        "hora": strftime("%H:%M %p", gmtime()),
        "fecha2": str(f" {mes_final} {now.day},  {now.year}"),
        "hora2": str(f"{now.hour}:{str(minute)}"),
    }
    return render(request, 'index.html', context)