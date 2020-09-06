from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profile_api import serializers
class HelloApiView(APIView):
    """Test API View """

    serializer_class=serializers.HelloSerializer

    def get(self,request,format=None):
        """Returns a list of API View features"""
        an_apiview=[
        "its lalit yadav for the great learning",
        "it is similar to normal http et and post request",
        "give you most control over api logic"
        ]

        return Response({'message':"hello",'an_apiview':an_apiview})


    def post(self,request):
        """create a hello message with our name"""
        serializer=self.serializer_class(data=request.data)
        if serializer.is_valid():
            name=serializer.validated_data.get('name')
            message=f'Hello {name}'
            return Response({"message":message})

        else :
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def put(self,request,pk=None):
        """Handle updating an object"""
        return Response({'method':"put"})


    def patch(self,request,pk=None):
        """Handle a partial update of an object"""
        return Response({'method':"PATCH"})


    def delete(self,request,pk=None):
        """Delete an project"""
        return Response({"method":"Delete"})
