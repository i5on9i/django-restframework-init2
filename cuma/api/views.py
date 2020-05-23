from django.shortcuts import render

from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from ..serializer import CumaSimpleApiParamSerializer

# Create your views here.

# https://www.django-rest-framework.org/tutorial/3-class-based-views/
class CumaApiView(APIView):
    # authentication_classes = (CsrfAuthentication,)
    permission_classes = (AllowAny, )

class SimpleApiView(CumaApiView):
    def post(self, request):
        """
        :param request:
        :return:
        """
        serializer = CumaSimpleApiParamSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST,
                            data={
                                'status': 'fail',
                                'message':  serializer.errors
                            })

        vdata = serializer.validated_data
        # result = riotapi.staticdata.rune(vdata)
        result = ''
        return Response(data={
            'status': 'success',
            'message': {
                'invertval' : 20,
                'result': result,}})