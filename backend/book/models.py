from django.db import models

from dvadmin.utils.models import CoreModel, table_prefix
# Create your models here.

class Book(CoreModel):
    book_no = models.CharField(max_length=24,unique=True, verbose_name='书籍编号', help_text="书籍编号")
    book_name = models.CharField(max_length=24,null=False, verbose_name='书籍名称', help_text="书籍名称")


    class Meta:
        db_table = table_prefix + "book"
        verbose_name = '书籍表'
        verbose_name_plural = verbose_name
        ordering = ('-create_datetime',)