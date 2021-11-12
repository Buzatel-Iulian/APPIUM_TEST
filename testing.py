import multiprocessing
import os
from time import sleep
import subprocess
import platform


def worker(comm, d, key, value):
    #d[key] = value
    process = subprocess.Popen(comm, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True, shell=True)
    d[key] = process.pid
    out_line = ''
    while True:
        try:
            out_line = process.stdout.readline()
        except:
            out_line = '\n'
        if out_line == '' and process.poll() is not None:
            break
        #print(out_line)

def thething(d, command):
    #mgr = multiprocessing.Manager()
    #d = mgr.dict()
    #jobs = [ multiprocessing.Process(target=worker, args=(command, d, i, i*2))
    #         for i in range(1) 
    #         ]
    jobs = multiprocessing.Process(target=worker, args=(command, d, 3, 3*2))
    #for j in jobs:
    #    j.start()
    #for j in jobs:
    #    j.join()
    #print ('Results:', d)
    return jobs

def stopp(p, d):
    aux = d[3]
    if platform.system() == "Windows":
        os.system(f"taskkill /F /PID {aux}")
    else:
        os.system(f"kill -9 {aux}")
    #for j in p:
    p.terminate()
    p.join()
    print ('Results:', d)
    

def startt(p, d):
    #for j in p:
    p.start()
    sleep(1)
    print ('Results:', d)

if __name__ == '__main__':
    mgr = multiprocessing.Manager()
    d = mgr.dict()
    jbs = thething(d, "appium -p 4723 -a 127.0.0.1 -pa /wb/hub -bp 5554 --allow-cors")

    #start
    #for j in jbs:
    #    j.start()
    #    sleep(1)
    #print ('Results:', d)
    startt(jbs, d)
    wait = input()
    #stop
    #for j in jbs:
    #    j.terminate()
    #    j.join()
    #print ('Results:', d)
    stopp(jbs, d)
    