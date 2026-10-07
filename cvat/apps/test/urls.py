# Copyright (C) CVAT.ai Corporation
#
# SPDX-License-Identifier: MIT

from django.urls import path

from . import views

urlpatterns = [
    path(
        "annotation-stats/tasks/<int:task_id>/class-counts",
        views.class_counts,
        name="class-counts",
    ),
]

