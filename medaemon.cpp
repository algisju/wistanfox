#include <sys/types.h>
#include <sys/stat.h>
#include <stdio.h>
#include <stdlib.h>
#include <fcntl.h>
#include <errno.h>
#include <unistd.h>
#include <syslog.h>
#include <string.h>

int main(void) {
        pid_t pid, sid; /* Our process ID and Session ID */
        pid = fork();	/* Fork off the parent process */
        if (pid < 0) {
				printf("Failed to Init Daemon");
                exit(EXIT_FAILURE);
        }
        if (pid > 0) {	/* If we got a good PID, then we can exit the parent process. */
				printf("Daemon Lauched Process %d",pid);
                exit(EXIT_SUCCESS);
        }
        umask(0);		/* Change the file mode mask */
		/* Open any logs here */
        sid = setsid();	/* Create a new SID for the child process */
        if (sid < 0) {
                exit(EXIT_FAILURE);	/* Log if failure */
        }
        if ((chdir("/")) < 0) {		/* Change the current working directory */
                /* Log the failure */
                exit(EXIT_FAILURE);
        }
        /* Close out the standard file descriptors */
        close(STDIN_FILENO);
        close(STDOUT_FILENO);
        close(STDERR_FILENO);
        /* Daemon-specific initialization goes here */
        /* The Big Loop */
        while (1) {
           /* Do some task here ... */
           /* Listen keyboard */
           sleep(30); /* wait 30 seconds */
        }
   exit(EXIT_SUCCESS);
}
