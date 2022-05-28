from rest_framework import serializers

from preparations.models import Drug, Box, DrugBox
from users.models import User

class DrugSerializer(serializers.ModelSerializer):

    class Meta:
        model = Drug
        fields = '__all__'


class DrugBoxSerializer(serializers.ModelSerializer):

    drug = serializers.SlugRelatedField(slug_field='name', queryset=Drug.objects.all())

    class Meta:
        model = DrugBox
        fields = ('id', 'drug', 'unit', 'amount', 'expiration_date')


class BoxSerializers(serializers.ModelSerializer):

    drugs = DrugBoxSerializer(
        many=True, source='drugs_in_box'
    )
    author = serializers.SlugRelatedField(slug_field='username', queryset=User.objects.all())

    class Meta:
        fields = ('id', 'name', 'author', 'drugs', )
        model = Box
