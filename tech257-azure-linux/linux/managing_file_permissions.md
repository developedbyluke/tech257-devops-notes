# Managing File Permissions in Linux

-   [Managing File Permissions in Linux](#managing-file-permissions-in-linux)
    -   [Managing File Permissions using Symbols](#managing-file-permissions-using-symbols)
    -   [Managing File Permissions using Numeric Values](#managing-file-permissions-using-numeric-values)

## Managing File Permissions using Symbols

Being the owner of a file in a Linux system does not automatically grant you full permissions over that file. File permissions in Linux are determined by the specific permissions set for the file, which can be modified using commands like `chmod`. The owner of a file can have any combination of read (`r`), write (`w`), and execute (`x`) permissions as defined by the file's permission settings. The permissions can be restricted even for the owner, based on how they are set.

In Linux, file permissions are defined for three types of entities: User, Group, and Other.

-   **User (u):** Refers to the file's owner. Permissions given to the User entity directly affect what actions the owner of the file can perform. For example, if the User permissions are read-only (`r--`), then the owner can only read the file, not modify or execute it.
-   **Group (g):** Refers to a group that is associated with the file. Each file in Linux is associated with a single group, and the permissions set for the Group entity affect all users who are members of that group. If the Group permissions are read and write (`rw-`), then any user who is a member of the group associated with the file can read and modify the file but not execute it.
-   **Other (o):** Refers to all other users on the system who are not the owner and not members of the group associated with the file. Setting permissions for the Other entity controls what actions can be performed on the file by these users. For example, if Other permissions are read, write, and execute (`rwx`), then any user on the system can read, modify, and execute the file.

Given the scenario where User (owner) permissions are read-only, Group permissions are read and write, and Other permissions are read, write, and execute, if you are logged in as the user who is the owner of the file, you will only have read permissions on this file (`r--`). Despite being the owner, the permissions set for the User entity take precedence over your ownership status, restricting you to read-only access.

The line from the `ls -l` command `-rwxr-xr-- 1 tcboony staff 123 Nov 25 18:36 keeprunning.sh` provides the following information:

-   `-rwxr-xr--`: The file permissions.
-   `rwx` for the owner (User) means the owner can read, write, and execute the file.
-   `r-x` for the group means members of the file's group can read and execute the file, but not write to it.
-   `r--` for others means all other users can only read the file.
-   `1`: The number of hard links to the file.
-   `tcboony`: The owner of the file.
-   `staff`: The group associated with the file.
-   `123`: The size of the file in bytes.
-   `Nov 25 18:36`: The last modification date and time of the file.
-   `keeprunning.sh`: The name of the file or directory.

This line indicates that "keeprunning.sh" is a file with specific permissions set for the owner (tcboony), the group (staff), and all other users, with its size being 123 bytes and the last modification made on November 25 at 18:36.

## Managing File Permissions using Numeric Values

-   **Read (r)** : 4
-   **Write (w)** : 2
-   **Execute (x)** : 1

To calculate the numeric value for a combination of permissions, you sum these values. For example:

1. **Read + Write permissions**:

-   Read (4) + Write (2) = **6**

1. **Read, Write, and Execute permissions**:

-   Read (4) + Write (2) + Execute (1) = **7**

1. **Read and Execute permissions**:

-   Read (4) + Execute (1) = **5**

A representation made up of three numbers is a representation of permissions for the owner, group, and others, in that order:

-   The **first digit** represents the owner's permissions.
-   The **second digit** represents the group's permissions.
-   The **third digit** represents others' permissions.

For example, **644**:

-   **6** (owner): Read (4) + Write (2) = **Read and Write** permissions
-   **4** (group): Read (4) = **Read** permission
-   **4** (others): Read (4) = **Read** permission
