
# Level13 - Reverse Engineering with Ghidra

## Observation

the level contain a binary file called `level13` which is a 32-bit ELF executable.

```bash
level13@SnowCrash:~$ file level13
level13: setuid setgid ELF 32-bit LSB executable, Intel 80386, version 1 (SYSV), dynamically linked (uses shared libs), for GNU/Linux 2.6.24, BuildID[sha1]=0xde91cfbf70ca6632d7e4122f8210985dea778605, not stripped
```
executing it print a message saying that it expect a user uid

```bash 
$ ./level13
UID 2013 started us but we expect 4242
```

## Description

after some attempts to overpass the uid check, we can see that the program is using the `geteuid()`, after all we desided to go further and check the binary with Ghidra.

The Level13 binary checks the user's UID as a trick, but the main logic resides in a function called `ft_des()`, Which takes a string code as argument and returns the flag.

---

## Steps to Solve

### Step 1: Transfer the Binary
1. From the VM, transfer the `level13` binary to local machine for analysis.
   ```bash
   scp level13@<VM_IP>:~/level13 ./level13
   ```

### Step 2: Open Ghidra
1. Launch Ghidra on your local machine.
2. Create a new project "Level13".
3. Import the `level13` binary into the project.

### Step 3: Analyze the Binary
1. Ghidra will prompt you to analyze the binary. Click "Yes".
2. Select appropriate options to perform the analysis we keeep the default options.

### Step 4: Locate the Functions needed
1. Navigate to the `main` function and inspect the logic.
2. create a file.c and coppy the code from the main function elinminating the check part.
3. Find the `ft_des()` function called within the main logic coppy it.

### Step 5: Recompile the code and Extract the Flag

The `ft_des()` function contains logic that computes the flag.
