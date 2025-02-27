from django.db import models
from common.models import CommonModel

# Create your models here.


class Note(CommonModel):
    text = models.CharField(
        max_length=200,
    )

    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
    )
