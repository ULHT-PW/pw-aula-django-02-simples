from django.shortcuts import render, HttpResponseRedirect, reverse
from .models import Tarefa
from .forms import TarefaForm

# Create your views here.

def view_lista_tarefas(request):
    context = {'tarefas': Tarefa.objects.all()}
    return render(request, 'tarefas/tarefas.html', context)


def view_nova_tarefa(request):

    form = TarefaForm(request.POST or None)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('tarefas:lista'))

    context = {'form': form}
    return render(request, 'tarefas/nova.html', context)


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