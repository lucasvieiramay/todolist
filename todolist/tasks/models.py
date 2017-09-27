from django.db import models


class BaseModel(models.Model):
    """
    Since in all modeling it is important to have these fields below,
    So I do not need to keep creating these fields in all models,
    Just inherit it.
    """

    date_created = models.DateTimeField(auto_now_add=True, null=True)
    last_updated = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        abstract = True


class Tasks(BaseModel):

    URGENT = 1
    MEDIUM = 2
    LIGHT = 3
    LABEL_CHOICES = (
        (URGENT, 'Urgent'),
        (MEDIUM, 'Medium'),
        (LIGHT, 'Light'),
    )

    title = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)
    # I need to specify the blank, if I will use django to handle the form
    # Ex: In Django Admin if the field is not blank, django don't let me save
    description = models.TextField(null=True, blank=True)
    deadline_date = models.DateField(null=True, blank=True)
    order_priority = models.PositiveIntegerField(
        default=None, null=True, blank=True)
    # To make it easier to understand and maintain I always use enums!
    label = models.PositiveSmallIntegerField(
        null=True, choices=LABEL_CHOICES, default=MEDIUM)
    # This will work like a SoftDelete
    archived = models.BooleanField(default=False)

    def is_urgent(self):
        return self.label == self.URGENT

    def is_medium(self):
        return self.label == self.MEDIUM

    def is_light(self):
        return self.label == self.LIGHT

    def __str__(self):
        return "[{}] {}".format(self.title, self.label)
