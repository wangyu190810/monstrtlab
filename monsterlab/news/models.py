#-*-coding:utf-8-*-
from django.db import models

class News(models.Model):

    title=models.CharField(max_length=200,verbose_name=u'标题')
    author=models.CharField(default="monster",max_length=100,verbose_name=u'作者')
    #	url=models.SlugField(max_length=100,verbose_name=u'Slug')
    count_hit=models.IntegerField(default=0,editable=False,verbose_name=u'点击数')
    img=models.ImageField('img',upload_to="img",max_length=100)
    content=models.TextField(verbose_name=u'内容')
    time=models.DateTimeField(u'编辑时间',auto_now=True)
    filedown=models.FileField(u'上传附件',upload_to='file',max_length=100)



    def __unicdoe__(self):
		return u'%s' %self.title

    def get_absolute_url(self):

		return u'news%s' %self.url


    class Meta:
		ordering=['-id']
		verbose_name_plural=verbose_name=u'文章'


# Create your models here.
