import jwt
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from .models import *
from .serializers import JWTPayloadTrackSerializer
from rest_framework.views import APIView


def product_list(request):
    return render(request, "model_main/base.html", )


class TakeJWTPayload(APIView):
    @csrf_exempt
    def get(self, request):
        print('HEADERS: ', request.headers)
        encoded_jwt = request.headers['Authorization']
        print('ENCODED JWT: ', encoded_jwt)

        if encoded_jwt:
            decoded_payloads = jwt.decode(encoded_jwt, 'IamTajalIslam', algorithms=['HS256'])
            print('DECODED: ', decoded_payloads)

            if decoded_payloads:
                saved_jwt_payloads = JWTPayloadTrack.objects.create(
                    username=decoded_payloads['username'],
                    password=decoded_payloads['password'],
                    iat=decoded_payloads['iat']
                )

                serialized_payload = JWTPayloadTrackSerializer(saved_jwt_payloads)

                return Response(serialized_payload.data, status=status.HTTP_201_CREATED)

            else:
                return Response({'message': 'decode not working!'}, status=status.HTTP_400_BAD_REQUEST)

        else:
            return Response({'message': 'jwt payload not found!'}, status=status.HTTP_404_NOT_FOUND)


@csrf_exempt
def api_data(request):
    print(request.headers)
    data = {
        'division': list(Division.objects.values()),
        'category': list(Category.objects.values()),
        'chandaKatha': list(ChandaKatha.objects.values())

    }

    return JsonResponse(data, safe=False)
