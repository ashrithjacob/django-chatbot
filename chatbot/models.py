from django.db import models


class Document(models.Model):
    document = models.FileField(upload_to='uploads/')
    document_url = models.URLField(max_length=200)
    num_page = models.IntegerField(default=0)
    pub_date = models.DateTimeField("date published")

    #def __str__(self) -> str:
        #return self.document
