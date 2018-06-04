from django.conf.urls import url
from .views import *



urlpatterns = [
    url(r'^products/$',ProductList.as_view(), name='products'),
    url(r'^branch-offices/$',BranchOfficeList.as_view(), name='branchoffices'),
    url(r'^stocks/$',StockList.as_view(), name='stocks'),
    
    url(r'^products/(?P<pk>[0-9]+)$',ProductDetail.as_view(), name='product'),
    url(r'^branch-offices/(?P<pk>[0-9]+)$',BranchOfficeDetail.as_view(), name='branchoffice'),
    url(r'^stocks/(?P<pk>[0-9]+)$',StockDetail.as_view(), name='stock'),

    url(r'^stocks/transfer/$', Transfer.as_view() ,name="transfer")
    
]