from django.test import TestCase, Client
from django.urls import reverse, resolve
from django import forms
from .views import (
UserListView, UserCreateView, UserUpdateView, UserDeleteView, TaskListView, TaskCreateView, TaskUpdateView, TaskDeleteView)
from .models import User, Task
from .forms import UserCreateForm, UserUpdateForm


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

    def test_correct_model(self):
        # Arrange
        expected_model = User
        # Act
        model = UserListView.model
        # Assert
        self.assertEqual(model, expected_model)

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

    def test_create_view_seccess_url(self):
        # Arrange
        expected_success_url = '/users'
        # Acr
        success_url = UserCreateView.success_url
        # Assert
        self.assertEqual(success_url, expected_success_url)

    def test_correct_user_create_form(self):
        # Arrange
        expected_form = UserCreateForm
        # Act
        form = UserCreateView.form_class
        # Assert
        self.assertEqual(form, expected_form)
    
    def test_correct_model(self):
        # Arrange
        expected_model = User
        # Act
        model = UserCreateView.model
        # Assert
        self.assertEqual(model, expected_model)

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

    def test_update_view_seccess_url(self):
        # Arrange
        expected_success_url = '/users'
        # Acr
        success_url = UserUpdateView.success_url
        # Assert
        self.assertEqual(success_url, expected_success_url)
    
    def test_correct_user_update_form(self):
        # Arrange
        expected_form = UserUpdateForm
        # Act
        form = UserUpdateView.form_class
        # Assert
        self.assertEqual(form, expected_form)

    def test_correct_model(self):
        # Arrange
        expected_model = User
        # Act
        model = UserUpdateView.model
        # Assert
        self.assertEqual(model, expected_model)

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

    def test_delete_view_seccess_url(self):
        # Arrange
        expected_success_url = '/users'
        # Acr
        success_url = UserDeleteView.success_url
        # Assert
        self.assertEqual(success_url, expected_success_url)

    def test_correct_model(self):
        # Arrange
        expected_model = User
        # Act
        model = UserDeleteView.model
        # Assert
        self.assertEqual(model, expected_model)

#USER - MODEL
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
class TaskListViewTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.url = reverse("task-list")

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
        self.assertTemplateUsed(result, "task_list.html")
        self.assertTrue(list(result.context["object_list"]) == [])

    def test_are_buttons_good(self):
        # Arrange
        Task.objects.create(
            id=1,
            owner=User.objects.create()
        )
        
        expected_update_btn_tag = "<button>Update Task</button>"
        expected_update_url = "/tasks/update/1"

        expected_delete_btn_tag = "<button>Delete Task</button>"
        expected_delete_url = "/tasks/delete/1"

        expected_create_btn_tag = "<button>Create Task</button>"
        expected_create_url = "/tasks/create"

        # Act
        result = self.client.get(self.url)

        # Assert
        self.assertInHTML(expected_update_btn_tag, str(result.content))
        self.assertIn(expected_update_url, str(result.content))

        self.assertInHTML(expected_delete_btn_tag, str(result.content))
        self.assertIn(expected_delete_url, str(result.content))

        self.assertInHTML(expected_create_btn_tag, str(result.content))
        self.assertIn(expected_create_url, str(result.content))

    def test_correct_model(self):
        # Arrange
        expected_model = Task
        # Act
        model = TaskListView.model
        # Assert
        self.assertEqual(model, expected_model)

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

    def test_create_task_seccess_url(self):
        # Arrange
        expected_success_url = '/tasks'
        # Acr
        success_url = TaskCreateView.success_url
        # Assert
        self.assertEqual(success_url, expected_success_url)

    def test_title_length_input(self):
        # Arrange
        wrong_input = 36*'xo'
        # Acte
        result = self.client.post(
            self.url,
            {'title' : wrong_input}
        )
        # Assert
        self.assertEqual(result.status_code, 200) # Není nutno
        self.assertContains(
            result, 
            "Ensure this value has at most 70 characters (it has 72).", 
            html=True
        )    

    def test_correct_model(self):
        # Arrange
        expected_model = Task
        # Act
        model = TaskCreateView.model
        # Assert
        self.assertEqual(model, expected_model)

class TaskUpdateViewTest(TestCase):
    
    def setUp(self):
        self.client = Client()
        self.url = reverse("task-update",args=[1])

    def tearDown(self):
        pass

    def test_update_task_submit_btn(self):
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

    def test_update_task_seccess_url(self):
        # Arrange
        expected_success_url = '/tasks'
        # Acr
        success_url = TaskUpdateView.success_url
        # Assert
        self.assertEqual(success_url, expected_success_url)

    def test_correct_model(self):
        # Arrange
        expected_model = Task
        # Act
        model = TaskUpdateView.model
        # Assert
        self.assertEqual(model, expected_model)

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

    def test_delete_task_seccess_url(self):
        # Arrange
        expected_success_url = '/tasks'
        # Acr
        success_url = TaskDeleteView.success_url
        # Assert
        self.assertEqual(success_url, expected_success_url)

    def test_correct_model(self):
        # Arrange
        expected_model = Task
        # Act
        model = TaskDeleteView.model
        # Assert
        self.assertEqual(model, expected_model)

#TASK - MODEL
class TaskModelTest(TestCase):

    def test_title_max_length(self):
        # Arrange
        expected_result = 70

        # Act
        max_length = Task._meta.get_field('title').max_length

        # Assert
        self.assertEqual(max_length, expected_result)

#FORM
class UserCreateFormTest(TestCase):
    
    def test_password_widget(self):
        # Arrange
        # Act
        result = UserCreateForm().fields["password"].widget
        # Assert
        self.assertIsInstance(result, forms.PasswordInput)

    
    def test_email_length_input(self):
        # Arrange
        wrong_input = 128*'xo'
        # Act
        result = UserCreateForm(data={"email" : wrong_input})
        # Assert
        self.assertFalse(result.is_valid())
        self.assertNotEqual(len(result.errors["email"]), 0 )
        self.assertEqual(
            result.errors["email"], 
            [
                'Enter a valid email address.', 
                "Ensure this value has at most 254 characters (it has 256)."
            ]
        )

    def test_password_length_input(self):
        # Arrange
        wrong_input = 26*'xo'
        # Act
        result = UserCreateForm(data={"password" : wrong_input})
        # Assert
        self.assertFalse(result.is_valid())
        self.assertNotEqual(len(result.errors["password"]), 0 )
        self.assertEqual(
            result.errors["password"], 
            [ 
                "Ensure this value has at most 50 characters (it has 52)."
            ]
        )

    def test_correct_model(self):
        # Arrange
        expected_model = User
        # Act
        model = UserCreateForm.Meta.model
        # Assert
        self.assertEqual(model, expected_model)

class UserUpdateFormTest(TestCase):
    
    def test_password_widget(self):
        # Arrange
        # Act
        result = UserUpdateForm().fields["password"].widget
        # Assert
        self.assertIsInstance(result, forms.PasswordInput)

    def test_email_length_input(self):
        # Arrange
        wrong_input = 128*'xo'
        # Act
        result = UserUpdateForm(data={"email" : wrong_input})
        # Assert
        self.assertFalse(result.is_valid())
        self.assertNotEqual(len(result.errors["email"]), 0 )
        self.assertEqual(
            result.errors["email"], 
            [
                'Enter a valid email address.', 
                "Ensure this value has at most 254 characters (it has 256)."
            ]
        )

    def test_password_length_input(self):
        # Arrange
        wrong_input = 26*'xo'
        # Act
        result = UserUpdateForm(data={"password" : wrong_input})
        # Assert
        self.assertFalse(result.is_valid())
        self.assertNotEqual(len(result.errors["password"]), 0 )
        self.assertEqual(
            result.errors["password"], 
            [ 
                "Ensure this value has at most 50 characters (it has 52)."
            ]
        )

    def test_correct_model(self):
        # Arrange
        expected_model = User
        # Act
        model = UserUpdateForm.Meta.model
        # Assert
        self.assertEqual(model, expected_model)

#URL
class UrlsTest(TestCase):


    def test_correct_view_assigned_user_list(self):
        # Arrange
        expected_user_list = 'user-list'
        # Act
        user_list = resolve(reverse('user-list'))
        # Assert
        self.assertEqual(user_list.view_name, expected_user_list)
        
    def test_correct_view_assigned_task_list(self):
        # Arrange
        expected_task_list = 'task-list'
        # Act
        task_list = resolve(reverse('task-list'))
        # Assert
        self.assertEqual(task_list.view_name, expected_task_list)

    def test_correct_view_assigned_user_create(self):
        # Arrange
        expected_user_create = 'user-create'
        # Act
        user_create = resolve(reverse('user-create'))
        # Assert
        self.assertEqual(user_create.view_name, expected_user_create)

    def test_correct_view_assigned_task_create(self):
        # Arrange
        expected_task_create = 'task-create'
        # Act
        task_create = resolve(reverse('task-create'))
        # Assert
        self.assertEqual(task_create.view_name, expected_task_create)

    def test_correct_view_assigned_user_update(self):
        # Arrange
        expected_task_create = 'user-update'
        # Act
        task_create = resolve(reverse('user-update', args=[1]))
        # Assert
        self.assertEqual(task_create.view_name, expected_task_create)

    def test_correct_view_assigned_task_update(self):
        # Arrange
        expected_task_create = 'task-update'
        # Act
        task_create = resolve(reverse('task-update', args=[1]))
        # Assert
        self.assertEqual(task_create.view_name, expected_task_create)

    def test_correct_view_assigned_user_delete(self):
        # Arrange
        expected_task_create = 'user-delete'
        # Act
        task_create = resolve(reverse('user-delete', args=[1]))
        # Assert
        self.assertEqual(task_create.view_name, expected_task_create)

    def test_correct_view_assigned_task_delete(self):
        # Arrange
        expected_task_create = 'task-delete'
        # Act
        task_create = resolve(reverse('task-delete', args=[1]))
        # Assert
        self.assertEqual(task_create.view_name, expected_task_create)