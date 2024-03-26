# Changing File Permissions in Linux

-   [Changing File Permissions in Linux](#changing-file-permissions-in-linux)
    -   [Linux Command for Changing File Permissions](#linux-command-for-changing-file-permissions)
    -   [Requirements for Changing Permissions on a File](#requirements-for-changing-permissions-on-a-file)
    -   [Examples of Setting Permissions on a File](#examples-of-setting-permissions-on-a-file)
        -   [1. Set Permissions: User to Read, Group to Read + Write + Execute, and Other to Read and Write Only](#1-set-permissions-user-to-read-group-to-read--write--execute-and-other-to-read-and-write-only)
        -   [2. Add Execute Permissions (to All Entities)](#2-add-execute-permissions-to-all-entities)
        -   [3. Take Write Permissions Away from Group](#3-take-write-permissions-away-from-group)
        -   [4. Use Numeric Values to Give Read + Write Access to User, Read Access to Group, and No Access to Other](#4-use-numeric-values-to-give-read--write-access-to-user-read-access-to-group-and-no-access-to-other)

### Linux Command for Changing File Permissions

The command used to change file permissions in Linux is `chmod` (change mode).

### Requirements for Changing Permissions on a File

To change permissions on a file, the end user must be either:

1. The owner of the file.
2. A superuser or have administrative privileges.

### Examples of Setting Permissions on a File

#### 1. Set Permissions: User to Read, Group to Read + Write + Execute, and Other to Read and Write Only

You can set these permissions using symbolic notation:

```bash
chmod u=r,g=rwx,o=rw testfile.txt
```

Or using numeric (octal) notation:

```bash
chmod 674 testfile.txt
```

#### 2. Add Execute Permissions (to All Entities)

To add execute permissions for all (user, group, and others), you can use:

```bash
chmod a+x testfile.txt
```

Or, if you're setting execute for all entities from scratch:

```bash
chmod +x testfile.txt
```

#### 3. Take Write Permissions Away from Group

To remove write permission from the group:

```bash
chmod g-w testfile.txt
```

#### 4. Use Numeric Values to Give Read + Write Access to User, Read Access to Group, and No Access to Other

To set permissions with numeric (octal) values for user read+write, group read only, and no access for others:

```bash
chmod 640 testfile.txt
```

-   **6** for the user: read (4) + write (2) = 6.
-   **4** for the group: read (4) = 4.
-   **0** for others: no permissions = 0.

Each permission operation in Linux, especially using `chmod`, can be performed using either symbolic notation (letters) or numeric (octal) notation, providing flexibility depending on the user's preference or requirements.
