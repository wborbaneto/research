
#define _LCD_FIRST_ROW          0x80     //Move cursor to the 1st row
#define _LCD_SECOND_ROW         0xC0     //Move cursor to the 2nd row
#define _LCD_CLEAR              0x01     //Clear display
#define _LCD_RETURN_HOME        0x02     //Return cursor to home position, returns a shifted display to
                                         //its original position. Display data RAM is unaffected.
#define _LCD_CURSOR_OFF         0x0C     //Turn off cursor
#define _LCD_UNDERLINE_ON       0x0E     //Underline cursor on
#define _LCD_BLINK_CURSOR_ON    0x0F     //Blink cursor on
#define _LCD_MOVE_CURSOR_LEFT   0x10     //Move cursor left without changing display data RAM
#define _LCD_MOVE_CURSOR_RIGHT  0x14     //Move cursor right without changing display data RAM
#define _LCD_TURN_ON            0x0C     //Turn Lcd display on
#define _LCD_TURN_OFF           0x08     //Turn Lcd display off
#define _LCD_SHIFT_LEFT         0x18     //Shift display left without changing display data RAM
#define _LCD_SHIFT_RIGHT        0x1E     //Shift display right without changing display data RAM

// LCD Definitions
#define LCD_ADDR 0x7E
#define BUFFER_SIZE 15

//SOFT I2C definitions
#include<lcd_i2c.h>

sbit Soft_I2C_Scl at RD2_bit;
sbit Soft_I2C_Sda at RD3_bit;
sbit Soft_I2C_Scl_direction at TRISD2_bit;
sbit Soft_I2C_Sda_direction at TRISD3_bit;

 //Memory Card Chip Select Connection
 sfr sbit Mmc_Chip_Select at RB2_bit;
 sfr sbit Mmc_Chip_Select_Direction at TRISB2_bit;

 // End LCD module connections
 unsigned char filename[] = "Temp.TXT";
 unsigned char error;
 unsigned char i;
 unsigned int adc_value;
 unsigned char tam[15];
 unsigned char teste[BUFFER_SIZE]="123456789123\r";
 unsigned char coisa[15]="00000000000000";
 unsigned char character[15];
 unsigned long j,size;
 char erro,byte_read;
 
 ///////////////////////////////////////////////////////////////////////
 

void main() {
    ADCON1 |= 0x0F;
    CMCON  |= 7;

    TRISA =0x00;
    TRISB=0x21;
    TRISC=0x00;
    TRISD=0x00;

    PORTA=0x00;
    PORTB=0x00;
    PORTC=0b01000000;
    PORTD=0x00;

    I2C_LCD_Init();
    I2C_LCD_Cmd(_LCD_CURSOR_OFF);
    I2C_LCD_Cmd(_LCD_CLEAR);
    
   /*erro=Soft_UART_Init(&PORTB,5,6,9600,0);

    if(erro>0){
         I2C_Lcd_Out(1,1,erro);
    }
    delay_ms(100);
    */
    
    SPI1_Init();
    SPI1_Init_Advanced(_SPI_MASTER_OSC_DIV64, _SPI_DATA_SAMPLE_MIDDLE, _SPI_CLK_IDLE_LOW, _SPI_LOW_2_HIGH);
    Delay_us(100);
    
    do{
      I2C_LCD_Cmd(_LCD_CLEAR);
      I2C_Lcd_Out(1,1,"NAO ENCONTRADO");
      error = MMC_Init();
      delay_ms(1000);
       }
    while(error);
       
       
     I2C_LCD_Cmd(_LCD_CLEAR);
     I2C_Lcd_Out(1,1,"CARTAO DETECTADO");
     I2C_Lcd_Out(2,1,"INICIALIZADO");
     Delay_ms(1000);
     /*
    byte_read=Soft_UART_Read(&erro);
    if(erro){
         I2C_LCD_Cmd(_LCD_CLEAR);
         I2C_Lcd_Out(1,1,erro);
    }
    else{
           I2C_Lcd_Out(1,1,byte_read);
    }
    
    
    
    
    
    
    
    
    
    
    
     /*
    while(1) {
         I2C_Lcd_Out(1,1," TESTE INICIAL");
         I2C_Lcd_Out(2,1," UFPI");
         
         SPI1_Init();
         SPI1_Init_Advanced(_SPI_MASTER_OSC_DIV64, _SPI_DATA_SAMPLE_MIDDLE, _SPI_CLK_IDLE_LOW, _SPI_LOW_2_HIGH);
         Delay_us(10);
         
         error = MMC_Init();
         while(error == 1){
          I2C_LCD_Cmd(_LCD_CLEAR);
          I2C_Lcd_Out(1,1,"NAO ENCONTRADO");
          I2C_LCD_Cmd(_LCD_CURSOR_OFF);
          delay_ms(1000);
          error = MMC_Init();
          }
         I2C_LCD_Cmd(_LCD_CLEAR);
         I2C_Lcd_Out(1,1,"CARTAO DETECTADO");
         I2C_Lcd_Out(2,1,"INICIALIZADO");
         Delay_ms(1000);
         
         MMC_Fat_Init(); // inicia o cartão
         
         SPI1_Init_Advanced(_SPI_MASTER_OSC_DIV4, _SPI_DATA_SAMPLE_MIDDLE, _SPI_CLK_IDLE_LOW, _SPI_LOW_2_HIGH);
         
         j=Mmc_Fat_Assign(&filename,0xA0);//cria ou informe se existe o .txt

         if(j==1){
              I2C_LCD_Cmd(_LCD_CLEAR);
              I2C_Lcd_Out(1,1,".TXT CRIADO") ;
         }
         else{
              I2C_LCD_Cmd(_LCD_CLEAR);
              I2C_Lcd_Out(1,1,"NAO GRAVADO") ;
              while(1);
         }
         delay_ms(1000);
         Mmc_Fat_Append();  //Abre o arquivo para salvar    algo nele sem apagar
         Mmc_Fat_Write(teste,15);   //Salva um determinado número de bytes no arquivo
         
         Mmc_Fat_Assign(&filename, 0);
         Mmc_Fat_Reset(&size);            // Reseta o vetor posição e retorna o tamanho
         LongToStr(size,tam);
         I2C_LCD_Cmd(_LCD_CLEAR);
         I2C_Lcd_Out(1,1,tam);
         
         delay_ms(1000);
         
         for (j = 1; j <= 15; j++) {
             Mmc_Fat_Read(&character);
             I2C_Lcd_Out(1,j,character);
             }
         delay_ms(1000);
         while(1);
    } */
}