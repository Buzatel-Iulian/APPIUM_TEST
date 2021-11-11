import subprocess
import multiprocessing
import os
import platform
from sys import stdout
from time import sleep

def Execute(command_list, is_background=False):
  
  print('Executing command:\n' + ' '.join(command_list))

  process = subprocess.Popen(command_list, stdout=subprocess.PIPE,
                             stderr=subprocess.STDOUT, universal_newlines=True, shell=True)
  if not is_background:
    print(f"PID : {process.pid}")
    out_line = ''
    while True:
      try:
        out_line = process.stdout.readline()
      except:
        out_line = '\n'
      if out_line == '' and process.poll() is not None:
        break
      stdout.write(out_line)
      stdout.flush()
  return process

class launcher:

    def __init__(self, server_port="4723", server_ip="127.0.0.1", device_port="5554", device="Pixel_3_API_27", startup_time=1, is_background=True):
        #self.command = "appium -p 4723 -a 127.0.0.1 -pa /wb/hub -bp 5554 --allow-cors -g appium_log1.txt"
        self.command = f"appium -p {server_port} -a {server_ip} -pa /wb/hub -bp {device_port} --allow-cors -g appium_log1.txt"
        self.name = self.command.split()[0]
        self.logfile = self.name + "_log2.txt"
        self.is_background = is_background
        self.startup_time = startup_time
        if self.is_background:
            self.log = open(self.logfile, "w")
        
        #self.aplication = multiprocessing.Process(name=self.name,target=self.Execute)
        self.aplication = self.makeProcess()

    def Execute(self):
        print('Executing command:\n' + ' '.join(self.command))

        process = subprocess.Popen(self.command, stdout=subprocess.PIPE,
                                    stderr=subprocess.STDOUT, universal_newlines=True, shell=True)

        out_line = ''
        while True:
            try:
                out_line = process.stdout.readline()
            except:
                out_line = '\n'
            
            if out_line == '' and process.poll() is not None:
                break
            
            if self.is_background:
                self.log.write(out_line)
            else:
                stdout.write(out_line)
                stdout.flush()
            

    def makeProcess (self):
        return  multiprocessing.Process(name=self.name,target=self.Execute)


    def start_s (self):
        print("Starting Appium Server")
        #self.aplication = multiprocessing.Process(name=self.name,target=self.Execute)
        self.aplication.start()
        sleep(self.startup_time)   # To start the aplication properly


    def stop_s (self):
        print("Turning Appium Server Off")
        
        if platform.system() == "Windows":
            Execute("taskkill /F /IM node.exe", is_background = False)
        else:
            Execute("killall node", is_background = False)

        self.aplication.terminate()
        self.aplication.join()

        if self.is_background:
            self.log.close()

