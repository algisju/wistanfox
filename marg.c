#include <stdio.h>
#include <string.h>
int main(int argc, char **argv){
    int i;
    const char *commands[]={"-c", "-p", "-v", "-d", "-a", NULL};
    enum {CREATE,PRINT,VERSION,DATE,AUTH};
    if (argc<2) {
usage:   printf ("Usage: %s [command]\n" 
            "-c  Create new entry.\n" 
            "-p  Print the latest entry.\n" 
            "-v  Version.\n" 
            "-d  Sort by date.\n" 
            "-a  Sort by author.\n",argv[0]);
        return 0;
    }
    for (i=0;commands[i]&&strcmp(argv[1],commands[i]);i++);
    switch (i) {
    case CREATE:
	printf("create\n");
    break;
    case PRINT:
	printf("print stuff\n");
    break;
    case VERSION:
	printf("Version 0.0 By Geeks\'Gang\n\n");
	break;
    default:
    printf ("Unknown parameter... %s\n",argv[1]);
    goto usage;
    }
    return 0;
}
