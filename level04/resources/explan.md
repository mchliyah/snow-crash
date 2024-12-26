
# Explanation for Level04

## Observations
1. The `level04.pl` file is a Perl script that takes a parameter `x` from the URL query string and executes it using the `echo` command.
2. The script uses the following code to execute the user input:
   ```perl
   print \`echo \$y 2>&1\`;
   ```
3. This creates a **command injection vulnerability** where the user can inject arbitrary shell commands through the `x` parameter in the URL.
4. The server listens on port `4747` as shown in the `netstat` output.
5. The goal is to exploit this vulnerability and execute a command such as `getflag` to retrieve the flag.

## Steps to Solve
1. **Identify the Vulnerability**:
   - The script directly executes the value of the `x` parameter in a shell command without sanitizing input.
   - This allows for **command injection** where any shell command can be executed.
   
2. **Craft the Exploit**:
   - Inject a command via the URL query string to execute `getflag` or any other shell command.
   - For example, you can inject `getflag` by passing it in the `x` parameter:
     ```bash
     curl "http://10.14.59.196:4747/level04.pl?x=getflag"
     ```
   
3. **Alternative Injection**:
   - If the direct injection doesn't work due to URL encoding issues, try encoding the command or chaining it with `;` or `|`:
     ```bash
     curl "http://10.14.59.196:4747/level04.pl?x=test%3B%20getflag"
     ```
   - The `%3B` encodes the `;` character, allowing you to chain multiple commands.

4. **Verify the Output**:
   - If successful, the server will execute the injected command and return the flag or relevant output.
   - Example output:
     ```
     Check flag. Here is your token: qi0maab88jeaj46qoumi7maus
     ```

## Summary
- The script is vulnerable to **command injection** because it directly executes user-supplied input in a shell command.
- By injecting `getflag` or other shell commands, you can execute arbitrary commands as the user running the Perl script.
- The solution involves crafting a URL with the `x` parameter set to the desired command and observing the output.




