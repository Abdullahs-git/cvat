# Copyright (C) CVAT.ai Corporation
#
# SPDX-License-Identifier: MIT

from django.urls import include, path
from rest_framework import routers

from . import views

router = routers.DefaultRouter(trailing_slash=False)
router.register("annotation-stats/tasks", views.TaskStatsViewSet, basename="annotation-stats-tasks")

urlpatterns = [
    path("", include(router.urls)),
]
