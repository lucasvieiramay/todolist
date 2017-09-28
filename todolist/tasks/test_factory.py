import factory
from builtins import object
from tasks.models import Tasks


class TaskFactory(factory.django.DjangoModelFactory):
    class Meta(object):
        model = Tasks

    title = factory.Sequence((lambda n: "title%03d" % n))
