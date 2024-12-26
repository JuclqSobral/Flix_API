
from django.db.models import Avg
from rest_framework import serializers
from movies.models import Movie
from movies.models import Genre
from movies.models import Actor

class MovieModelSerializer(serializers.ModelSerializer):
    rate = serializers.SerializerMethodField(read_only=True)
    
    
    class Meta:
        model = Movie
        fields = '__all__'
    
    def get_rate(self, obj):
        rate = obj.reviews.aggregate(Avg('stars'))['stars__avg']
        
        if rate:
            return round(rate, 1)
        
        return None
        
            
    def validate_realease_date(self, value):
        if value.year < 1900:
            raise serializers.ValidationError('A data do lançamento não pode ser anterior a 1900.')
        return value
    
    def validate_resume(self, value):
        if len(value) > 500:
            raise serializers.ValidationError('Resumo maior que 500 caracteres.')
        return value
    
