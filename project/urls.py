"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from ejemplo.views import (index, saludar_a, sumar, 
                            buscar, monstrar_familiares,
                            BuscarFamiliar, AltaFamiliar,
                            ActualizarFamiliar, BorrarFamiliar,
                            FamiliarList, FamiliarCrear, FamiliarBorrar, FamiliarActualizar, FamiliarDetalle)
from ejemplo_dos.views import (index, about, PostDetalle, PostListar, 
                               PostCrear, PostBorrar, PostActualizar,
                               UserSignUp, UserLogin, UserLogout, 
                               AvatarActualizar, UserActualizar, MensajeCrear, MensajeListar, MensajeDetalle )
from django.contrib.admin.views.decorators import staff_member_required

urlpatterns = [
    path('admin/', admin.site.urls),
    path('mi-blog/', index, name="mi-blog-index"),
    path('mi-blog/<int:pk>/detalle/', PostDetalle.as_view(), name="mi-blog-detalle"),
    path('mi-blog/listar/', PostListar.as_view(), name="mi-blog-listar"),
    path('mi-blog/crear/', staff_member_required(PostCrear.as_view()), name="mi-blog-crear"),
    path('mi-blog/<int:pk>/borrar/', staff_member_required(PostBorrar.as_view()), name="mi-blog-borrar"),
    path('mi-blog/<int:pk>/actualizar/', staff_member_required(PostActualizar.as_view()), name="mi-blog-actualizar"),
    path('mi-blog/signup/', UserSignUp.as_view(), name ="mi-blog-signup"),
    path('mi-blog/login/', UserLogin.as_view(), name= "mi-blog-login"),
    path('mi-blog/logout/', UserLogout.as_view(), name="mi-blog-logout"),
    path('mi-blog/avatars/<int:pk>/actualizar/', AvatarActualizar.as_view(), name="mi-blog-avatars-actualizar"),
    path('mi-blog/users/<int:pk>/actualizar/', UserActualizar.as_view(), name="mi-blog-users-actualizar"),
    path('mi-blog/mensajes/crear/', MensajeCrear.as_view(), name="mi-blog-mensajes-crear"),
    path('mi-blog/mensajes/<int:pk>/detalle/', MensajeDetalle.as_view(), name="mi-blog-mensajes-detalle"),
    path('mi-blog/mensajes/listar/', MensajeListar.as_view(), name="mi-blog-mensajes-listar"),
    path('mi-blog/about', about, name="about"),
    
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
