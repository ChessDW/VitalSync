import requests
from django.http import JsonResponse
from django.core.cache import cache

def cedula_proxy(request, query):
    cache_key = f'cedula_{query}'
    cached = cache.get(cache_key)
    if cached:
        return JsonResponse(cached)

    try:
        response = requests.get(
            f'https://apis.gometa.org/cedulas/{query}',
            timeout=10
        )
        data = response.json()
        cache.set(cache_key, data, timeout=60 * 60 * 24 * 7)
        return JsonResponse(data)
    except Exception as e:
        if cached:
            return JsonResponse(cached)
        return JsonResponse({'error': str(e)}, status=500)