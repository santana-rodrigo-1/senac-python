from django.urls import path, reverse_lazy
from django.contrib.auth import views as auth_views
from . import views
from .forms import CustomPasswordChangeForm

urlpatterns = [
    path("", views.home, name="home"),
    path("cadastro/", views.register, name="register"),
    path("sobre/", views.sobre, name="sobre"),
    path('perfil/editar-endereco/', views.editar_endereco, name='editar_endereco'),
    
    # Rotas do Perfil
    path('perfil/', views.perfil, name='perfil'),
    path('perfil/editar/', views.editar_perfil, name='editar_perfil'),
    
    # Rotas de Senha
    path('perfil/senha/', auth_views.PasswordChangeView.as_view(
        template_name='registration/password_change_form.html',
        form_class=CustomPasswordChangeForm,
        success_url=reverse_lazy('password_change_done')
    ), name='password_change'),
    
    path('perfil/senha/sucesso/', auth_views.PasswordChangeDoneView.as_view(
        template_name='registration/password_change_done.html'
    ), name='password_change_done'),
]