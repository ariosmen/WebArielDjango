from django.shortcuts import render
from contacto.form import FormularioContacto
from django.core.mail import send_mail

def contacto(request):
    valid = False
    if request.method == 'POST':
        formulario = FormularioContacto(request.POST)
        if formulario.is_valid():
            valid = True
            info = formulario.cleaned_data
            send_mail(info['asunto'], info['mensaje'], info.get('email', ''), ['arielmendezcantautor@gmail.com'], fail_silently=False)
            return render(request, 'contacto.html', {'formulario': formulario, 'valid': valid})
    else:
        formulario = FormularioContacto()
    
    return render(request, 'contacto.html', {'formulario': formulario, 'valid': valid})