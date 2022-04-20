from django.urls import path

from todo.views import (
    TodoListView,
    TodoCreateView,
    TodoUpdateView,
    TodoDeleteView,
    todo_change_button,
    TagListView,
    TagCreateView,
    TagUpdateView,
    TagDeleteView,
)

urlpatterns = [
    path("", TodoListView.as_view(), name="todo-list"),
    path("todo/create", TodoCreateView.as_view(), name="todo-create"),
    path("todo/<int:pk>/update", TodoUpdateView.as_view(), name="todo-update"),
    path("todo/<int:pk>/delete", TodoDeleteView.as_view(), name="todo-delete"),
    path("todo/<int:pk>/change", todo_change_button, name="todo-change-button"),
    path("tag_list/", TagListView.as_view(), name="tag-list"),
    path("tag_list/create/", TagCreateView.as_view(), name="tag-create"),
    path("tag_list/<int:pk>/update", TagUpdateView.as_view(), name="tag-update"),
    path("tag_list/<int:pk>/delete", TagDeleteView.as_view(), name="tag-delete"),
]

app_name = "todo"
