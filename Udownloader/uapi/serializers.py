from rest_framework import serializers


class UD_Serializer(serializers.Serializer):

	file=serializers.CharField()