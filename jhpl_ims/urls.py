from django.urls import path
from . import views

app_name = 'jhpl_ims'

urlpatterns = [

    path('', views.index.as_view(), name='index'),
    path('sop_one', views.sop_one.as_view(), name='sop_one'),
    path('sop_two', views.sop_two.as_view(), name='sop_two'),
    path('sop_three', views.sop_three.as_view(), name='sop_three'),
    path('sop_four', views.sop_four.as_view(), name='sop_four'),
    path('sop_five', views.sop_five.as_view(), name='sop_five'),

]
