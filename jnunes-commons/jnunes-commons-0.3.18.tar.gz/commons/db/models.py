from django.db import models


class BaseModel(models.Model):
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    @classmethod
    def get_last_or_else(cls):
        last_object = cls.objects.last()
        if last_object is not None:
            return last_object
        else:
            return cls()

    @classmethod
    def get_max_id(cls):
        try:
            return cls.objects.latest('id').id
        except Exception as err:
            print(err)
            return None
