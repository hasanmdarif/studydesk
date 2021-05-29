from django.db import models

class ContactUs(models.Model):

    name = models.CharField(max_length=200, null=False)
    phone = models.CharField(max_length=200, null=False)
    subject = models.CharField(max_length=200, null=False, default="")
    email = models.EmailField(max_length=200, null=False)
    content = models.TextField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Contact Us"
        ordering = ('-created_at',)






