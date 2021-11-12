import subprocess
import multiprocessing
from sys import stdout
import platform

class launcher:
    def __init__(self, command="whoami", task_name="", is_background=True):
        self.command = command
        self.logfile = command.split()[0] + "log.txt"
        self.aplication = None
        self.task_name = task_name
        self.is_background = is_background

    def Execute(self):
        print('Executing command:\n' + self.command +"\n")

        process = subprocess.Popen(self.command, stdout=subprocess.PIPE,
                                    stderr=subprocess.STDOUT, universal_newlines=True, shell=True)
        
        if not self.is_background:
            out_line = ''
            while True:
                
                try:
                    out_line = process.stdout.readline()
                except:
                    out_line = '\n'

                if out_line == '' and process.poll() is not None:
                    break
                
                print(out_line)
                
        else :
            log = open(self.logfile, "w")
            out_line = ''
            while True:
                
                try:
                    out_line = process.stdout.readline() 
                except:
                    out_line = '\n'
                    
                if out_line == '' and process.poll() is not None:
                    break
                
                log.write(out_line)
            log.close()

    def launch(self):
        self.aplication=multiprocessing.Process(target=self.Execute)
        self.aplication.start()

    def stop(self):
        self.aplication.terminate()
        self.aplication.join()
        if platform.system() == "Windows":
            Execute("taskkill /F /IM {}.exe".format(self.task_name), is_background = False)
        else:
            Execute("killall {}".format(self.task_name), is_background = False)


def Execute(command_list, is_background=False):
  
  print('Executing command:\n' + command_list +"\n")

  process = subprocess.Popen(command_list, stdout=subprocess.PIPE,
                             stderr=subprocess.STDOUT, universal_newlines=True)
  if not is_background:
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

