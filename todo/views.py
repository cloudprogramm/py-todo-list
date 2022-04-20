from django.shortcuts import render
from django.urls import reverse_lazy

from todo.models import Task, Tag
from django.views import generic


class TodoListView(generic.ListView):
    model = Task
    context_object_name = "todo_list"
    template_name = "todo/index.html"

    ordering = ["task_completed"]


class TodoCreateView(generic.CreateView):
    model = Task
    fields = [
        "content",
        "deadline_time",
        "task_completed"
    ]
    success_url = reverse_lazy("todo:todo-list")


class TodoUpdateView(generic.UpdateView):
    model = Task
    fields = [
        "content",
        "deadline_time",
        "task_completed",
        "tags"
    ]
    success_url = reverse_lazy("todo:todo-list")


class TodoDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("todo:todo-list")
    template_name = "todo/todo_delete_confirmation.html"


def todo_change_button(request, pk):
    button = Task.objects.get(pk=pk)

    if button.task_completed:
        button.task_completed = False
    else:
        button.task_completed = True
    button.save()

    return redirect("todo:todo-list")


class TagListView(generic.ListView):
    model = Tag
    context_object_name = "tag_list"
    template_name = "todo/tag_list.html"


class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todo:tag-list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todo:tag-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("todo:tag-list")
    template_name = "todo/tag_delete_confirmation.html"
