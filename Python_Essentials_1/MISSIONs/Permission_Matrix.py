# Define permission flags using powers of 2

READ = 4      # Binary: 100
WRITE = 2     # Binary: 010
EXECUTE = 1   # Binary: 001

#User has a combined score of 6 (Read + Write -> 110 in binary)
user_permissions = 6

#Test if the user has WRITE permission
has_write_permission = (user_permissions & WRITE) == WRITE

#Output the results
print(f"User Permission Score: {user_permissions} (Binary: {bin(user_permissions)})")
print(f"Checking for WRITE ({WRITE}): {has_write_permission}")

if has_write_permission:
    print("-> Access Granted: The user has WRITE permissions.")
else:
    print("-> Access Denied: The user does NOT have WRITE permissions.")