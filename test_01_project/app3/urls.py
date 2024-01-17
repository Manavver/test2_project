
from django.urls import path
from .import views
urlpatterns = [

    path('villian_list/',views.villian_list),
    path('data_post3/',views.data_post3,name='data_post'),
    path('update_villian/<int:id>', views.update_villian),
    path('do-update-villian/<int:id>', views.do_update_villian),


]