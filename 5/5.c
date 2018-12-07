#include <stdio.h>
#include <string.h>
#include <stdlib.h>

// Lower case == upper case + 32

int main(int argc, char *argv[]){
	FILE *f = fopen("input", "r");
	char c = fgetc(f);
	while(c != EOF){
		printf("%i ", c);
		c = fgetc(f);
	}
	printf("\n");
	fclose(f);
}
