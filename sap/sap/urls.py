
from django.contrib import admin
from django.urls import path

from people.views import personDetail, newPerson, editPerson, deletePerson
from webapp.views import  welcome

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('welcome/', welcome)
    path('', welcome, name = 'start'),
    path('person_detail/<int:id>', personDetail),
    path('new_person', newPerson),
    path('edit_person/<int:id>', editPerson),
    path('delete_person/<int:id>', deletePerson)
]
