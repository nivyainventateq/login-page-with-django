from django.urls import path,include
from  login.views import me

urlpatterns = [
    path('site/', view=me, name='me'),
]


