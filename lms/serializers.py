from rest_framework import serializers

from lms.models import Course, Lesson


class CourseSerializer(serializers.ModelSerializer):
    """Course serializer"""
    class Meta:
        model = Course
        fields = ['id', 'name', 'desc', 'image']


class LessonSerializer(serializers.ModelSerializer):
    """Lesson serializer"""
    class Meta:
        model = Lesson
        fields = ['id', 'name', 'desc', 'image', 'url', 'course']
