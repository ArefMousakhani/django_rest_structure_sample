from django_rest_structure.results.exception import Err, ResultMessages
from django_rest_structure.results.codes import ResultMessageStructure
from rest_framework import status


class CustomResultMessages(ResultMessages):
    TEST_RESULT = ResultMessageStructure(10, 'this is my test error', False, status.HTTP_400_BAD_REQUEST)


class Ex(CustomResultMessages, Err):
    def __init__(self, *args, **kwargs):
        super(Ex, self).__init__(*args, **kwargs)
