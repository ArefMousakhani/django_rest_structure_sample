from django_rest_structure.api.serializers import BaseSerializer
from rest_framework import serializers
from django_rest_structure.api.validations import StrFieldValidation
from django_rest_structure.results.response import ResponseStructure
from django_rest_structure.requests.tools import get_client_ip

from core.exception import ResultMessages


def first_name_validation(value, **extra_params):
    return value.capitalize()


def last_name_validation(value, **extra_params):
    return value.capitalize()


class ProfileSerializer(BaseSerializer):
    first_name = serializers.CharField(validators=[StrFieldValidation(
        regex=r'^[A-Za-z]+$',
        error_message='just enter alphabet',
        extra_function=first_name_validation
    )])
    last_name = serializers.CharField(validators=[StrFieldValidation(
        regex=r'^[A-Za-z]+$',
        error_message='just enter alphabet',
        extra_function=last_name_validation
    )])

    age = serializers.IntegerField()

    def get_detail(self):
        response_data = {
            'request_id': self.request.request_uid,
            'ip_address': get_client_ip(self.request),
            'first_name': self.validated_data['first_name'],
            'last_name': self.validated_data['last_name'],
            'full_name': f"{self.validated_data['first_name']} {self.validated_data['last_name']}",
            'age': self.validated_data['age']
        }
        return ResponseStructure(ResultMessages.GET_SUCCESSFULLY, response_data)
