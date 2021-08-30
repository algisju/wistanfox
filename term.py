#/usr/bin/python3
import os,time,subprocess
# create custom pipe file
PIPE_PATH = "/tmp/my_pipe"
os.remove(PIPE_PATH) if os.path.exists(PIPE_PATH) else os.mkfifo(PIPE_PATH)
# open terminal that reads from your pipe file
a = subprocess.Popen(['xterm', '-e', 'tail --follow {0}'.format(PIPE_PATH)])
# write to file and it will be displayed in the terminal window
message = "some message to terminal\n"
with open(PIPE_PATH, "w") as p:
    p.write(message)
    p.write("Second Message...")
input("Press [Enter] to terminate PIPE > ")
# close the terminal
a.terminate()
