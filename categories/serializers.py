from rest_framework import serializers


class CategorySerializer(serializers.Serializer):
    name = serializers.CharField(
        required=True,
        max_length=50,
    )
    kind = serializers.CharField(
        max_length=15,
    )
    pk = serializers.IntegerField(read_only=True)
    created_at = serializers.DateTimeField(read_only=True)
