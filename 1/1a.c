#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int freq = 0;

int main(int argc, char *argv[]){

	for (int i=0; i<argc; i++){
		freq += atoi(argv[i]);
	}
	printf("Frequency is %d\n", freq);
	return 0;
}
