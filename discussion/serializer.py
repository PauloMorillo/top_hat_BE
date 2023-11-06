from .models import DiscussionQuestion
from rest_framework import serializers


class RecursiveField(serializers.Serializer):
    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data


class DiscussionQuestionSerializer(serializers.ModelSerializer):
    children = RecursiveField(many=True, read_only=True)

    class Meta:
        model = DiscussionQuestion
        fields = ('id', 'comment', 'user', 'children', 'parent')
