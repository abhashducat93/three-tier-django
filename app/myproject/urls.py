from django.contrib import admin
from django.http import JsonResponse
from django.urls import path

def home(request):
    return JsonResponse({
        'message': 'Welcome to Three-Tier Django App!',
        'status': 'success',
        'tier': 'application'
    })

def health_check(request):
    return JsonResponse({
        'status': 'healthy',
        'service': 'three-tier-django-app',
        'database': 'connected' if check_db_connection() else 'disconnected'
    })

def check_db_connection():
    from django.db import connection
    try:
        connection.ensure_connection()
        return True
    except Exception:
        return False

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('health/', health_check),
    path('api/data/', lambda r: JsonResponse({'data': [1, 2, 3, 4, 5]})),
]
