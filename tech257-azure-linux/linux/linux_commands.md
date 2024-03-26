# Linux Commands Documentation

-   [Linux Commands Documentation](#linux-commands-documentation)
    -   [Navigation Commands](#navigation-commands)
    -   [File and Directory Management Commands](#file-and-directory-management-commands)
    -   [File Content Management Commands](#file-content-management-commands)
    -   [Text Editors](#text-editors)
    -   [File Information Commands](#file-information-commands)
    -   [Package Management Commands](#package-management-commands)
    -   [Permissions Commands](#permissions-commands)
    -   [Process Management Commands](#process-management-commands)
    -   [Other Commands](#other-commands)

---

## Navigation Commands

-   `pwd`: Print the current working directory (path).
-   `cd`: Change the directory to the specified path. Without a path, it changes to the home directory of the current user.
-   `cd /`: Change the current working directory to the root directory (`/`).

## File and Directory Management Commands

-   `ls`: List files and directories in the current directory.
-   `ls -a`: List all files and directories, including hidden ones (those starting with a dot `.`).
-   `mkdir [directory_name]`: Create a new directory.
-   `touch [file_name]`: Create an empty file or update the timestamp of an existing file.
-   `cp [source] [destination]`: Copy a file from the source to the destination.
-   `mv [source] [destination]`: Move (rename) a file or directory.
-   `rm [file_name]`: Delete a file.
-   `rm -d [directory_name]`: Remove an empty directory.
-   `rm -r [directory_name]`: Remove a directory and its contents recursively. **Potentially dangerous!**

## File Content Management Commands

-   `cat [file_name]`: Display the contents of a file.
-   `head -n [number] [file_name]`: Display the first n lines of a file.
-   `tail -n [number] [file_name]`: Display the last n lines of a file.
-   `nl [file_name]`: Display the contents of a file with line numbers.
-   `grep [pattern] [file_name]`: Display lines from a file that match a specific pattern or string.
-   `echo [string]`: Print a string to the terminal.

## Text Editors

-   `nano [file_name]`: Open a file in the nano text editor.

    -   **Save Changes**: Press `Ctrl + S` to save the file.
    -   **Exit**: Press `Ctrl + X`. If there are unsaved changes, nano will ask if you want to save them, otherwise it will exit immediately.
    -   **Search Text**: Press `Ctrl + W`, then type the text you're looking for and press `Enter`.
    -   **Cut Text**: Navigate to the line you want to cut and press `Ctrl + K`.
    -   **Paste Text**: Navigate to where you want to paste and press `Ctrl + U`.

-   `vim [file_name]`: Open a file in the vim text editor.
    -   **Enter Insert Mode**: Press `i` to start inserting text at the cursor's location, or `a` to append text after the cursor.
    -   **Save Changes**: Press `Esc` to go back to command mode, then type `:w` and press `Enter` to save the file.
    -   **Exit**: Type `:q` and press `Enter` to quit. If you have unsaved changes, Vim will warn you. To quit without saving, type `:q!` and press `Enter`.
    -   **Search Text**: Press `Esc` to ensure you're in command mode, then type `/{text}` and press `Enter` to search for `{text}`.
    -   **Cut (Delete) Text**: In command mode, navigate to the line you want to cut and press `dd`. To cut a specific number of lines, type `{number}dd`, replacing `{number}` with how many lines you want to cut.
    -   **Paste Text**: After cutting or copying, navigate to where you want to paste and press `p` to paste after the cursor, or `P` to paste before the cursor.
    -   **Undo**: Press `u` in command mode to undo the last action. Press `Ctrl + R` to redo.

## File Information Commands

-   `file [file_name]`: Determine the type of a file.
-   `ps -p $$`: Display the process information for the current shell process (identified by `$$`).
-   `history`: Display the command history of the current shell session.

## Package Management Commands

-   `sudo apt install [package_name]`: Install a package using the apt package manager with superuser privileges.
-   `sudo apt update`: Update the package lists from the repositories.
-   `sudo apt upgrade`: Upgrade all installed packages to their latest versions. Add `-y` to automatically answer "yes" to any prompts.

## Permissions Commands

-   `chmod [permissions] [file_name]`: Change the permissions of a file or directory, e.g. `chmod +x script.sh` to add execute permissions.

## Process Management Commands

-   `ps aux` - View all running processes.
-   `top` - View a dynamic, real-time list of running processes.
-   `command &` - Run `command` in the background.
-   `fg` - Bring a background process to the foreground.
-   `kill PID` - Gracefully terminate a process with the given PID.
-   `kill -9 PID` - Forcefully terminate a process with the given PID.
-   `pgrep name` - Find the PID of a process named `name`.

## Other Commands

-   `curl [URL]`: Transfer data from or to a server using various protocols (e.g., HTTP, FTP).
-   `curl [URL] --output [file_name]`: Download data from a URL and save it to a specified file.
-   `tree`: Display a tree-like representation of directories and files in the current directory. (Note: `tree` might need to be installed separately.)
-   `sudo su`: Switch to the root user account (superuser).

> **Note**: Commands like `rm` and `sudo` can be **potentially dangerous** and cause data loss or system damage if used improperly, so they should be used with caution.
