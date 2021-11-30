from django import forms
from .models import Todo


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = '__all__'
        labels = {
            "task": "Task name",
            "complete": "Completed"
        }

        widgets = {
            'task': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Add tasks"
            }),
            'complete': forms.CheckboxInput(attrs={
                'class': 'form-check-input',
                'role': 'switch'
            })
        }
