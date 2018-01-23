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

	while (i < 5000000) {
		int stopa = 0;
		int stopb = 0;
		uint16_t a = 0;
		uint16_t b = 0;
		while(stopa == 0) {
			gena = (gena * 16807) % 2147483647;
			if (!(gena & 0x3)) {
				a = (uint16_t)gena;
				stopa = 1;
			}
		}
		while(stopb == 0) {
			genb = (genb * 48271) % 2147483647;
			if (!(genb & 0x7)) {
				b = (uint16_t)genb;
				stopb = 1;
			}
		}
		if (a == b) {
			matches++;
		}
		i++;
	}
	printf("A is %lu, B is %lu, matches = %d\n", gena, genb, matches);
}
