from django.db import models


class Todo(models.Model):
    class Meta:
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"

    title = models.CharField(max_length=255, verbose_name="Имя", unique=True)
    description = models.TextField(verbose_name="Описание")

    def __str__(self):
        return self.title
