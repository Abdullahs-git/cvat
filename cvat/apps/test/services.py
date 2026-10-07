# Copyright (C) CVAT.ai Corporation
#
# SPDX-License-Identifier: MIT

from django.db.models import Count, Q

from cvat.apps.engine.models import Label, LabeledShape, Task


def get_task_class_counts(
    task: Task,
    group_by: str | None = None,
    shape_type: str | None = None,
    job_id: int | None = None,
) -> dict:
    shape_filter = Q(labeledshape__job__segment__task=task) & Q(
        labeledshape__parent__isnull=True
    )
    image_filter = Q(labeledimage__job__segment__task=task)
    track_filter = Q(labeledtrack__job__segment__task=task) & Q(
        labeledtrack__parent__isnull=True
    )

    if job_id:
        shape_filter &= Q(labeledshape__job_id=job_id)
        image_filter &= Q(labeledimage__job_id=job_id)
        track_filter &= Q(labeledtrack__job_id=job_id)

    if shape_type:
        shape_filter &= Q(labeledshape__type=shape_type)

    count_images = not shape_type
    count_tracks = not shape_type

    labels_qs = Label.objects.filter(
        Q(task=task) | Q(project=task.project_id), parent__isnull=True
    ).annotate(
        shapes_count=Count("labeledshape", filter=shape_filter, distinct=True),
        images_count=Count("labeledimage", filter=image_filter, distinct=True)
        if count_images
        else Count("id", filter=Q(id__isnull=True)),
        tracks_count=Count("labeledtrack", filter=track_filter, distinct=True)
        if count_tracks
        else Count("id", filter=Q(id__isnull=True)),
    )

    by_type_map = {}
    if group_by == "shape_type":
        shape_groups_filter = Q(job__segment__task=task, parent__isnull=True)
        if job_id:
            shape_groups_filter &= Q(job_id=job_id)
        if shape_type:
            shape_groups_filter &= Q(type=shape_type)

        shape_groups = (
            LabeledShape.objects.filter(shape_groups_filter)
            .values("label_id", "type")
            .annotate(cnt=Count("id"))
        )
        for sg in shape_groups:
            by_type_map.setdefault(sg["label_id"], {})[sg["type"]] = sg["cnt"]

    results = []
    total = 0
    for label in labels_qs:
        count = label.shapes_count + label.images_count + label.tracks_count
        total += count
        item = {
            "label_id": label.id,
            "name": label.name,
            "color": label.color,
            "count": count,
        }
        if group_by == "shape_type":
            item["by_shape_type"] = by_type_map.get(label.id, {})
        results.append(item)

    results.sort(key=lambda x: (-x["count"], x["name"]))

    data = {"task_id": task.id, "total": total, "classes": results}
    if group_by:
        data["group_by"] = group_by
    if shape_type:
        data["shape_type"] = shape_type
    if job_id:
        data["job_id"] = job_id
    return data
