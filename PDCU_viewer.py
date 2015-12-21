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

pdc = xlwt.Workbook()
plsi=rlsi=vlsi = 6


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

        plctable = pdc.add_sheet('Port Configuration')
        plcsingle = re.findall(r'0x\w.*?U\S*',self.ConData)
        plci,plcj = 5,0
        for plcstr in plcsingle:
            plc = plcstr.split(",")
            plclen = len(plc)
            for plcj in range(0,plclen):
                plctable.write(plci,plcj,(plc[plcj]))
            plci = plci + 1
        pdc.save('/tmp/log.xls')



        rlctable = pdc.add_sheet('Rank Configuration')
        rlcsingle = re.findall(r'\s0x\w{1,4}\,0x\w\S*',self.ConData)
        rlci, rlcj = 5, 0
        for rlcstr in rlcsingle:
            rlc = rlcstr.split(",")
            rlclen = len(rlc)
            for rlcj in range(0,rlclen):

                rlctable.write(rlci,rlcj,(rlc[rlcj]))
            rlci = rlci + 1
        pdc.save('/tmp/log.xls')



        vlctable = pdc.add_sheet('Volume Configuration')
        vlcsingle = re.findall(r'0x\w.*?\,IBM\S*',self.ConData)
        vlci,vlcj = 5,0
        for vlcstr in vlcsingle:
            vlc = vlcstr.split(",")
            vlclen = len(vlc)
            for vlcj in range(0,vlclen):
                vlctable.write(vlci,vlcj,(vlc[vlcj]))
            vlci = vlci + 1
        pdc.save('/tmp/log.xls')

    def get_time(self,data_cut):
        #pds = xlwt.Workbook()

        plsstart = re.findall(r'Interval Start\:\s*(\S*\s*\S*',self.data_cut)[0]
        plsend = re.findall(r'Interval End\:\s*(\S*\s*\S*',self.data_cut)[0]
        plength = re.findall(r'Interval Length:\s*(\d*)',self.data_cut)[0]

    def get_pls(self,PLScut,plsi):

        #plstable = pdc.add_sheet('Port Statistics')
        singlepls = re.findall(r'(0x.*\d)',PLScut)

        for splstr in singlepls:
            plsj = 6
            spls = splstr.split(",")
            for pi in range(0,len(spls)):
                plstable.write(plsi,plsj+pi,spls[pi])
            plsi = plsi+1

        pdc.save('/tmp/log.xls')
        return plsi


    def get_rls(self,RLScut,rlsi):
        #rlstable = pdc.add_sheet('Rank Statistics')
        singlerls = re.findall(r'(0x.*\d)',RLScut)

        for srplstr in singlerls:
            rlsj = 6
            srls = srplstr.split(",")
            for ri in range(0,len(srls)):
                rlstable.write(rlsi,rlsj+rj,srls[ri])
            rlsi = rlsi+1
        pdc.save('/tmp/log.xls')
        return  rlsi


















logdata = Logpost(logfile)
logdata.get_PDC()
print logdata.PDC_cut
logdata.get_statistics()
logdata.creatxls()

plstable = pdc.add_sheet('Port Statistics')
for PLSCUT in logdata.PLS_cut:

    plsi = logdata.get_pls(PLSCUT,plsi)

rlstable = pdc.add_sheet('Rank Statistics')
for RLSCUT in logdata.RLS_cut:
    rlsi = logdata.get_rls(RLSCUT,rlsi)


