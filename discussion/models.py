from django.db import models
from mptt.models import MPTTModel, TreeForeignKey, TreeManager


class DiscussionQuestionManager(TreeManager):
    def viewable(self):
        """This method filter parents to show only tree structure"""
        queryset = self.get_queryset().filter(level=0)
        return queryset


class DiscussionQuestion(MPTTModel):
    """
    This model represents a discussion (teacher - student)
    """
    profile_choices = [("teacher", "TEACHER"), ("student", "STUDENT")]

    comment = models.TextField()
    user = models.CharField(max_length=10, choices=profile_choices)
    parent = TreeForeignKey(
        'self',
        on_delete=models.CASCADE,
        related_name='children',
        null=True,
        blank=True,
    )
    objects = DiscussionQuestionManager()
