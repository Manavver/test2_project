


from django.urls import path
from .import views
urlpatterns = [

    path('actoress_list/',views.actoress_list),
    path('data_post2/',views.data_post2),
    path('update-data/<int:id>', views.update_data),

    path('do-update-data/<int:id>', views.do_update_data),

]
