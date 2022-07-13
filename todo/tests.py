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


    def test_are_buttons_good(self):
        # Arrange
        User.objects.create(
            id=1,
            is_active=True,
            email="test@test.com",
            password="password123"
        )
        
        expected_update_btn_tag = "<button>Update User</button>"
        expected_update_url = "/users/update/1"

        expected_delete_btn_tag = "<button>Delete User</button>"
        expected_delete_url = "/users/delete/1"

        expected_create_btn_tag = "<button>Create User</button>"
        expected_create_url = "/users/create"

        # Act
        result = self.client.get(self.url)

        # Assert
        self.assertInHTML(expected_update_btn_tag, str(result.content))
        self.assertIn(expected_update_url, str(result.content))

        self.assertInHTML(expected_delete_btn_tag, str(result.content))
        self.assertIn(expected_delete_url, str(result.content))

        self.assertInHTML(expected_create_btn_tag, str(result.content))
        self.assertIn(expected_create_url, str(result.content))


class UserCreateViewTest(TestCase):
    
    def setUp(self):
        self.client = Client()
        self.url = reverse("user-create")

    def tearDown(self):
        pass

    def test_create_user_submit_btn(self):
        # Arrange
        expected_result = "<input type=\"submit\" value=\"Submit\">"

        # Act
        result = self.client.get(self.url)

        # Assert
        self.assertInHTML(expected_result, str(result.content))

class UserUpdateViewTest(TestCase):
    
    def setUp(self):
        self.client = Client()
        self.url = reverse("user-update",args=[1])

    def tearDown(self):
        pass

    def test_update_user_submit_btn(self):
        # Arrange
        User.objects.create(
            id=1,
            is_active=True,
            email="test@test.com",
            password="password123"
        )

        expected_result = "<input type=\"submit\" value=\"Submit\">"

        # Act
        result = self.client.get(self.url)

        # Assert
        self.assertInHTML(expected_result, str(result.content))

class UserDeleteViewTest(TestCase):
    
    def setUp(self):
        self.client = Client()
        self.url = reverse("user-delete",args=[1])

    def tearDown(self):
        pass

    def test_delete_user_submit_btn(self):
        # Arrange
        User.objects.create(
            id=1,
            is_active=True,
            email="test@test.com",
            password="password123"
        )

        expected_result = "<input type=\"submit\" value=\"Ano\">"

        # Act
        result = self.client.get(self.url)

        # Assert
        self.assertInHTML(expected_result, str(result.content))


#_____________TASKS_____________________

class TaskCreateViewTest(TestCase):
    
    def setUp(self):
        self.client = Client()
        self.url = reverse("task-create")

    def tearDown(self):
        pass

    def test_create_task_submit_btn(self):
        # Arrange
        expected_result = "<input type=\"submit\" value=\"Submit\">"

        # Act
        result = self.client.get(self.url)

        # Assert
        self.assertInHTML(expected_result, str(result.content))

