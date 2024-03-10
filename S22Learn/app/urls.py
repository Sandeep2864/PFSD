from django.urls import path
from .views import *

urlpatterns = [
    path('home', homepage, name="home"),
    path('login/',login,name="login"),
    path('signup/',signup,name="signup"),
    path('reg/',registration,name="registration"),
    path('', add_student, name="add"),
    path('view', view_students, name="view"),
    path('dashboard/apply', apply,name="apply"),
    path('dashboard/practice',practice,name="practice"),
    path('dashboard/profile',profile,name="profile"),
    path('dashboard/jobs',jobs,name="jobs"),
]
