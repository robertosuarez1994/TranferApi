from django.shortcuts import render
from .models import Product,BranchOffice,Stock
from rest_framework import generics
from .serializers import *
from django.shortcuts import get_object_or_404

# Create your views here.


class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(
            queryset,
            pk=self.kwargs['pk'],
        )

class BranchOfficeList(generics.ListCreateAPIView):
    queryset = BranchOffice.objects.all()
    serializer_class = BranchOfficeSerializer

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(
            queryset,
            pk=self.kwargs['pk'],
        )

class StockList(generics.ListCreateAPIView):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(
            queryset,
            pk=self.kwargs['pk'],
        )


class ProductDetail(generics.RetrieveUpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class BranchOfficeDetail(generics.RetrieveUpdateAPIView):
    queryset = BranchOffice.objects.all()
    serializer_class = BranchOfficeSerializer

class StockDetail(generics.RetrieveUpdateAPIView):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer

