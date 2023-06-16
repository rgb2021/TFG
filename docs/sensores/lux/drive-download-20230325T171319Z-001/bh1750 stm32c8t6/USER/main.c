
#include "usart.h"
#include "delay.h"
#include "sys.h"
#include "led.h"
#include "timer.h"
#include "bh1750.h"

 int main(void)
 {		
	 
	 delay_init();
	 uart_init(115200);
	 LED_Init();
	 //LED1_Init();
	 //TIM3_Int_Init(71,999);
	 printf("π‚’’«ø∂»ºÏ≤‚------\n");
	 bh1750_Init();
   while(1)
	{

		
	}	 
 }

