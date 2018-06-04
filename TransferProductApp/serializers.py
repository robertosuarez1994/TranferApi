from .models import *
from rest_framework import serializers


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields =['id','name']

class BranchOfficeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BranchOffice
        fields = ['id','name']

class StockSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    branchOffice = BranchOfficeSerializer()
    class Meta:
        model = Stock
        fields = ('id','product','branchOffice','stock')
        depth = 1

class TransferSerializer(serializers.Serializer):
    class Meta:
     fields = ['branchFrom_id','branchTo_id','product_id','stock']