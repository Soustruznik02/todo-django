from django.test import TestCase, Client
from django.urls import reverse
from .views import UserListView
from .models import User, Task


#USER - VIEWS and TEMPLATES
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

#USER = MODEL
class UserModelTest(TestCase):

    def setUp(self):
        pass

    def test_email_max_length(self):
        # Arrange
        expected_max_length = 254

        # Act
        max_length = User._meta.get_field('email').max_length

        # Assert
        self.assertEqual(max_length, expected_max_length)

    def test_password_max_length(self):
        # Arrange
        expected_max_length = 50

        # Act
        max_length = User._meta.get_field('password').max_length

        # Assert
        self.assertEqual(max_length, expected_max_length)



#TASK - VIEWS and TEMPLATES

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

class TaskUpdateViewTest(TestCase):
    
    def setUp(self):
        self.client = Client()
        self.url = reverse("task-update",args=[1])

    def tearDown(self):
        pass

    def test_update_user_submit_btn(self):
        # Arrange
        Task.objects.create(
            id=1,
            is_completed=False,
            owner=User.objects.create(
                id=1,
                is_active=True,
                email="test@test.com",
                password="password123"
            ),
            title="Task1"
        )

        expected_result = "<input type=\"submit\" value=\"Submit\">"

        # Act
        result = self.client.get(self.url)

        # Assert
        self.assertInHTML(expected_result, str(result.content))

class TaskDeleteViewTest(TestCase):
    
    def setUp(self):
        self.client = Client()
        self.url = reverse("task-delete",args=[1])

    def tearDown(self):
        pass

    def test_delete_task_submit_btn(self):
        # Arrange
        Task.objects.create(
            id=1,
            is_completed=False,
            owner=User.objects.create(
                id=1,
                is_active=True,
                email="test@test.com",
                password="password123"
            ),
            title="Task1"
        )

        expected_result = "<input type=\"submit\" value=\"Ano\">"

        # Act
        result = self.client.get(self.url)

        # Assert
        self.assertInHTML(expected_result, str(result.content))

    def test_title_max_length(self):
        # Arrange
        expected_result = 70

        # Act
        max_length = Task._meta.get_field('title').max_length

        # Assert
        self.assertEqual(max_length, expected_result)