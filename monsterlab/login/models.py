#coding:utf-8
from django.db import models


# Create your models here.
class FindPassword(models.Model):
    username=models.CharField(max_length=20)
    activetion_key=models.CharField(max_length=20)
    data=models.DateField(auto_now_add=True)

#class ordinaryUser(models.Model):
#    user=models.OneToOne(User)
#    nickname=models.CharField(u'',max_length=30)
#    sex=models.CharField(u'',max_length=1,choices=SEX_CHOICES,default='1')
#    address=models.CharFiled(u'',max_length=100,null=True)
#    img=models.ImageField(u'',)
#    def __unicode__(self):
#        return "%s%s" %(self.nickname,self.address)
