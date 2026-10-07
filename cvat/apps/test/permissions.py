# Copyright (C) CVAT.ai Corporation
#
# SPDX-License-Identifier: MIT

from cvat.apps.engine.permissions import TaskPermission


class StatsPermission(TaskPermission):
    @classmethod
    def get_scopes(cls, request, view, obj):
        if view.action == "class_counts" and request.method == "GET":
            return [cls.Scopes.VIEW_ANNOTATIONS]
        return super().get_scopes(request, view, obj)
