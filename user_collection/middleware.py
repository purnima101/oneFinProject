from django.utils.deprecation import MiddlewareMixin
from django.core.cache import cache


class RequestCounterMiddleware(MiddlewareMixin):
    @staticmethod
    def process_request(request):
        # Increment the request count stored in cache
        count = cache.get('request_count', 0)
        cache.set('request_count', count + 1)