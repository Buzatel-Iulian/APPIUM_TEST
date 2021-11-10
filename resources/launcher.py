import subprocess
import multiprocessing
from sys import stdout

class launcher2:
    def __init__(self, command="whoami", is_background=True):
        self.command = command
        self.name = command.split()[0]
        self.logfile = self.name + "_log.txt"
        self.aplication = None
        self.event = multiprocessing.Event()
        self.is_background = is_background

    def Execute(self):
        print('Executing command:\n' + ' '.join(self.command))

        process = subprocess.Popen(self.command, stdout=subprocess.PIPE,
                                    stderr=subprocess.STDOUT, universal_newlines=True, shell=True)
        if not self.is_background:
            out_line = ''
            while True:
                #print(6)
                try:
                    out_line = process.stdout.readline()      #    <<<   IT GETS STUCK HERE !!!
                    #print(2)
                except:
                    out_line = '\n'
                    #print(3)
                #print(4)
                if out_line == '' and process.poll() is not None:
                    break
                #print(5)
                stdout.write(out_line)
                stdout.flush()
                if self.event.is_set() :
                    self.StopProcess(process)
                    break
                #print(1)
        else :
            log = open(self.logfile, "w")
            out_line = ''
            while True:
                #print(6)
                try:
                    out_line = process.stdout.readline()      #    <<<   IT GETS STUCK HERE !!!
                    #print(2)
                except:
                    out_line = '\n'
                    #print(3)
                #print(4)
                if out_line == '' and process.poll() is not None:
                    break
                #print(5)
                log.write(out_line)
                ##stdout.write(out_line)
                ##stdout.flush()

                if self.event.is_set() :
                    self.StopProcess(process)
                    break
                #print(1)
            log.close()
        
        #return process

    def StopProcess (self, process):
        if process is not None:
            process.terminate()
            try:
                process.wait(3)
            except subprocess.TimeoutExpired:
                process.kill()

    def launch(self):
        self.aplication=multiprocessing.Process(name=self.name,target=self.Execute)
        self.aplication.start()

    def stop(self):
        self.event.set()
        self.aplication.join()

def Execute(command_list, is_background=False):
  
  print('Executing command:\n' + ' '.join(command_list))

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

class launcher:

    def __init__(self, server_port="4723", server_ip="127.0.0.1", device_port="5554", device="Pixel_3_API_27"):
        #self.appium_command = "appium -p 4723 -a 127.0.0.1 -pa /wb/hub -bp 5554 --allow-cors -g appium_log1.txt"
        self.appium_command = f"appium -p {server_port} -a {server_ip} -pa /wb/hub -bp {device_port} --allow-cors -g appium_log.txt"
        self.emulator_command = f"emulator -avd {device}"
        self.appium = None
        self.emulator = None

    def Execute(self, command, is_background=False):
  
        print('Executing command:\n' + ' '.join(command))

        process = subprocess.Popen(command, stdout=subprocess.PIPE,
                                    stderr=subprocess.STDOUT, universal_newlines=True, shell=True)
        if not is_background:
            out_line = ''
            while True:
                print(6)
                try:
                    out_line = process.stdout.readline()      #    <<<   IT GETS STUCK HERE !!!
                    print(2)
                except:
                    out_line = '\n'
                    print(3)
                print(4)
                if out_line == '' and process.poll() is not None:
                    break
                print(5)
                stdout.write(out_line)
                stdout.flush()
                print(1)
        
        return process

    def StopProcess (self, process):
        if process is not None:
            process.terminate()
            try:
                process.wait(3)
            except subprocess.TimeoutExpired:
                process.kill()

    def startEmulator (self):
        print("Starting Emulator")
        self.emulator = self.Execute(self.emulator_command, is_background = False)
        if self.emulator.stdout.readline() and self.emulator.poll() is None:
            print("Emulator is running\n")

    def startAppium (self):
        print("Starting Appium Server")
        self.appium = self.Execute(self.appium_command, is_background = True)    #  <<< NEEDS TO GET OUTPUT REDIRECTED
        if self.appium.stdout.readline() and self.appium.poll() is None:
            print("Appium is running\n")

    def stopEmulator (self):
        print("Turning Emulator Off")
        self.StopProcess(self.emulator)

    def stopAppium (self):
        print("Turning Appium Server Off")
        self.StopProcess(self.appium)

