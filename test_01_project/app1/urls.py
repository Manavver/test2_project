


from django.urls import path             # Crud
from .import views
urlpatterns = [

    path('actor_list/',views.actor_list),   # read/retrieve
    path('data_post/',views.data_post),         #create
    path('delete/<int:id>', views.delete),
    #path('edit/<int:id>', views.edit),
    #path('RecordEdited/<int:id>', views.RecordEdited),
    path('update-std/<int:id>', views.update_std),        #update
    path('do-update-std/<int:id>', views.do_update_std), # ------
    path('testing/',views.testing),
    path('testing2/',views.testing2),
]
