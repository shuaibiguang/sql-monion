from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField('姓名',max_length=64)
    age = models.SmallIntegerField('年龄')
    choices = (
        (1,'男'),
        (2,'女'),
        (3,'未知')
    )

    sex = models.SmallIntegerField('性别', choices=choices)

class department1(models.Model):
    ip = models.GenericIPAddressField()
    typeTu = (
        (1,'主库'),
        (2,'从库')
    )
    type = models.SmallIntegerField('数据库类型', choices=typeTu)
    username = models.CharField('账号',max_length=64)
    password = models.CharField('密码',max_length=64)
    port = models.IntegerField('端口号')
    master_ip = models.GenericIPAddressField(default='',null=True,blank=True)
    master_port = models.IntegerField('主库端口号',null=True,blank=True)

    def __str__(self):

        if self.type == 1:
            temp_type = "MASTER"
        else:
            temp_type = 'SLAVE'
        return self.ip + " : "+str(self.port) + " ------> " + temp_type

    class Mate:
        abstract = True
        verbose_name = "事业部-1数据表"
        verbose_name_plural = verbose_name