extern sfr sbit SoftWare_Uart_Tx;
extern sfr sbit SoftWare_Uart_Rx;
extern sfr sbit SoftWare_Uart_Tx_Direction;
extern sfr sbit SoftWare_Uart_Rx_Direction;




void __SoftWareUart_Init();
void __Tx_Byte(unsigned char Data);
unsigned char __Rx_Byte();
void __SoftUart_Print(char* Text);
void __SoftUart_PrintLine(char* Text);
void __SoftUart_PrintConst(const char* Text);
void __SoftUart_PrintConstLine(const char* Text);
void __SoftUart_ScanText(char* Buffer, char StopChar);
void __SoftUart_PrintNChar(char* Buffer, char Size);
void __SoftUart_PrintNCharLine(char* Buffer, char Size);
unsigned char __SoftWareUart_GetChar();
void __SoftWareUart_PutChar(char DataByte);




//change the baudrate here
#define BAUDRATE 38400       //<--------
#define BITPERIOD ((1000000/BAUDRATE)-2)//dont change this
#define HALFBITPERIOD (BITPERIOD/2)//dont change this




struct SOFTWARE_SERIAL_STRUCT
{
  void (*Init)();
  void (*Print)(char* Text);
  void (*PrintLine)(char* Text);
  void (*PrintConst)(const char* Text);
  void (*PrintConstLine)(const char* Text);
  void (*ScanText)(char* Buffer, char StopChar);
  void (*PrintNchar)(char* Buffer, char Size);
  void (*PrintNCharLine)(char* Buffer, char Size);
  unsigned char (*GetChar)();
  void (*PutChar)(char DataByte);
}SoftSerial=
{
&__SoftWareUart_Init,
&__SoftUart_Print,
&__SoftUart_PrintLine,
&__SoftUart_PrintConst,
&__SoftUart_PrintConstLine,
&__SoftUart_ScanText,
&__SoftUart_PrintNChar,
&__SoftUart_PrintNCharLine,
&__SoftWareUart_GetChar,
&__SoftWareUart_PutChar
};




#include "SoftWareUart.c"