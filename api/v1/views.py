from django_rest_structure.api.views import BaseApiView
from django_rest_structure.results.response import ResponseStructure

from api.v1.serializers import ProfileSerializer
from core.exception import ResultMessages, Ex


class ProfileView(BaseApiView):
    def post_method(self, request, *args, **kwargs):
        return ProfileSerializer(data=request.data, check_is_valid=True, request=request).get_detail()


class TestExceptionView(BaseApiView):
    def post_method(self, request, *args, **kwargs):
        raise Ex(Ex.TEST_RESULT)
