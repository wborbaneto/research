#line 1 "F:/Dropbox/UFPI - Aulas/UFPI/PIBIC/I2C 16x2, 20x2, 20x4 LCD/I2C LCD.c"
#line 1 "f:/dropbox/ufpi - aulas/ufpi/pibic/i2c 16x2, 20x2, 20x4 lcd/lcd_i2c.h"
void I2C_LCD_Cmd(char out_char);
void I2C_LCD_Chr(char row, char column, char out_char);
void I2C_LCD_Chr_Cp(char out_char);
void I2C_LCD_Init();
void I2C_LCD_Out(char row, char col, char *text);
void I2C_LCD_Out_Cp(char *text);

void I2C_LCD_Cmd(char out_char) {

 char hi_n, lo_n;
 char rs = 0x00;

 hi_n = out_char & 0xF0;
 lo_n = (out_char << 4) & 0xF0;

 Soft_I2C_Start();

 Soft_I2C_Write( 0x7E );

 Soft_I2C_Write(hi_n | rs | 0x04 | 0x08);

 Delay_us(50);
 Soft_I2C_Write(hi_n | rs | 0x00 | 0x08);

 Soft_I2C_Write(lo_n | rs | 0x04 | 0x08);
 Delay_us(50);
 Soft_I2C_Write(lo_n | rs | 0x00 | 0x08);

 Soft_I2C_Stop();

 if(out_char == 0x01)Delay_ms(2);
}

void I2C_LCD_Chr(char row, char column, char out_char) {

 char hi_n, lo_n;
 char rs = 0x01;

 switch(row){

 case 1:
 I2C_LCD_Cmd(0x80 + (column - 1));
 break;
 case 2:
 I2C_LCD_Cmd(0xC0 + (column - 1));
 break;
 case 3:
 I2C_LCD_Cmd(0x94 + (column - 1));
 break;
 case 4:
 I2C_LCD_Cmd(0xD4 + (column - 1));
 break;
 };

 hi_n = out_char & 0xF0;
 lo_n = (out_char << 4) & 0xF0;

 Soft_I2C_Start();

 Soft_I2C_Write( 0x7E );

 Soft_I2C_Write(hi_n | rs | 0x04 | 0x08);

 Delay_us(50);
 Soft_I2C_Write(hi_n | rs | 0x00 | 0x08);

 Delay_us(100);
 Soft_I2C_Write(lo_n | rs | 0x04 | 0x08);

 Delay_us(50);
 Soft_I2C_Write(lo_n | rs | 0x00 | 0x08);

 Soft_I2C_Stop();
}

void I2C_LCD_Chr_Cp(char out_char) {

 char hi_n, lo_n;
 char rs = 0x01;

 hi_n = out_char & 0xF0;
 lo_n = (out_char << 4) & 0xF0;

 Soft_I2C_Start();

 Soft_I2C_Write( 0x7E );

 Soft_I2C_Write(hi_n | rs | 0x04 | 0x08);

 Delay_us(50);
 Soft_I2C_Write(hi_n | rs | 0x00 | 0x08);

 Delay_us(100);
 Soft_I2C_Write(lo_n | rs | 0x04 | 0x08);

 Delay_us(50);
 Soft_I2C_Write(lo_n | rs | 0x00 | 0x08);

 Soft_I2C_Stop();
}


void I2C_LCD_Init() {

 char rs = 0x00;

 Soft_I2C_Start();

 Soft_I2C_Write( 0x7E );


 Delay_ms(30);

 Soft_I2C_Write(0x30 | rs | 0x04 | 0x08);

 Delay_us(50);
 Soft_I2C_Write(0x30 | rs | 0x00 | 0x08);


 Delay_ms(10);

 Soft_I2C_Write(0x30 | rs | 0x04 | 0x08);

 Delay_us(50);
 Soft_I2C_Write(0x30 | rs | 0x00 | 0x08);


 Delay_ms(10);

 Soft_I2C_Write(0x30 | rs | 0x04 | 0x08);

 Delay_us(50);
 Soft_I2C_Write(0x30 | rs | 0x00 | 0x08);


 Delay_ms(10);

 Soft_I2C_Write(0x20 | rs | 0x04 | 0x08);

 Delay_us(50);
 Soft_I2C_Write(0x20 | rs | 0x00 | 0x08);

 Soft_I2C_Stop();

 Delay_ms(10);

 I2C_LCD_Cmd(0x28);
 I2C_LCD_Cmd(0x06);
}

void I2C_LCD_Out(char row, char col, char *text) {
 while(*text)
 I2C_LCD_Chr(row, col++, *text++);
}

void I2C_LCD_Out_Cp(char *text) {
 while(*text)
 I2C_LCD_Chr_Cp(*text++);
}
#line 24 "F:/Dropbox/UFPI - Aulas/UFPI/PIBIC/I2C 16x2, 20x2, 20x4 LCD/I2C LCD.c"
sbit Soft_I2C_Scl at RD2_bit;
sbit Soft_I2C_Sda at RD3_bit;
sbit Soft_I2C_Scl_direction at TRISD2_bit;
sbit Soft_I2C_Sda_direction at TRISD3_bit;


 sfr sbit Mmc_Chip_Select at RB2_bit;
 sfr sbit Mmc_Chip_Select_Direction at TRISB2_bit;


 unsigned char filename[] = "Temp.TXT";
 unsigned char error;
 unsigned char i;
 unsigned int adc_value;
 unsigned char tam[15];
 unsigned char teste[ 15 ]="123456789123\r";
 unsigned char coisa[15]="00000000000000";
 unsigned char character[15];
 unsigned long j,size;
 char erro,byte_read;




void main() {
 ADCON1 |= 0x0F;
 CMCON |= 7;

 TRISA =0x00;
 TRISB=0x21;
 TRISC=0x00;
 TRISD=0x00;

 PORTA=0x00;
 PORTB=0x00;
 PORTC=0b01000000;
 PORTD=0x00;

 I2C_LCD_Init();
 I2C_LCD_Cmd( 0x0C );
 I2C_LCD_Cmd( 0x01 );
#line 74 "F:/Dropbox/UFPI - Aulas/UFPI/PIBIC/I2C 16x2, 20x2, 20x4 LCD/I2C LCD.c"
 SPI1_Init();
 SPI1_Init_Advanced(_SPI_MASTER_OSC_DIV64, _SPI_DATA_SAMPLE_MIDDLE, _SPI_CLK_IDLE_LOW, _SPI_LOW_2_HIGH);
 Delay_us(100);

 do{
 I2C_LCD_Cmd( 0x01 );
 I2C_Lcd_Out(1,1,"NAO ENCONTRADO");
 error = MMC_Init();
 delay_ms(1000);
 }
 while(error);


 I2C_LCD_Cmd( 0x01 );
 I2C_Lcd_Out(1,1,"CARTAO DETECTADO");
 I2C_Lcd_Out(2,1,"INICIALIZADO");
 Delay_ms(1000);
#line 167 "F:/Dropbox/UFPI - Aulas/UFPI/PIBIC/I2C 16x2, 20x2, 20x4 LCD/I2C LCD.c"
}
