from django.shortcuts import render
from django.http import HttpResponse
from cmdb1.models import department1 as v1
from cmdb1.utils.processor import processor
# Create your views here.


def index(request):
    return render(request,"index.html")


def department1(request):
    # 首先拿取主库,做个字典雏形
    sqlStatus = {}
    masterList = v1.objects.filter(type = 1)
    for master in masterList:
        sqlStatus[master.ip+":"+str(master.port)] = {}
    # 拿取从库开始查询
    slaveList = v1.objects.filter(type = 2)
    for slave in slaveList:
        queryStatus = processor.loop(slave.ip,slave.port,slave.username,slave.password)
        sqlStatus[queryStatus['Master_Host'] + ":" + str(queryStatus['Master_Port'])][slave.ip +":"+str(slave.port)] = queryStatus
    masterLen = len(masterList)
    slaveLen = len(slaveList)
    msg = "总共 "+str(masterLen)+" 台主库  "+str(slaveLen)+" 台从库."
    return render(request, "department1.html",{'sqlStatus':sqlStatus,'msg':msg})