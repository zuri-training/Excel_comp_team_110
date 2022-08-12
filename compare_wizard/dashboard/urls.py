from django.urls import path
from . import views
from .views import new_project, del_fxn, down_fxn

urlpatterns = [
    # path('workspace', views.workspace, name="workspace"),
    # path('community', views.community, name="community"),
    path('project', views.project, name="project"),
    path('new_project', new_project, name='new_project'),
    path('', views.dashboard, name="dashboard"),
    path('del_fxn/?P<int:pj_id>', del_fxn, name='del_fxn'),
    path('down_fxn/?P<int:pj_id>', down_fxn, name='down_fxn')

]

# {% url 'down_fxn' i.project_name %}
# {% url 'del_fxn' i.id %}