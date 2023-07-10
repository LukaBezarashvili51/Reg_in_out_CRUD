from django.urls import path
from myapp.views import (
    RegisterView,
    LoginView,
    LogoutView,
    PostCreateView,
    PostDeleteView, UserListView,
    SomeView
)

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('create/', PostCreateView.as_view()),
    path('delete/<int:pk>/', PostDeleteView.as_view()),
    path('list/', UserListView.as_view()),
    path('login-status/', SomeView.as_view()),
]
