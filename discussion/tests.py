from rest_framework import status
from rest_framework.test import APITestCase
from discussion.models import DiscussionQuestion


class DiscussionQuestionTest(APITestCase):
    complete_endpoint = '/api/v1/discussion_question/'
    data = {
        "comment": "Hi Guys",
        "user": "teacher",
        "parent": None
    }

    def setUp(self) -> None:
        self.post_response = self.client.post(self.complete_endpoint, self.data, format='json')

    def test_create_discussion(self) -> None:
        """
        This method is a test to check if discussion is created as expected
        """
        self.assertEqual(self.post_response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(DiscussionQuestion.objects.count(), 1)
        self.assertEqual(DiscussionQuestion.objects.get().comment, self.data["comment"])
        self.assertEqual(DiscussionQuestion.objects.get().user, self.data["user"])

    def test_list_discussion(self) -> None:
        """
        This method is a test to check if discussion is returning data as expected
        """
        response = self.client.get(self.complete_endpoint, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]["comment"], self.data["comment"])
        self.assertEqual(response.data[0]["user"], self.data["user"])

    def test_update_discussion(self) -> None:
        """
        This method is a test to check if discussion is updating data as expected
        """
        new_data = self.data.copy()
        new_data["comment"] = "Hello dear students"
        response = self.client.put(f'{self.complete_endpoint}1/', data=new_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(DiscussionQuestion.objects.get().comment, new_data["comment"])
        self.assertEqual(DiscussionQuestion.objects.get().user, self.data["user"])

    def test_delete_discussion(self) -> None:
        """
        This method is a test to check if discussion is deleting data as expected
        """
        response = self.client.delete(f'{self.complete_endpoint}1/', format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(DiscussionQuestion.objects.count(), 0)

    def test_create_child_discussion(self) -> None:
        """
        This method is a test to check if discussion tree is created as expected
        """
        data = {
            "comment": "Hello teacher",
            "user": "student",
            "parent": 1
        }
        response = self.client.post(self.complete_endpoint, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        response = self.client.get(self.complete_endpoint,  format='json')
        self.assertEqual(DiscussionQuestion.objects.count(), 2)
        self.assertEqual(response.data[0]["children"][0]["parent"], data["parent"])
        self.assertEqual(response.data[0]["children"][0]["user"], data["user"])
