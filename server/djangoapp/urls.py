from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),

    # Inclure les routes de l'app principale
    path('', include('djangoapp.urls')),

    # Pages HTML statiques servies directement (optionnel si déjà géré dans djangoapp.views)
    path('', TemplateView.as_view(template_name="Home.html"), name='home'),
    path('contact/', TemplateView.as_view(template_name="Contact.html")),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
