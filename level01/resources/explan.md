# Explanation for Level01
## Observations
1. while trying to solve the level00 i noticed a code in permission when we check the passwd file .
```
    $> cat /etc/passwd

    level13:x:2013:2013::/home/user/level13:/bin/bash
    level14:x:2014:2014::/home/user/level14:/bin/bash
    flag00:x:3000:3000::/home/flag/flag00:/bin/bash
    flag01:42hDRfypTqqnw:3001:3001::/home/flag/flag01:/bin/bash
    flag02:x:3002:3002::/home/flag/flag02:/bin/bash
    flag03:x:3003:3003::/home/flag/flag03:/bin/bash
    flag04:x:3004:3004::/home/flag/flag04:/bin/bash
 
```
## Steps to Solve
1. after search and testing we can decode the password using joh the ripper tool "42hDRfypTqqnw" gave  "abcdefg"
2. after that we can use the password to login to the system and get the flag01
```
level01@SnowCrash:~$ su flag01
Password: 
Don't forget to launch getflag !
flag01@SnowCrash:~$ getflag
Check flag.Here is your token : f2av5il02puano7naaf6adaaf
flag01@SnowCrash:~$ 
```



