from django.db import models


class ShortLink(models.Model):
    link = models.URLField()
    short_link = models.URLField(blank=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.link
