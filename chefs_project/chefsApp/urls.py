from django.urls import path
from . import views
urlpatterns = [
    path('b/', views.home),
    # path('', views.methods),
    path('', views.showform, name="showform"),
    path("getform/", views.getform, name='getform'),
]
# Now we need to configure url
# at project level because project does not now where the view file is present
