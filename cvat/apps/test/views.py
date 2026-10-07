# Copyright (C) CVAT.ai Corporation
#
# SPDX-License-Identifier: MIT

from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from cvat.apps.engine.models import Task

from .permissions import StatsPermission
from .services import get_task_class_counts


class TaskStatsViewSet(viewsets.GenericViewSet):
    queryset = Task.objects.all()
    iam_permission_class = StatsPermission
    filter_backends = []

    @action(detail=True, methods=["GET"], url_path="class-counts")
    def class_counts(self, request, pk=None):
        task = self.get_object()
        data = get_task_class_counts(task)
        return Response(data, status=status.HTTP_200_OK)
