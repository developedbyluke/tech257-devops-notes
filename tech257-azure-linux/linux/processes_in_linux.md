# Processes in Linux

#### Viewing Processes

To view active processes, you can use the `ps` command for a snapshot, or `top` for a dynamic, real-time view.

-   `ps aux` displays all running processes with detailed information.
-   `top` provides a real-time view of running processes and their resource usage.

#### Running Processes in the Background

To run a process in the background, add an `&` at the end of the command:

```bash
command &
```

This allows the terminal to be used for other tasks while the process runs. To bring a background process to the foreground, use the `fg` command, optionally followed by the job number.

#### Managing Processes

You can use the `kill` command to terminate processes. This command requires the process ID (PID).

-   To gracefully terminate a process, use: `kill PID`.
-   To forcefully terminate a process, use: `kill -9 PID`.
