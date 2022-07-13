from django.test import TestCase, Client
from django.urls import reverse
from .views import UserListView
from .models import User


class UserListViewTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.url = reverse("user-list")

    def tearDown(self):
        pass

    def test_should_render_text_empty(self):
        # Arrange
        expected_result = "<li>empty</li>"
        expected_status_code = 200

        # Act
        result = self.client.get(self.url)

        # Assert
        self.assertContains(
            result, 
            expected_result, 
            1, 
            expected_status_code
        )
        self.assertTemplateUsed(result, "user_list.html")
        self.assertTrue(list(result.context["object_list"]) == [])
        
