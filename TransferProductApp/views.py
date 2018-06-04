from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse , JsonResponse
from django.shortcuts import render
from .models import Product,BranchOffice,Stock
from rest_framework import generics
from django.views.generic import View
from .serializers import *
from django.shortcuts import get_object_or_404
import json


# Create your views here.

class Transfer(generics.UpdateAPIView):
    
    def get_object():
        pass
    def get_response():
        pass
    def patch(self,request):
        #se deserealiza el json de request.data
        #en un obeto transfer con los atributos branchFrom_id,branchTo_id,producto_id,stock    
        try:
            stockFrom = Stock.objects.update_or_create(branchOffice=request.data['branchFrom_id'],product=request.data['product_id'])
        
            product_id =  Product.objects.get(pk=request.data['product_id'])
            branch_id = BranchOffice.objects.get(pk=request.data['branchTo_id'])            
            stockTo = Stock.objects.update_or_create(branchOffice=branch_id,product=product_id,defaults={'product':product_id,'stock':0})
            
                
            
            if (stockFrom[0].stock >= request.data['stock']):                      #verifico si hay stock suficiente para transferir

                stockFrom[0].stock = stockFrom[0].stock - request.data['stock']
                stockTo[0].stock = stockTo[0].stock + request.data['stock']
                
                stockFrom[0].save()
                stockTo[0].save()
                return JsonResponse({"code":"201","data":"Trasferencia realizada satasfactoriamente"})
            else:
                return JsonResponse({"code":"201","data":"No hay stock"})
        except Exception as e:
            return JsonResponse({'code':"201","data":"No hay producto en la sucursal emisora"})

class ProductList(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class BranchOfficeList(generics.ListAPIView):
    queryset = BranchOffice.objects.all()
    serializer_class = BranchOfficeSerializer


class StockList(generics.ListCreateAPIView):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer


class ProductDetail(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class BranchOfficeDetail(generics.RetrieveAPIView):
    queryset = BranchOffice.objects.all()
    serializer_class = BranchOfficeSerializer

class StockDetail(generics.RetrieveAPIView):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer


        