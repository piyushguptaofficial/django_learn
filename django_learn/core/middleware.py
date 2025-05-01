# Middleware is a framework of hook into Django's request/response processing
#It's a lightweight plugin that processes request before and after views are called.

from django.utils.deprecation import MiddlewareMixin

class SimpleLoggingMiddleware(MiddlewareMixin):
    def process_request(self, request):
        print(f"Request Path: {request.path}")

    def process_response(self, request, response):
        print(f"Response Status: {response.status_code}")
        return response
