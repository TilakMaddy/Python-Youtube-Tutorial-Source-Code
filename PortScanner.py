try:
	import socket
except ImportError :
	print " [!] WARNING : Unable to import requierd modules . Please update python libraries"

print "[*] Starting port scanner ..."
print "[*] Configuring settings  ..."

if (socket.socket(socket.AF_INET , socket.SOCK_STREAM)):
	socketScanner = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
	print "[*] Scanner started successfully\n"

ip = raw_input("Enter the IP address to scan	: ")
scanType = raw_input("\nHow to do you want to scan the ports ?\n\n 1) Enter a custom port to scan\n 2) Enter the range of ports \n\nChoose option number	: ")
	
if(scanType is "1"):
	print "\n[*] Chose to scan a custom port"
	print "[*] Verifying options ...\n"
	customPort = input("Enter the port number	: ")
	if(socketScanner.connect_ex((ip , customPort))):
		print "Port " , customPort , "is open "
	else:
		print "Port ", customPort , "is closed "
elif(scanType is "2"):
	print "\n[*] Chose to scan a range of ports"
	print "[*] Verifying options ...\n"
	rangeStart = input("Enter the range \nStarting port number	: ")
	rangeFinish = input("Ending port number	: ")	
	print "\n[*] Starting scan ..."
	for i in range(rangeStart , rangeFinish):
		if(socketScanner.connect_ex((ip , i))):
			print "Port " , i , "is open "
		else:
			print "Port ", i  , "is closed "	
else:
	print "\n[-] Choose a valid option "
