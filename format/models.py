from django.db import models
from .validaters import validate_file_extension
class samme(models.Model):
    char=models.CharField(max_length=150)
    mod=models.FileField(upload_to="documents/",validators=[validate_file_extension])
