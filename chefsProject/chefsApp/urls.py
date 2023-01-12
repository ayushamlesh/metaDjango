from django.urls import path
from . import views
urlpatterns = [
    path('', views.home),
]
# Now we need to configure url
# at project level because project does not now where the view file is present
