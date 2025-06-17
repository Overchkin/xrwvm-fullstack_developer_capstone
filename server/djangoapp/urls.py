from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'djangoapp'

urlpatterns = [
    # path for login
    path('login', views.login_user, name='login'),

    # path for about page
    path('about', views.about, name='about'),

    # ici tu peux ajouter les autres routes nécessaires plus tard
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
