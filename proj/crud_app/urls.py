from django.urls import path
from .views import Student_view, student_list_view, Student_update_view,student_delete

urlpatterns = [
    path('student/',Student_view.as_view(), name='student_urls'),
    path('show/',student_list_view.as_view(), name='show_urls'),
    path('update/<int:pk>/',Student_update_view.as_view(),name='update_urls'),
    path('delete/<int:pk>/',student_delete.as_view(),name='delete_urls')

]