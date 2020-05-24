from django.db import models


class ShortLink(models.Model):
    link = models.URLField()
    short_link = models.CharField(max_length=20, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.link
