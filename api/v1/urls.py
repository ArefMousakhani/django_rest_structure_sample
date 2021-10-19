
from django.urls import path, include

from api.v1.views import ProfileView, TestExceptionView

urlpatterns = [
    path('profile/', ProfileView.as_view()),
    path('exception/', TestExceptionView.as_view()),

]
