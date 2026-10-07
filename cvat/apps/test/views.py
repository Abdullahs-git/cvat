# Copyright (C) CVAT.ai Corporation
#
# SPDX-License-Identifier: MIT

from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(["GET"])
def class_counts(request, task_id):
    return Response({
        "task_id": task_id,
        "total": 0,
        "classes": [],
    })

