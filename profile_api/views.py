from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test API View """

    def get(self,request,format=None):
        """Returns a list of API View features"""
        an_apiview=[
        "its lalit yadav for the great learning",
        "it is similar to normal http et and post request",
        "give you most control over api logic"
        ]

        return Response({'message':"hello",'an_apiview':an_apiview})
