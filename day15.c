#include <stdlib.h>
#include <stdio.h>
#include <stdint.h>

int main()
{
	uint64_t gena = 618;
	uint64_t genb = 814;
	// test
	//uint64_t gena = 65;
	//uint64_t genb = 8921;

	int i = 0;
	int matches = 0;

	while (i < 40000000) {
		gena = (gena * 16807) % 2147483647;
		genb = (genb * 48271) % 2147483647;
		if ((gena & 0xffff) == (genb & 0xffff))
			matches++;
		i++;
	}
	printf("A is %lu, B is %lu, matches = %d\n", gena, genb, matches);
}
