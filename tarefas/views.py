from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .models import Tarefa
from .forms import TarefaForm

# Create your views here.

def view_login(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(
            request,
            username=username,
            password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('tarefas:lista'))
        else:
            return render(request, 'tarefas/login.html', {
                'message': 'Credenciais invalidas.'
            })

    return render(request, 'tarefas/login.html')

def view_logout(request):
    logout(request)

    return render(request, 'tarefas/login.html', {
                'message': 'Foi desconetado.'
            })


def view_lista_tarefas(request):
    context = {'tarefas': Tarefa.objects.all()}
    return render(request, 'tarefas/tarefas.html', context)


def view_nova_tarefa(request):

    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('tarefas:login'))

    form = TarefaForm(request.POST or None)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('tarefas:lista'))

    context = {'form': form}
    return render(request, 'tarefas/nova.html', context)

@login_required
def view_editar_tarefa(request, tarefa_id):

    tarefa = Tarefa.objects.get(id=tarefa_id)
    form = TarefaForm(request.POST or None, instance=tarefa)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('tarefas:lista'))

    context = {'form': form, 'tarefa_id': tarefa_id}
    return render(request, 'tarefas/edita.html', context)


def view_apagar_tarefa(request, tarefa_id):

    tarefa = Tarefa.objects.get(id=tarefa_id)
    tarefa.delete()
    return HttpResponseRedirect(reverse('tarefas:lista'))