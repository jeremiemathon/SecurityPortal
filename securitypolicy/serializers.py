from rest_framework import serializers
from .models import Section, Rule


class SectionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Section
        fields = ('title', 'description')

class RuleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Rule
        fields = ('title', 'section', 'content')
