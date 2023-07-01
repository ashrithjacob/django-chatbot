from django.db import models


class Document(models.Model):
    num_page = models.IntegerField(default=0)
    document = models.FileField(upload_to='uploads/')
    pub_date = models.DateTimeField("date published")

    def __str__(self) -> str:
        return self.document
