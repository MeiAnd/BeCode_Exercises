# Exercise Powershell CLI (Trial of Might)



Go to the webpage of the [Century game](https://underthewire.tech/century) and follow the instructions there

complete a maximum amount of levels and take note of the passwords for each one of them

    First level: century1@century.underthewire.tech
    Password: century1
    
    
Encrypt the collected passwords with GPG, upload them on Github with a minimalist readme and send me your public key.

Password with GPG;

[meilyn_andrade](meilyn_andrade.txt.gpg)

Installation:

	brew install gnupg
	
Steps	
	
	gpg --full-gen-key
	gpg --encrypt --recipient email@mail.com --output 	meilyn_andrade.gpg filex.txt
		

