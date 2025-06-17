from django.http import JsonResponse, FileResponse, Http404
from django.contrib.auth import login, authenticate
import logging
import json
import os
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt

# Get an instance of a logger
logger = logging.getLogger(__name__)

# Create your views here.

# Create a `login_request` view to handle sign in request
@csrf_exempt
def login_user(request):
    # Get username and password from request.POST dictionary
    data = json.loads(request.body)
    username = data['userName']
    password = data['password']
    # Try to check if provide credential can be authenticated
    user = authenticate(username=username, password=password)
    data = {"userName": username}
    if user is not None:
        # If user is valid, call login method to login current user
        login(request, user)
        data = {"userName": username, "status": "Authenticated"}
    return JsonResponse(data)

# New view to serve about.html
def about(request):
    filepath = os.path.join(settings.BASE_DIR, 'frontend', 'static', 'about.html')
    if os.path.exists(filepath):
        return FileResponse(open(filepath, 'rb'), content_type='text/html')
    else:
        raise Http404("Page non trouvée")
