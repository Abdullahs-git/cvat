# Copyright (C) CVAT.ai Corporation
#
# SPDX-License-Identifier: MIT

from django.db.models import Count, Q

from cvat.apps.engine.models import Label, Task


def get_task_class_counts(task: Task) -> dict:
    labels = Label.objects.filter(
        Q(task=task) | Q(project=task.project_id), parent__isnull=True
    ).annotate(
        shapes_count=Count(
            "labeledshape",
            filter=Q(labeledshape__job__segment__task=task) & Q(labeledshape__parent__isnull=True),
            distinct=True,
        ),
        images_count=Count(
            "labeledimage", filter=Q(labeledimage__job__segment__task=task), distinct=True
        ),
        tracks_count=Count(
            "labeledtrack",
            filter=Q(labeledtrack__job__segment__task=task) & Q(labeledtrack__parent__isnull=True),
            distinct=True,
        ),
    )

    results = []
    total = 0
    for label in labels:
        count = label.shapes_count + label.images_count + label.tracks_count
        total += count
        results.append(
            {"label_id": label.id, "name": label.name, "color": label.color, "count": count}
        )

    results.sort(key=lambda x: (-x["count"], x["name"]))

    return {"task_id": task.id, "total": total, "classes": results}
