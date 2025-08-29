from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from lms.models import Course, Lesson
from users.models import User


class MyAPITest(APITestCase):
    def setUp(self):
        self.user = User.objects.create(email="admin@lms.ru")
        self.client.force_authenticate(self.user)

    def test_course_list(self):
        self.url = reverse("course-list")
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_lesson_list(self):
        self.url = reverse("lesson-list")
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_lesson_detail(self):
        model = Lesson(name="bob")
        model.save()
        response = self.client.get(reverse("lesson-detail", args=(model.pk,)))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_course_detail(self):
        course = Course(name="bob")
        course.save()
        response = self.client.get(reverse("course-detail", args=(course.pk,)))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_subscription(self):
        course = Course(name="bob")
        course.save()
        data = {"course_id": course.pk}
        response = self.client.post(reverse("subscription"), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
