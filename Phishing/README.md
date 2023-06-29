# Phishing Analysis 

## Mission

As a SOC analyst, you have to analyze the 5 emails that your colleagues send you. You must determine which email appears to be phishing and write a report. Your report should include all your thoughts and print screens of all the tools you used


	
```
**SOC Security Operation Center (SOC)** is a centralized function within an 
organization employing people, processes, and technology to continuously monitor 
and improve an organization's security posture while preventing, detecting, 
analyzing, and responding to cybersecurity incidents.
```

## Phishing Case

Your colleagues have provided you with emails in .eml format, ".eml" files are individual email files stored in Multipurpose Internet Mail Extensions (MIME) format. To scan .eml emails, you can use tools such as email clients (Outlook, Thunderbird, etc.), email viewing applications, or specialized tools such as email scanners.


### Email #1


* What is the email's timestamp?

		Mon, 20 Mar | 15:57:04.9879(UTC)
* Who is the email from?

		Service Paypal
* What is his email address?
		
		service@paypal.be
* What email address will receive a reply to this email?

		none
* What brand was this email tailored to impersonate?
	
		Spotify
	
* What is the originating IP? Defang the IP address.
	
		66[.]211[.]170[.]87
* What do you think will be a domain of interest? Defang the domain.

		www[.]paypal[.]be
		mx1[.]phx[.]paypal[.]com
		www[.]paypalobjects[.]com
	
* What is the shortened URL? Defang the URL.
	
		

* Do you think this is a phishing email?

		Yes, www[.]paypal[.]be is classified as Phishing

### Email #2


* What is the email's timestamp?

		12 Dec 2022 03:56:38 -0500

* Who is the email from?
	
		midnight magic events
	
* What is his email address?
		
		stainless@midnightmagicevents.com
* What email address will receive a reply to this email?

		 stainless@midnightmagicevents.com
* What brand was this email tailored to impersonate?
	
		Trust Wallet
	
* What is the originating IP? Defang the IP address.
	
		85[.][.]134[.]107
* What do you think will be a domain of interest? Defang the domain.
	
		www[.]midnightmagicevents[.]com
		vps37336[.]servconfig[.]com
		https[:]//climovil[.]com/		
	
* What is the shortened URL? Defang the URL.
	
		

* Do you think this is a phishing email?

		Surely because many links has been classified as malicious/phishing 
		on https://www.virustotal.com/
		
### Email #3


* What is the email's timestamp?
		
		Sun, 26 Mar 2023 13:31:56 +0000à
		
* Who is the email from?

		regruhosting[.]ru

* What is his email address?

		gq@80-78-255-128.cloudvps.regruhosting.ru
		
* What email address will receive a reply to this email?

		gq@80-78-255-128.cloudvps.regruhosting.ru
		 
* What brand was this email tailored to impersonate?
	
		Tinder
	
* What is the originating IP? Defang the IP address.
	
		80[.]78[.]255[.]128
		
* What do you think will be a domain of interest? Defang the domain.
	
		www[.]REGRUHOSTING[.]RU
		hxxp[:]//blog[.]tulingxueyuan[.]cn/
	
* What is the shortened URL? Defang the URL.
	
		

* Do you think this is a phishing email?

		I do!  
		for REGRUHOSTING[.]RU (4 security vendors flagged this domain as 		malicious)
		hxxp[:]//blog[.]tulingxueyuan[.]cn/. (14 security vendors flagged this 		URL as malicious)
		80-78-255-128[.]cloudvps[.]regruhosting[.]ru (Malicious/Malware/Phishing)
		

### Email #4


* What is the email's timestamp?
		
		Fri, 3 Mar 2023 12:44:01 +0100
		
* Who is the email from?

		Dr. Dan Miller

* What is his email address?

		babakingsouthmichael@gmail.com		
		
* What email address will receive a reply to this email?
 		
		imorourafiatou0@gmail.com
		Return-path babakingsouthmichael@gmail.com
		 
* What brand was this email tailored to impersonate?
	
		Disaster Risk Reduction (UNDRR)
		IMF
	
* What is the originating IP? Defang the IP address.
	
		209[.]85[.]220[.]41
				
* What do you think will be a domain of interest? Defang the domain.
	
		This is a plain/text email, But it's possible to have more information here  mrroberttaiwo212@gmail.com 
		( +229 ) 699 363 62 (Need to verify)
			
	
* What is the shortened URL? Defang the URL.
	
		

* Do you think this is a phishing email?

		yes, IP 209[.]85[.]220[.]41 classified as malicious by https://www.virustotal.com


### Email #5


* What is the email's timestamp?
		
		09:42 am, Aug 27th 2022
		
* Who is the email from?

		Ariana
		
* What is his email address?
	
		newsmail@app9l.serenitepure.fr
			
		
* What email address will receive a reply to this email?
 		
		Reply-To news@aichakandisha.com
		Return-Path return24F5o01l@arnhemophthalmics.com
		 
* What brand was this email tailored to impersonate?
	
		WhatsApp 
	
* What is the originating IP? Defang the IP address.
	
		51[.]83[.]34[.]109
				
* What do you think will be a domain of interest? Defang the domain.
	
		hxxp[:]//secure-netcloud[.]com/
			
	
* What is the shortened URL? Defang the URL.
	
		

* Do you think this is a phishing email?

		hxxp[:]//secure-netcloud[.]com/ (Phishing/ Suspicious) 		


