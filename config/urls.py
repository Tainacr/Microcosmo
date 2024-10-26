from django.contrib import admin
from django.urls import include, path
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('usuario/', ViewUsuario.as_view(), name='usuario'),
    path('questionarios/', ViewListaQuestionarios.as_view(), name='lista_questionarios'),
    path('questionario/<int:questionario_id>/', ViewQuestionario.as_view(), name='view_questionario'),
    path('material/', ViewMaterial, name='material'),
    path('material2/', ViewMaterial2, name='material2'),
    path('contato/', contato, name='contato'),
    path('cadastro/', cadastro, name='cadastro'),
    path('login/', login, name='login'),
]
