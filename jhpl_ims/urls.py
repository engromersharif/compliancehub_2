from django.urls import path, reverse_lazy
from . import views

app_name = 'jhpl_ims'

urlpatterns = [

    path('', views.index.as_view(), name='index'),
    path('procedures/<int:pk>', views.procedures.as_view(), name='procedures'),
    path('master-list/<int:pk>/update',views.MasterUpdateView.as_view(success_url=reverse_lazy('jhpl_ims:index')), name='jhplmaster_update'),
    path('sop/<int:pk>/comment',views.NotesCreateView.as_view(), name='comment_create'),

]
