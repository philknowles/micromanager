from django import forms


class TaskForm(forms.Form):
    text = forms.CharField(max_length=40, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Add a task', 'arial-label': 'Task'}
    ))