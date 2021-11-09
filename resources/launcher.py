import subprocess
from sys import stdout

class launcher:

    def __init__(self, server_port="4723", server_ip="127.0.0.1", device_port="5554", device="Pixel_3_API_27"):
        #self.appium_command = f"appium -p {server_port} -a {server_ip} -pa /wb/hub -bp {device_port} --allow-cors -g appium_log.txt"
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

