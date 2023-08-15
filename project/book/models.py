from django.db import models
from django.contrib.auth.models import User
# Create your models here.


# 독서 후기
class readingList(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE,related_name="추천인")
    title = models.TextField(verbose_name="제목")
    report = models.TextField(verbose_name="후기")
    created_at = models.DateTimeField(auto_now_add=True,verbose_name="작성날짜")
    voter = models.ManyToManyField(User, related_name="good_report")
    img = models.ImageField(upload_to='reading_list_images/')