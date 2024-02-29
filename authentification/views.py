from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import User

@csrf_exempt
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=username, password=password)
            return JsonResponse({'message': 'Login successful!'})
        except User.DoesNotExist:
            return JsonResponse({'error': 'Invalid credentials'}, status=400)
    return JsonResponse({'error': 'Invalid request method'}, status=405)
