from django.db import models

# Create your models here.


class Test(models.Model):
    url = models.CharField(max_length=228, blank=True, null=True)
    img_url = models.CharField(max_length=228, blank=True, null=True)
    title = models.CharField(max_length=228, blank=True, null=True)
    content = models.CharField(max_length=228, blank=True, null=True)

    class Meta:
        db_table = 'test'
        verbose_name = "test表"

    def __unicode__(self):
        return self.id