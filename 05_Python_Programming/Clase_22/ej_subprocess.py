import subprocess


#p = subprocess.run(["python.exe", "-V"], capture_output=True, encoding="cp850" )
#p = subprocess.run("hostname", capture_output=True, encoding="cp850" )

#p = subprocess.run(["ipconfig", "/all"], capture_output=True, encoding="cp850" )

p = subprocess.run(["dir", "pppp.txt"], capture_output=True, encoding="cp850", shell=True )

print("STDOUT:", p.stdout)
print("STDERR:", p.stderr)
print("RETCODE:", p.returncode)

