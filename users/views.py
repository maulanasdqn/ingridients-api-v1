from rest_framework.views import APIView, Response

from users.serializers import UserSerializer

class Register(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(reraise_exception=True)
        serializer.save()
        return Response(serializer.data)

