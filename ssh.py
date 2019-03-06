import paramiko
import getpass
import threading

def remote_conn(host,pwd,command,user):
	ssh = paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	ssh.connect(hostname=host,username=user,password=pwd)
	stdin ,stdout,stderr = ssh.exec_command(command)
	
	out = stdout.read()
	error=stderr.read()
	
	if out:
		print("[%s] OUT:>\n%s" % (host,out.decode("utf-8")))
	if error:
		print("[%s] ERROR:>\n%s" % (host,error.decode("utf-8")))
	ssh.close()


if __name__ == "__main__":
	host = input("IP:> ")
	user = input("username:> (default:root)")
	if not user :
		user == "root"
	pwd = getpass.getpass("password:> ")
	print(user)
	while 1:
		comm = input("command:> ")
		if not comm :
			exit (1)
		remote_conn(host,pwd,comm,user)
	
