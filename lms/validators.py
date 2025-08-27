from rest_framework import serializers


class YoutubeValidator:
    def __call__(self, value):
        if "youtube.com" not in value:
            raise serializers.ValidationError("The value must be an youtube link.")
