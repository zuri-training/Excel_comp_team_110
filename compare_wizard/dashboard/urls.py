from django.urls import path
from . import views
from .views import new_project

urlpatterns = [
    # path('workspace', views.workspace, name="workspace"),
    # path('community', views.community, name="community"),
    path('project', views.project, name="project"),
    path('new_project/use_arg/', new_project, name='new_project'),
    path('', views.dashboard, name="dashboard"),
]