from django import forms

class FormularioContacto(forms.Form):
    
    asunto = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'placeholder': 'Asunto'}))
    nombre = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Nombre'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    mensaje = forms.CharField(max_length=3000, widget=forms.Textarea(attrs={'placeholder': 'Mensaje'}))

