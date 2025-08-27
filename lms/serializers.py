from rest_framework import serializers

from lms.models import Course, Lesson, Payment, Subscription
from lms.validators import YoutubeValidator

class SubscriptionSerializer(serializers.ModelSerializer):
    """Subscription serializer"""
    class Meta:
        model = Subscription
        fields = '__all__'


class LessonSerializer(serializers.ModelSerializer):
    """Lesson serializer"""
    url = serializers.CharField(validators=[YoutubeValidator()])
    class Meta:
        model = Lesson
        fields = ['id', 'name', 'desc', 'image', 'url', 'course']


class CourseSerializer(serializers.ModelSerializer):
    """Course serializer"""
    lesson_count = serializers.SerializerMethodField()
    lessons = LessonSerializer(source='course_lessons', many=True, read_only=True )
    subscriptions = SubscriptionSerializer(source='course_subscriptions', many=True, read_only=True )
    iam_subscriber = serializers.SerializerMethodField()
    class Meta:
        model = Course
        fields = '__all__'

    def get_iam_subscriber(self, obj):
        request = self.context.get('request', None)
        if request.user in map(lambda x: x.user, obj.course_subscriptions.all()):
            return True
        return False

    def get_lesson_count(self, obj):
        return obj.course_lessons.count()

class PaymentSerializer(serializers.ModelSerializer):
    """Payment serializer"""
    class Meta:
        model = Payment
        fields = '__all__'

