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
        group_by = request.query_params.get("group_by")
        shape_type = request.query_params.get("shape_type")
        job_id_param = request.query_params.get("job_id")
        job_id = int(job_id_param) if job_id_param and job_id_param.isdigit() else None

        data = get_task_class_counts(
            task=task,
            group_by=group_by,
            shape_type=shape_type,
            job_id=job_id,
        )
        return Response(data, status=status.HTTP_200_OK)
