# coding=utf-8
from enum import Enum
from rest_framework import serializers

__author__ = 'namh'

class CumaSimpleApiParamSerializer(serializers.Serializer):
    pass
    # interval = serializers.ChoiceField(choices=['month', 'week', 'day'], allow_empty=False)
    # start = serializers.DateField(input_formats=['%Y-%m-%d'])
    # end = serializers.DateField(input_formats=['%Y-%m-%d'])