from django.db import models


class OrderedModel(models.Model):
    def save(self, *args, **kwargs):
        ChildModel = self._meta.model
        different_items = ChildModel.objects.filter(position=self.position).exclude(
            pk=self.pk
        )
        super().save(*args, **kwargs)

        for item in different_items:
            reserved_postions = ChildModel.objects.values_list(
                "position", flat=True
            ).distinct()
            reserved_max = max(reserved_postions)
            unreserved_position = min(
                [i for i in range(0, reserved_max) if i not in reserved_postions]
                or [reserved_max + 1]
            )
            item.position = unreserved_position
            item.save()

    class Meta:
        abstract = True
