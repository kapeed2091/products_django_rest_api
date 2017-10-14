# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from rest_framework import serializers
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


class ProductRequestType(object):
    def __init__(self, p_name):
        self.p_name = p_name


class ProductRequestSerializer(serializers.Serializer):
    p_name = serializers.CharField()

    def create(self, validated_data):
        return ProductRequestType(**validated_data)


class ProductResponseType(object):
    def __init__(self, p_id, score, product_name):
        self.p_id = p_id
        self.score = score
        self.product_name = product_name


class ProductResponseSerializer(serializers.Serializer):
    p_id = serializers.IntegerField()
    score = serializers.IntegerField()
    product_name = serializers.CharField()

    def create(self, validated_data):
        return ProductResponseType(**validated_data)


@api_view(['GET'])
def product_match(request):
    # TODO: here goes your actual logic

    product_list = list()
    product_list.append(ProductResponseType(p_id=1, score=100, product_name='Product-1'))
    product_list.append(ProductResponseType(p_id=2, score=90, product_name='Product-2'))

    response_serializer = ProductResponseSerializer(product_list, many=True)
    return Response(response_serializer.data, status=status.HTTP_200_OK)
