import os
cmd = "git branch --list | egrep --invert-match \"(main|\*)\" | xargs git branch -d"

shellcmd = os.popen(cmd)

print(shellcmd.read())