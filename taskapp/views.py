from django.views.generic import ListView, FormView
from django.views import View
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect
from .models import Task
from .forms import TaskForm

class TaskListView(ListView):
     model = Task
     template_name =  'taskapp/index.html'
     context_object_name = 'tasks'

     def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = TaskForm()
        return context

class createTask(FormView):
    template_name =  'taskapp/index.html'
    form_class = TaskForm
    model = Task
    success_url = reverse_lazy('task_list')

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            name = form.cleaned_data['name']
            Task.objects.create(name=name)
        return super().post(request, *args, **kwargs)


class TaskListCreateView(View):
    def get(self, request, *args, **kwargs):
        view = TaskListView.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = createTask.as_view()
        return view(request, *args, **kwargs)

# @csrf_exempt
def update_task_view(request,pk):
    if request.method == 'POST' or 'GET':
        item = Task.objects.get(id=pk)
        if item.completed == False:
            item.completed = True
        else:
            item.completed = False
        item.save()
    return redirect("/")

# @csrf_exempt
# def TaskUpdateView(request):
#     if request.method == 'POST':
#         pk = request.POST.get('pk')
#         item = Task.objects.get(id=pk)
#         if item.completed == False:
#             item.completed = True
#         else:
#             item.completed = False
#         item.save()
#         return JsonResponse({'succes': True,'completed':}, status=200)
#     else:
#         return JsonResponse({'succes': False, 'errors': []}, status=400)