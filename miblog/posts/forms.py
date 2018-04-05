from django import forms
from pagedown.widgets import PagedownWidget
from .models import Post


class PostForm(forms.ModelForm):
    contenido = forms.CharField(widget=PagedownWidget)
    publish = forms.DateField(widget=forms.SelectDateWidget)

    class Meta:
        model = Post
        fields = [
            "titulo",
            "contenido",
            "imagenes",
            "draft",
            "publish",
        ]
