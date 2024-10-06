from rest_framework_simplejwt.tokens import RefreshToken
from django.core.cache import cache
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from user_collection.manager import UserManagement, CollectionManagement
from user_collection.serializers import UserSerializer
from rest_framework import status

class RegisterUser(APIView):
    @staticmethod
    def post(request):
        try:
            serializer = UserSerializer(data=request.data)
            if serializer.is_valid():
                user = serializer.save()
                refresh = RefreshToken.for_user(user)
                return Response({
                    'access_token': str(refresh.access_token)
                }, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"result": "failure", "message": str(e)}, 500)


class FetchAllMovies(APIView):
    @staticmethod
    def get(request):
        try:
            data = UserManagement.get_movies_list()
            return Response({"result" : "success", "data": data}, 200)
        except Exception as e:
            return Response({"result" : "failure", "message":str(e)}, 500)




class UserCollection(APIView):
    permission_classes = [IsAuthenticated]
    @staticmethod
    def get(request):
        try:
            return "10"
        except Exception as e:
            return Response({"result": "failure", "message": str(e)}, 500)

    @staticmethod
    def post(request):
        try:
            data = request.data
            get_movies = CollectionManagement.add_new_collection(request, data)
            return Response(data=get_movies, status=status.HTTP_400_BAD_REQUEST)
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