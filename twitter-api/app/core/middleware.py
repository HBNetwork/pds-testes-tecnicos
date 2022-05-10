from core.models import User
from model_bakery import baker


class AlwaysAuthenticatedMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        user = User.objects.first()
        if not user:
            user = baker.make(User)

        request.user = user

        response = self.get_response(request)

        return response
