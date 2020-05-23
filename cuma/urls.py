
from django.urls import path, include
from django.contrib import admin
from django.views.generic import TemplateView

from cuma.api.views import SimpleApiView


"""
    lolstat.urls
        - path('cuma/', include('cuma.urls', namespace='cuma')),
"""
app_name = "cuma"
urlpatterns = [
    path('', SimpleApiView.as_view()),
]
