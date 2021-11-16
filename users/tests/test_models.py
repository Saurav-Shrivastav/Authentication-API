from django.test import TestCase
from django.contrib.auth import get_user_model
from users import models


class ModelTests(TestCase):
    def test_create_user_with_email_successful(self):
        """Test creating a new user with an email is successful"""
        email = "test@gmail.com"
        password = "Testpass123"
        user = get_user_model().objects.create_user(email=email, name="Tester", password=password)

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test that the email for a new user is normalized"""
        email = "test@GMAIL.COM"
        user = get_user_model().objects.create_user(email, "Tester", "test123")

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Tests creating a new user with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, "Tester", "test123")

    def test_create_new_superuser(self):
        """Creating a new superuser"""
        user = get_user_model().objects.create_superuser("test@gmail.com", "Tester", "test123")

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
