# coding:utf-8
__author__ = 'jummy'

from rest_framework import serializers

from goods.models import Goods, GoodsCategory


class CategorySerizlizer(serializers.ModelSerializer):
    class Meta:
        model = GoodsCategory
        fields = '__all__'


class GoodsSerizlizer(serializers.ModelSerializer):
    category = CategorySerizlizer()

    class Meta:
        model = Goods
        fields = '__all__'
