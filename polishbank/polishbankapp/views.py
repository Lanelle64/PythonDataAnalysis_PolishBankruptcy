from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .ml_model import MLModel
from rest_framework import generics
from .models import PolishBank
from .serializers import PolishBankSerializer

class PolishBankListCreateView(generics.ListCreateAPIView):
    queryset = PolishBank.objects.all()
    serializer_class = PolishBankSerializer

class PolishBankPredictView(APIView):
    def post(self, request, *args, **kwargs):
        input_data = request.data.get('input_data', None)

        if input_data is None:
            return Response({'error': 'Input data is missing'}, status=status.HTTP_400_BAD_REQUEST)

        model_path = 'polishbankmodel.pkl'  
        ml_model = MLModel(model_path)

        try:
            prediction = ml_model.predict([input_data])
            return Response({'prediction': prediction.tolist()}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': f'Prediction failed: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)