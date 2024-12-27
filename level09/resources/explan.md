# Level 09 Vulnerability Exploit Documentation

## Overview
In Level 09, we encountered a binary file `level09` and a `token` file containing unreadable characters mixed with readable characters. The goal was to analyze the binary's behavior, identify its vulnerability, and use it to gain the necessary flag.

## Observations
1. **Binary Behavior:**
   - Running `./level09` accepts an input string and transforms it into a new string.
   - Example:
     ```
     ./level09 "aaa" -> "abc"
     ./level09 "111" -> "123"
     ```
   - The transformation adds the position index of each character to its ASCII value.

2. **Token File:**
   - Using `cat token` reveals a mix of non-printable and readable characters.
   - Running `./level09 token` outputs the string `tpmhr`, indicating some processing based on the input.

3. **Behavior Analysis:**
   - After analyzing the behavior, we inferred that the binary applies a specific transformation on the input string. Each character in the input string is shifted by its position index (e.g., first character +0, second character +1, etc.).

## Exploitation Steps
### Reverse the Transformation
To reverse the binary's transformation, a custom Python script was created to decrypt the `token` and extract the original string.

#### Python Script: `reverse.py`
you can use the reverse.py asociated file to decrypt the token

### Steps to Exploit
1. **Analyze the Token:**
   - Decrypt the contents of the `token` file using the custom script:
     ```
     python /tmp/reverse.py $(cat token)
     ```
   - The decrypted output gives the original code.

2. **Switch User:**
    the decrypted code is the password to switch user 

   - Use the decrypted code to switch to the `flag09` user:
     ```
     su flag09
     ```

3. **Retrieve the Flag:**
   - Run the `getflag` command to retrieve the flag:
     ```
     getflag
     ```

### Example Output
```bash
level09@SnowCrash:~$ python /tmp/reverse.py $(cat token)
f3iji1ju5yuevaus41q1afiuq
level09@SnowCrash:~$ su flag09
Password: 
flag09@SnowCrash:~$ getflag
Check flag.Here is your token : xxxxxxxxxxxxxxxxx
```

## Conclusion
The vulnerability in the `level09` binary was its predictable transformation logic. By reversing the transformation using a custom script, we successfully extracted the required credentials to switch to the `flag09` user and retrieve the flag.
