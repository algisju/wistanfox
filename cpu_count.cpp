#include <unistd.h>
#include <stdio.h>
#include <cstring>
int main(void)
{
char str[256];
int procCount = 0;
FILE *fp;

if( (fp = fopen("/proc/cpuinfo", "r")) )
{
  while(fgets(str, sizeof str, fp))
  if( !memcmp(str, "processor", 9) ) procCount++;
}

if ( !procCount ) 
{ 
printf("Unable to get proc count. Defaulting to 2");
procCount=2;
}

printf("Proc Count:%d\n", procCount);
return 0;
}
