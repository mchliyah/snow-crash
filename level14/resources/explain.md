
# Level14 - Reverse Engineering with Ghidra

## Observation

the level contain nothing no files or binary .

but sense we have used the reverse engineering tool Ghidra in previous levels we thought that we can use it here too and there no binary left other then getflag itselfe.

*belive me you wont think about it at first haha*

exploiting it sayse "you should not reverse this you should not reverse this", we did it anyway

---

## Steps to Solve
as the prev level we copy the binary and will use Ghidra to reverse the binary.

### Step 1: Transfer the Binary
1. From the VM, transfer the `getflag` binary to local machine for analysis.
   ```bash
   scp level1r@<VM_IP>:/bin/getflag ./getflag
   ```

### Step 2: Open Ghidra

1. Launch Ghidra on your local machine.
2. Create a new project "Level14".
3. Import the `getflag` binary into the project.

### Step 3: Analyze the Binary
1. Ghidra will prompt you to analyze the binary. Click "Yes".
2. Select appropriate options to perform the analysis we keep the default options.

### Step 4: Locate the Functions needed
1. Navigate to the `main` function and inspect the logic.
3. We can see that the program is checking for a hexa string and if it matches it will call the `ft_des()`  to get the flag print the flag.
2. create a file.c and coppy the string ppassed to `ft_des()` when the check matches the hex `0xBC6` which is the `3014`.
3. ofc we are using the code craeted in the level13 to resolve the the flag.

### Step 5: Recompile the code and Extract the Flag

The `ft_des()` function contains logic that computes the flag.
