import pika
import json

from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer, ValidationError
from rest_framework_simplejwt.state import token_backend
from uuid import uuid4


class UserSerializer(ModelSerializer):
    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        user.is_active = False
        user.save()
        token = token_backend.encode({"unique": uuid4().hex, "uid": user.id})
        text = f'Subject: Account confirmation\n\n' \
               f'Please confirm your account by clicking this link: http://localhost:8001/auth/confirm?token={token}'
        print(text)
        data = json.dumps({'recipient': user.email, 'text': text})
        params = pika.ConnectionParameters('mq', 5672, '/', pika.PlainCredentials('user', 'user'))
        connection = pika.BlockingConnection(params)
        channel = connection.channel()
        channel.queue_declare(queue='hello')
        channel.basic_publish(exchange='', routing_key='hello', body=data)
        return user

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        extra_kwargs = {'email': {'required': True}}
