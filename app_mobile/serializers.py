from rest_framework import serializers
from .models import WordGroup, Homonym


class WordGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = WordGroup
        fields = '__all__'


class HomonymListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Homonym
        fields = ['homonym_name']

        def get_queryset(self):
            if 'keyword' in self.request.query_params:
                return Homonym.objects.filter(homonym_name__icontains=self.request.query_params['keyword'])
            return Homonym.objects.all()


class HomonymAllInfoSerializer(serializers.ModelSerializer):
    homonym_info = serializers.SerializerMethodField(read_only=True, source='get_homonym_info')

    class Meta:
        model = Homonym
        fields = ['id', 'homonym_name', 'homonym_info']

    def get_homonym_info(self, obj):
        return f"http://localhost:8000/api/v1/mobile/homonym/{obj.id}"

