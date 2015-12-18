# -*- coding:utf-8 -*-

import xlrd
import xlwt
import re
import json
import struct

#read logfile
log = open('/tmp/test.txt','r')
logfile = log.read()
log.close()


class Logpost(object):

    def __init__(self,logfiles):
        self.logfile = logfiles

    def get_PDC(self):
        self.PDC_cut = re.findall(r'Performance Data Collection(.*?)\=\=\=\=\=',self.logfile,re.S)[0]
        self.ConData = re.findall(r'Configuration Data(.*?)\=\=\=\=\=',self.logfile,re.S)[0]

    def get_statistics(self):
        self.PLS_cut = re.findall(r'Port Level Statistics(.*?)Rank Level',self.logfile,re.S)
        self.RLS_cut = re.findall(r'Rank Level Statistics(.*?)Volume Level',self.logfile,re.S)
        self.VLS_cut = re.findall(r'Volume Level Statistics(.*?)\=\=\=\=\=',self.logfile,re.S)

    def creatxls(self):
        pdc = xlwt.Workbook()

        plctable = pdc.add_sheet('Port Configuration')
        plcsingle = re.findall(r'0x\w.*?U\S*',self.ConData)
        plci,plcj = 5,0
        for plcstr in plcsingle:
            plc = plcstr.split(",")
            plclen = len(plc)
            for plcj in range(0,plclen):
                plctable.write(plci,plcj,(plc[plcj]))
            plci = plci + 1
        pdc.save('/tmp/log1.xls')
        print('11111')


        rlctable = pdc.add_sheet('Rank Configuration')
        rlcsingle = re.findall(r'0x\w{1,4}\,0x\w\S*',self.ConData)
        rlci,rlcj = 5,0
        for rlcstr in rlcsingle:
            rlc = rlcstr.split(",")
            rlclen = len(rlc)
            for rlcj in range(0,rlclen):
                print(rlc[rlcj])
                rlctable.write(rlci,rlcj,(rlc[rlcj]))
            rlci = rlci + 1
        pdc.save('/tmp/log1.xls')
        print('22222')


        vlctable = pdc.add_sheet('Volume Configuration')
        vlcsingle = re.findall(r'0x\w.*?IBM\S*',self.ConData)
        vlci,vlcj = 5,0
        for vlcstr in vlcsingle:
            vlc = plcstr.split(",")
            vlclen = len(vlc)
            for vlcj in range(0,vlclen):
                vlctable.write(vlci,vlcj,(vlc[vlcj]))
            vlci = vlci + 1
        pdc.save('/tmp/log1.xls')
        print('33333')















logdata = Logpost(logfile)
logdata.get_PDC()
print logdata.PDC_cut
logdata.get_statistics()
logdata.creatxls()
for PLS in logdata.PLS_cut:
    #print PLS
    pass