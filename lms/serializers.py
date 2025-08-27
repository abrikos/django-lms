from rest_framework import serializers

from lms.models import Course, Lesson, Payment


class LessonSerializer(serializers.ModelSerializer):
    """Lesson serializer"""
    class Meta:
        model = Lesson
        fields = ['id', 'name', 'desc', 'image', 'url', 'course']


class CourseSerializer(serializers.ModelSerializer):
    """Course serializer"""
    lesson_count = serializers.SerializerMethodField()
    lessons = LessonSerializer(source='lesson_set', many=True, read_only=True )
    class Meta:
        model = Course
        fields = '__all__'

    def get_lesson_count(self, obj):
        return obj.lesson_set.count()

class PaymentSerializer(serializers.ModelSerializer):
    """Payment serializer"""
    class Meta:
        model = Payment
        fields = '__all__'

