#coding:utf-8
from django.db import models
from django.contrib.auth.models import User
class ordinaryUser(models.Model):
    user=models.OneToOneField(User)
    SEX_CHOICES=(
            ('1',u'男'),
            ('2',u'女'),
            )
    nickname=models.CharField(u'昵称',max_length=30)
    sex=models.CharField(u'性别',max_length=1,choices=SEX_CHOICES,default='1')
    address=models.CharField(u'地址',max_length=100,null=True)
    img=models.ImageField(u'头像',upload_to="ordinaryUser",max_length=100)

    def __unicode__(self):
        return "%s%s%s" %(self.nickname,self.address,self.img)


