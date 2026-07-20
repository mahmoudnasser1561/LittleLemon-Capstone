from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Booking, Menu
from .serializers import bookingSerializer, menuSerializer

class bookingview(APIView):
    def get(self, request):
        items = Booking.objects.all()
        serializer = bookingSerializer(items, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = menuSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response({
                "status": "success",
                "data": serializer.data
                })