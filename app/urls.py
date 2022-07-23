from django.urls import path
from .views import TaskList, TaskDetail, TaskCreate, TaskDelete, TaskUpdate
from .views import MyLoginView, RegisterPage
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', MyLoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(next_page="login"), name="logout"),
    
    path('register/', RegisterPage.as_view(), name='register'),


    path("", TaskList.as_view(), name="tasks"),
    path("<int:pk>/", TaskDetail.as_view(), name="task"),
    path('create/', TaskCreate.as_view(), name="create"),
    path('delete/<int:pk>/', TaskDelete.as_view(), name="delete"),
    path('update/<int:pk>', TaskUpdate.as_view(), name="update")
]