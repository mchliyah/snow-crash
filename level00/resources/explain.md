
# Explanation for Level00

## Observations
1. The project uses two types of users:
   - `levelXX`: Regular user accounts.
   - `flagXX`: Accounts containing the flags required to progress.

2. The goal is to switch from `level00` to `flag00` by identifying and using the corresponding password.

## Steps to Solve

### Step 1: Identify Users and Files
- Searched for files corresponding to user accounts by exploring user-owned files:
  ```bash
  find / -user flag00 2>/dev/null
  ```
- Found a file located at:
  ```
  /usr/sbin/john
  ```

### Step 2: Analyze the File
- Opened the file to inspect its contents. It contained an encrypted password.
  ```
  cdiiddwpgswtgt
  ```

- After an online search, determined that the encryption used was **Rot 15**.

### Step 3: Decrypt the Password
- Decrypted the Rot 15 hash using an online Rot 15 decryption tool to obtain the plaintext password.
  ```
  nottoohardhere
  ```

### Step 4: Switch to flag00 User
- Used the decrypted password to switch to the `flag00` account:
  ```
  bash
  $> su flag00
  $> Password: nottoohardhere
  ```

### Step 5: Retrieve the Flag
- After logging in, executed the `getflag` command:
  ```bash
  getflag
  ```
- This command displayed the token needed for the next level.
  ```
  Check flag.Here is your token : xxxxxxxxxxxxxxxxxxxxxxxxxxxxx
  ```
## Notes
- The message after switching to `flag00` reminded to execute the `getflag` command to retrieve the token.
- Understanding file permissions and ownership was crucial in identifying the relevant file.

## Commands Summary
```bash
# Find files owned by the target user
find / -user flag00 2>/dev/null

# Switch user
su flag00

# Retrieve the flag
getflag
```