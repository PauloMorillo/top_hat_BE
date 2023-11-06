from .models import DiscussionQuestion
from .serializer import DiscussionQuestionSerializer
from rest_framework import viewsets


class DiscussionQuestionViewSet(viewsets.ModelViewSet):
    queryset = DiscussionQuestion.objects.viewable()
    serializer_class = DiscussionQuestionSerializer
