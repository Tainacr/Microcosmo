from django import forms
from .models import Usuario

class CadastroForm(forms.ModelForm):
    senha = forms.CharField(widget=forms.PasswordInput)
    senha_conf = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Usuario
        fields = ['nome', 'cpf', 'email', 'ocupacao_do_usuario', 'senha']

    def clean(self):
        cleaned_data = super().clean()
        senha = cleaned_data.get("senha")
        senha_conf = cleaned_data.get("senha_conf")

        if senha != senha_conf:
            raise forms.ValidationError("As senhas não coincidem!")

class LoginForm(forms.Form):
    user = forms.CharField(label="CPF")
    password = forms.CharField(widget=forms.PasswordInput)
