from django.test import TestCase
from django.contrib.auth import get_user_model
from core import models


def sample_user(email='amit@gmail.com', password='aries'):
    return get_user_model().objects.create_user(email, password)

class ModelTests(TestCase):

    def test_create_user_with_email_sucessfully(self):

        email = "amit@gmail.com"
        password = "Singh@922"

        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email,email)
        self.assertTrue(user.check_password(password))\

    def test_new_email_normalized(self):
        email ="kumarsingh922@Gmail.com"
        user = get_user_model().objects.create_user(email , "amit1234")

        self.assertEqual(user.email , email.lower())    

    def test_new_user_invalid_email(self):
        with self.assertRaises(ValueError):
           get_user_model().objects.create_user(None , "amit1234")

    def test_superuser(self):
        user = get_user_model().objects.create_superuser(
            email = "kumarsingha922@gmail.com",
            password = "amit1234"
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_tag_str(self):
        tag = models.Tag.objects.create(
            user=sample_user(),
            name='vegan'
        )

        self.assertEqual(str(tag), tag.name)

    def test_ingredients_str(self):
        ingredient = models.Ingredient.objects.create(
            user=sample_user(),
            name='fish'
        )

        self.assertEqual(str(ingredient), ingredient.name)
