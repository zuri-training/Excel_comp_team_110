from django.urls import path
from . import views

urlpatterns = [
    # path('workspace', views.workspace, name="workspace"),
    # path('community', views.community, name="community"),
    path('project', views.project, name="project"),
    path('', views.dashboard, name="dasboard"),
]