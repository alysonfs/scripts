import os
import sys

if len(sys.argv) > 1:
  # Se o primeiro argumento for -h ou --help exibir a ajuda
  if(sys.argv[1] == "-h" or sys.argv[1] == "--help"):
      print("bclean help")
      sys.exit(0)
  # Se o primeiro argumento for -v ou --version exibir a versão
  if(sys.argv[1] == "-v" or sys.argv[1] == "--version"):
      print("bclean version 1.0.0")
      sys.exit(0)
  # Se o primeiro argumento for c ou -c capturar o segundo argumento com objetivo de fazer um checkout para a branch informada
  if(sys.argv[1] == "c" or sys.argv[1] == "-c"):
      if len(sys.argv) == 3:
          cmd = "git checkout " + sys.argv[2]
          shellcmd = os.popen(cmd)
          sys.exit(0)
      else:
          print("bclean: missing branch name")
          sys.exit(-1)

cmd = "git branch --list | egrep --invert-match \"(main|\*)\" | xargs git branch -d"
shellcmd = os.popen(cmd)

print(shellcmd.read())
sys.exit(0)