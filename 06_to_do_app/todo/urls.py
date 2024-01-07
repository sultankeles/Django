from django.urls import path, include

from .views import todo_list_create, todo_view_update_delete, Todos, Todo_Detail, TodoMVS

from rest_framework import routers


router = routers.DefaultRouter()
router.register("todo_mvs", TodoMVS)


urlpatterns = [
    path('todos/', todo_list_create),
    path('todo/<int:id>/', todo_view_update_delete),


    path("todos_list_create/", Todos.as_view()),
    path("todo_view_update_delete/<int:pk>/", Todo_Detail.as_view()),


    path("", include(router.urls))

]
#   + router.urls