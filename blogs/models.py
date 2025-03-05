from django.db import models
from common.models import CommonModel

# Create your models here.


class Blog(CommonModel):
    title = models.CharField(
        max_length=100,
    )

    blog_contents = models.TextField()

    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "블로그 글"
