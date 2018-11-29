#line 1 "C:/TESTE/UFPI/Monitorias&Acadêmicos/PIBIC/I2C 16x2, 20x2, 20x4 LCD/SoftWareUart.c"
void __SoftWareUart_Init()
{
 SoftWare_Uart_Tx=1;
 SoftWare_Uart_Rx=1;
 SoftWare_Uart_Tx_Direction=0;
 SoftWare_Uart_Rx_Direction=1;

 SoftWare_Uart_Tx=1;
 delay_us(BITPERIOD);
}


void __Tx_Byte(unsigned char Data)
{
 char mask;
 SoftWare_Uart_Tx = 0;
 delay_us(BITPERIOD);

 for (mask=0x01;mask!=0;mask=mask<<1)
 {
 if(Data&mask) SoftWare_Uart_Tx = 1;
 else SoftWare_Uart_Tx = 0;
 delay_us(BITPERIOD);
 }
 SoftWare_Uart_Tx = 1;
 delay_us(BITPERIOD);
}

unsigned char __Rx_Byte()
{
 char mask;
 char Data;
 Data=0;
 while(SoftWare_Uart_Rx);
 delay_us(HALFBITPERIOD);
 for(mask=0x01;mask!=0;mask=mask<<1)
 {
 delay_us(BITPERIOD);
 if(SoftWare_Uart_Rx)Data=Data|mask;
 }
 Delay_us(BITPERIOD);
 return Data;
}


void __SoftUart_Print(char* Text)
{
 while(*Text)__Tx_Byte(*Text++);
}


void __SoftUart_PrintLine(char* Text)
{
 while(*Text)__Tx_Byte(*Text++);
 __Tx_Byte('\r');__Tx_Byte('\n');
}



void __SoftUart_PrintConst(const char* Text)
{
 while(*Text)__Tx_Byte(*Text++);
}




void __SoftUart_PrintConstLine(const char* Text)
{
 while(*Text)__Tx_Byte(*Text++);
 __Tx_Byte('\r');__Tx_Byte('\n');
}





void __SoftUart_ScanText(char* Buffer, char StopChar)
{
 while(*(Buffer-1)!=StopChar)
 {
 *Buffer++=__Rx_Byte();
 }
 *--Buffer='\0';
}

void __SoftUart_PrintNChar(char* Buffer, char Size)
{
 char i;
 for(i=0;i<Size;i++)
 __Tx_Byte(Buffer[i]);
}

void __SoftUart_PrintNCharLine(char* Buffer, char Size)
{
 char i;
 for(i=0;i<Size;i++)
 __Tx_Byte(Buffer[i]);

 __Tx_Byte('\r');
 __Tx_Byte('\n');
}

unsigned char __SoftWareUart_GetChar()
{
 return __Rx_Byte();
}

void __SoftWareUart_PutChar(char DataByte)
{
 __Tx_Byte(DataByte);
}
