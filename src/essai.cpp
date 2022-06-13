#include <iostream>
using namespace std;

int main(void)
{
	int i = 0;

	if (i < 10)
	{
		int b = 3 * 4;
		while(i > 3)
			i++;
	}
	int toto = 3;

	for(int blabla = 0; i < 4; blabla--)
	{
		i += 1;
	}

	for(int blabla = 0; i < 4; blabla += 1)
	{
		i += 1;
	}

	for(int i = 0; i < 4; ++i)
	{
		i += 1;
	}

	for(int blabla = 0; i < 4; blabla = blabla + 1)
	{
		i += 1;
	}


}