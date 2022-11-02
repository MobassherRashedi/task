from django.forms import ModelForm
from .models import Task

class TaskForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            visible.label = ""

    class Meta:
        model = Task
        fields = ['name'] 