# coding: utf-8

# from rest_framework.views import APIView
# from rest_framework import mixins
# from rest_framework.response import Response
from rest_framework import generics

from .models import Goods
from .serializers import GoodsSerizlizer
# Create your views here.


class GoodsListView(generics.ListAPIView):
    '''
    商品类别
    '''
    queryset = Goods.objects.all()
    serializer_class = GoodsSerizlizer
