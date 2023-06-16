## ROOTMe

Nmap to scan de Machine and see the ports

To scan Nmap ports on a  remote system, enter the following in the terminal:

	sudo nmap 192.168.X.X
	
	mkdir rootme
	mkdir nmap
	
    nmap -sC -sV -oN nmap/rootme <MACHINE_IP>

    -sC : Default scripts
    -sV : Version detection
    -oN : Output to be stored in the directory ‘nmap’ you created earlier
    

###Gobuster

Gobuster is a tool used to brute-force:    	