
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from django.core.cache import cache
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from user_collection.manager import UserCollectionManager


class RegisterUser(APIView):
    @staticmethod
    def post(request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = User.objects.create_user(username=username, password=password)
        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)
        refresh_token = str(refresh)

        # Store tokens in session
        request.session['access_token'] = access_token
        request.session['refresh_token'] = refresh_token

        return Response({'access_token': access_token})


class FetchAllMovies(APIView):
    @staticmethod
    def get(request):
        try:
            data = UserCollectionManager.getAllMovies()
            return Response({"result" : "success", "data": data}, 200)
        except Exception as e:
            return Response({"result" : "failure", "message":str(e)}, 500)


# class RegisterUser(APIView):
#     @staticmethod
#     def post(request):
#         try:
#             return "10"
#         except Exception as e:
#             return Response({"result": "failure", "message": str(e)}, 500)


class UserCollection(APIView):
    @staticmethod
    def get(request):
        try:
            return "10"
        except Exception as e:
            return Response({"result": "failure", "message": str(e)}, 500)

    @staticmethod
    def post(request):
        try:
            return "10"
        except Exception as e:
            return Response({"result": "failure", "message": str(e)}, 500)


class CollectionDetailView(APIView):
    @staticmethod
    def get(request):
        try:
            return "10"
        except Exception as e:
            return Response({"result": "failure", "message": str(e)}, 500)

    @staticmethod
    def post(request):
        try:
            return "10"
        except Exception as e:
            return Response({"result": "failure", "message": str(e)}, 500)


class RequestCountView(APIView):
    permission_classes = [IsAuthenticated]  # Can be removed if no auth is required

    @staticmethod
    def get(request):
        count = cache.get('request_count', 0)
        return Response({'requests': count})


# View to reset the request count
class ResetRequestCountView(APIView):
    permission_classes = [IsAuthenticated]  # Can be removed if no auth is required

    @staticmethod
    def post(request):
        cache.set('request_count', 0)
        return Response({'message': 'Request count reset successfully'})