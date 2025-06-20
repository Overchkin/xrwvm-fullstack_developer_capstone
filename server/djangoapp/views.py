from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, FileResponse, Http404
from django.contrib.auth import authenticate, login
import json
import os
from django.conf import settings

# Optionnel : import pour CORS si nécessaire (à installer via pip install django-cors-headers)
from django.views.decorators.csrf import ensure_csrf_cookie
from django.utils.decorators import decorator_from_middleware
#from corsheaders.middleware import CorsMiddleware

# Si tu veux appliquer CORS sur cette vue (optionnel)
# login_user = decorator_from_middleware(CorsMiddleware)(login_user)


@csrf_exempt  # ok en dev, à retirer en prod absolument
def login_user(request):
    if request.method == 'GET':
        return JsonResponse({'message': 'Envoyez un POST avec userName et password'}, status=200)
    
    if request.method != 'POST':
        return JsonResponse({'error': 'Méthode non autorisée, POST uniquement.'}, status=405)

    try:
        if not request.body:
            return JsonResponse({'error': 'Requête vide'}, status=400)

        data = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({'error': 'JSON invalide'}, status=400)

    username = data.get('userName')
    password = data.get('password')

    if not username or not password:
        return JsonResponse({'error': 'Nom d\'utilisateur et mot de passe requis'}, status=400)

    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        return JsonResponse({'userName': username, 'status': 'Authenticated'})
    else:
        return JsonResponse({'error': 'Nom d\'utilisateur ou mot de passe incorrect'}, status=401)


def about(request):
    filepath = os.path.join(settings.BASE_DIR, 'frontend', 'static', 'about.html')
    if os.path.exists(filepath):
        return FileResponse(open(filepath, 'rb'), content_type='text/html')
    else:
        raise Http404("Page non trouvée")
