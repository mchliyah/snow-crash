# snow-crash


# Snow Crash Project

## Project Overview
The **Snow Crash** project involves solving a series of challenges by progressing through multiple levels on a virtual machine (VM). Each level requires identifying specific passwords to advance, using problem-solving skills and technical expertise. The project emphasizes precision, justification, and understanding of solutions.

## Level Structure
- Each level requires you to:
  1. Access the `flagXX` account using the password derived from the current level.
  2. Execute the `getflag` command to retrieve the token for the next level.
- Example session:
  ```
  level00@SnowCrash:~$ su flag00
  Password:
  flag00@SnowCrash:~$ getflag
  Check flag. Here is your token: XXXXXXXXXXXXXXXXXX
  flag00@SnowCrash:~$ su level01
  Password:
  level01@SnowCrash:~$
  ```
- The `flag` file can be empty, but its purpose and any supporting files in the `resources/` directory must be explained during evaluation.

## Key Guidelines
1. **Resource Usage:**
   - Use the `/tmp/` or `/var/tmp/` directories sparingly as they have restricted permissions and may reset periodically.
   - Work locally and avoid using machine-specific files in your repository.

2. **External Tools:**
   - Use external software (e.g., SCP) as needed to transfer files between the VM and your local machine.
   - Configure additional environments if required (e.g., Docker, Vagrant).

3. **Scripts:**
   - Automate tasks where possible, but ensure you can explain the purpose and functionality of every script during evaluation.

4. **Bruteforcing:**
   - Brute-forcing passwords is prohibited and unnecessary, as each solution must be justified.

## Mandatory Levels
- The following levels must be completed for the mandatory part of the project:
  - `level00`
  - `level01`
  - `level02`
  - `level03`
  - `level04`
  - `level05`
  - `level06`
  - `level07`
  - `level08`
  - `level09`
