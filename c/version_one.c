#include <stdio.h>

/*
 * Let's have a go at writing a FizzBuzz before I Know anything 
 * about C except for how to print "Hello World!". 
 *
 * Sorry if your eyes bleed.
 */
int main(void)
{
	puts("Let's play fizzbuzz!\n");
	
	int i;
	for(i = 1; i <=100; i++)
	{
		if(i % 3 == 0 && i % 5 == 0) 
		{
			puts("FizzBuzz");
		}
		else if(i % 3 == 0) 
		{ 
			puts("Fizz"); 
		}
		else if(i % 5 == 0) 
		{ 
			puts("Buzz");
		} 
		else 
		{ 
			printf("%d\n", i);
		}
	}

	return(0);
}