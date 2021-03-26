from django.conf.urls import url
from . import views
from rest.quickstart.views import homePageView, SensorDetailView

app_name = 'quickstart'

urlpatterns = [
    # sensor detail view
    url('',SensorDetailView.as_view(), name='sensor-detail'),
]