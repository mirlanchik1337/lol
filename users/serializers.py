import email

from allauth.account.adapter import get_adapter
from allauth.account.utils import setup_user_email
from rest_framework import serializers
from rest_auth.registration.serializers import RegisterSerializer
from allauth.account.adapter import DefaultAccountAdapter

class CustomRegisterSerializer(RegisterSerializer):
    email = serializers.EmailField(required=True)

    def get_cleaned_data(self):
        data_dict = super().get_cleaned_data()
        data_dict['email'] = self.validated_data.get('email', '')
        return data_dict

    def custom_signup(self, request, user):

        adapter = DefaultAccountAdapter()
        adapter.send_mail(request,email, "subject", "message", "from_email")
        adapter = get_adapter()
        adapter.send_mail(
            request,
            'Welcome',
            'email/body.txt',
            {'user': user},
        )
