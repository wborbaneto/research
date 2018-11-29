
_I2C_LCD_Cmd:

;lcd_i2c.h,8 :: 		void I2C_LCD_Cmd(char out_char) {
;lcd_i2c.h,11 :: 		char rs = 0x00;
	CLRF        I2C_LCD_Cmd_rs_L0+0 
;lcd_i2c.h,13 :: 		hi_n = out_char & 0xF0;
	MOVLW       240
	ANDWF       FARG_I2C_LCD_Cmd_out_char+0, 0 
	MOVWF       I2C_LCD_Cmd_hi_n_L0+0 
;lcd_i2c.h,14 :: 		lo_n = (out_char << 4) & 0xF0;
	MOVF        FARG_I2C_LCD_Cmd_out_char+0, 0 
	MOVWF       I2C_LCD_Cmd_lo_n_L0+0 
	RLCF        I2C_LCD_Cmd_lo_n_L0+0, 1 
	BCF         I2C_LCD_Cmd_lo_n_L0+0, 0 
	RLCF        I2C_LCD_Cmd_lo_n_L0+0, 1 
	BCF         I2C_LCD_Cmd_lo_n_L0+0, 0 
	RLCF        I2C_LCD_Cmd_lo_n_L0+0, 1 
	BCF         I2C_LCD_Cmd_lo_n_L0+0, 0 
	RLCF        I2C_LCD_Cmd_lo_n_L0+0, 1 
	BCF         I2C_LCD_Cmd_lo_n_L0+0, 0 
	MOVLW       240
	ANDWF       I2C_LCD_Cmd_lo_n_L0+0, 1 
;lcd_i2c.h,16 :: 		Soft_I2C_Start();
	CALL        _Soft_I2C_Start+0, 0
;lcd_i2c.h,18 :: 		Soft_I2C_Write(LCD_ADDR);
	MOVLW       126
	MOVWF       FARG_Soft_I2C_Write_data_+0 
	CALL        _Soft_I2C_Write+0, 0
;lcd_i2c.h,20 :: 		Soft_I2C_Write(hi_n | rs | 0x04 | 0x08);
	MOVF        I2C_LCD_Cmd_rs_L0+0, 0 
	IORWF       I2C_LCD_Cmd_hi_n_L0+0, 0 
	MOVWF       FARG_Soft_I2C_Write_data_+0 
	BSF         FARG_Soft_I2C_Write_data_+0, 2 
	BSF         FARG_Soft_I2C_Write_data_+0, 3 
	CALL        _Soft_I2C_Write+0, 0
;lcd_i2c.h,22 :: 		Delay_us(50);
	MOVLW       2
	MOVWF       R12, 0
	MOVLW       75
	MOVWF       R13, 0
L_I2C_LCD_Cmd0:
	DECFSZ      R13, 1, 1
	BRA         L_I2C_LCD_Cmd0
	DECFSZ      R12, 1, 1
	BRA         L_I2C_LCD_Cmd0
;lcd_i2c.h,23 :: 		Soft_I2C_Write(hi_n | rs | 0x00 | 0x08);
	MOVF        I2C_LCD_Cmd_rs_L0+0, 0 
	IORWF       I2C_LCD_Cmd_hi_n_L0+0, 0 
	MOVWF       FARG_Soft_I2C_Write_data_+0 
	BSF         FARG_Soft_I2C_Write_data_+0, 3 
	CALL        _Soft_I2C_Write+0, 0
;lcd_i2c.h,25 :: 		Soft_I2C_Write(lo_n | rs | 0x04 | 0x08);
	MOVF        I2C_LCD_Cmd_rs_L0+0, 0 
	IORWF       I2C_LCD_Cmd_lo_n_L0+0, 0 
	MOVWF       FARG_Soft_I2C_Write_data_+0 
	BSF         FARG_Soft_I2C_Write_data_+0, 2 
	BSF         FARG_Soft_I2C_Write_data_+0, 3 
	CALL        _Soft_I2C_Write+0, 0
;lcd_i2c.h,26 :: 		Delay_us(50);
	MOVLW       2
	MOVWF       R12, 0
	MOVLW       75
	MOVWF       R13, 0
L_I2C_LCD_Cmd1:
	DECFSZ      R13, 1, 1
	BRA         L_I2C_LCD_Cmd1
	DECFSZ      R12, 1, 1
	BRA         L_I2C_LCD_Cmd1
;lcd_i2c.h,27 :: 		Soft_I2C_Write(lo_n | rs | 0x00 | 0x08);
	MOVF        I2C_LCD_Cmd_rs_L0+0, 0 
	IORWF       I2C_LCD_Cmd_lo_n_L0+0, 0 
	MOVWF       FARG_Soft_I2C_Write_data_+0 
	BSF         FARG_Soft_I2C_Write_data_+0, 3 
	CALL        _Soft_I2C_Write+0, 0
;lcd_i2c.h,29 :: 		Soft_I2C_Stop();
	CALL        _Soft_I2C_Stop+0, 0
;lcd_i2c.h,31 :: 		if(out_char == 0x01)Delay_ms(2);
	MOVF        FARG_I2C_LCD_Cmd_out_char+0, 0 
	XORLW       1
	BTFSS       STATUS+0, 2 
	GOTO        L_I2C_LCD_Cmd2
	MOVLW       52
	MOVWF       R12, 0
	MOVLW       241
	MOVWF       R13, 0
L_I2C_LCD_Cmd3:
	DECFSZ      R13, 1, 1
	BRA         L_I2C_LCD_Cmd3
	DECFSZ      R12, 1, 1
	BRA         L_I2C_LCD_Cmd3
	NOP
	NOP
L_I2C_LCD_Cmd2:
;lcd_i2c.h,32 :: 		}
L_end_I2C_LCD_Cmd:
	RETURN      0
; end of _I2C_LCD_Cmd

_I2C_LCD_Chr:

;lcd_i2c.h,34 :: 		void I2C_LCD_Chr(char row, char column, char out_char) {
;lcd_i2c.h,37 :: 		char rs = 0x01;
	MOVLW       1
	MOVWF       I2C_LCD_Chr_rs_L0+0 
;lcd_i2c.h,39 :: 		switch(row){
	GOTO        L_I2C_LCD_Chr4
;lcd_i2c.h,41 :: 		case 1:
L_I2C_LCD_Chr6:
;lcd_i2c.h,42 :: 		I2C_LCD_Cmd(0x80 + (column - 1));
	DECF        FARG_I2C_LCD_Chr_column+0, 0 
	MOVWF       R0 
	MOVF        R0, 0 
	ADDLW       128
	MOVWF       FARG_I2C_LCD_Cmd_out_char+0 
	CALL        _I2C_LCD_Cmd+0, 0
;lcd_i2c.h,43 :: 		break;
	GOTO        L_I2C_LCD_Chr5
;lcd_i2c.h,44 :: 		case 2:
L_I2C_LCD_Chr7:
;lcd_i2c.h,45 :: 		I2C_LCD_Cmd(0xC0 + (column - 1));
	DECF        FARG_I2C_LCD_Chr_column+0, 0 
	MOVWF       R0 
	MOVF        R0, 0 
	ADDLW       192
	MOVWF       FARG_I2C_LCD_Cmd_out_char+0 
	CALL        _I2C_LCD_Cmd+0, 0
;lcd_i2c.h,46 :: 		break;
	GOTO        L_I2C_LCD_Chr5
;lcd_i2c.h,47 :: 		case 3:
L_I2C_LCD_Chr8:
;lcd_i2c.h,48 :: 		I2C_LCD_Cmd(0x94 + (column - 1));
	DECF        FARG_I2C_LCD_Chr_column+0, 0 
	MOVWF       R0 
	MOVF        R0, 0 
	ADDLW       148
	MOVWF       FARG_I2C_LCD_Cmd_out_char+0 
	CALL        _I2C_LCD_Cmd+0, 0
;lcd_i2c.h,49 :: 		break;
	GOTO        L_I2C_LCD_Chr5
;lcd_i2c.h,50 :: 		case 4:
L_I2C_LCD_Chr9:
;lcd_i2c.h,51 :: 		I2C_LCD_Cmd(0xD4 + (column - 1));
	DECF        FARG_I2C_LCD_Chr_column+0, 0 
	MOVWF       R0 
	MOVF        R0, 0 
	ADDLW       212
	MOVWF       FARG_I2C_LCD_Cmd_out_char+0 
	CALL        _I2C_LCD_Cmd+0, 0
;lcd_i2c.h,52 :: 		break;
	GOTO        L_I2C_LCD_Chr5
;lcd_i2c.h,53 :: 		};
L_I2C_LCD_Chr4:
	MOVF        FARG_I2C_LCD_Chr_row+0, 0 
	XORLW       1
	BTFSC       STATUS+0, 2 
	GOTO        L_I2C_LCD_Chr6
	MOVF        FARG_I2C_LCD_Chr_row+0, 0 
	XORLW       2
	BTFSC       STATUS+0, 2 
	GOTO        L_I2C_LCD_Chr7
	MOVF        FARG_I2C_LCD_Chr_row+0, 0 
	XORLW       3
	BTFSC       STATUS+0, 2 
	GOTO        L_I2C_LCD_Chr8
	MOVF        FARG_I2C_LCD_Chr_row+0, 0 
	XORLW       4
	BTFSC       STATUS+0, 2 
	GOTO        L_I2C_LCD_Chr9
L_I2C_LCD_Chr5:
;lcd_i2c.h,55 :: 		hi_n = out_char & 0xF0;
	MOVLW       240
	ANDWF       FARG_I2C_LCD_Chr_out_char+0, 0 
	MOVWF       I2C_LCD_Chr_hi_n_L0+0 
;lcd_i2c.h,56 :: 		lo_n = (out_char << 4) & 0xF0;
	MOVF        FARG_I2C_LCD_Chr_out_char+0, 0 
	MOVWF       I2C_LCD_Chr_lo_n_L0+0 
	RLCF        I2C_LCD_Chr_lo_n_L0+0, 1 
	BCF         I2C_LCD_Chr_lo_n_L0+0, 0 
	RLCF        I2C_LCD_Chr_lo_n_L0+0, 1 
	BCF         I2C_LCD_Chr_lo_n_L0+0, 0 
	RLCF        I2C_LCD_Chr_lo_n_L0+0, 1 
	BCF         I2C_LCD_Chr_lo_n_L0+0, 0 
	RLCF        I2C_LCD_Chr_lo_n_L0+0, 1 
	BCF         I2C_LCD_Chr_lo_n_L0+0, 0 
	MOVLW       240
	ANDWF       I2C_LCD_Chr_lo_n_L0+0, 1 
;lcd_i2c.h,58 :: 		Soft_I2C_Start();
	CALL        _Soft_I2C_Start+0, 0
;lcd_i2c.h,60 :: 		Soft_I2C_Write(LCD_ADDR);
	MOVLW       126
	MOVWF       FARG_Soft_I2C_Write_data_+0 
	CALL        _Soft_I2C_Write+0, 0
;lcd_i2c.h,62 :: 		Soft_I2C_Write(hi_n | rs | 0x04 | 0x08);
	MOVF        I2C_LCD_Chr_rs_L0+0, 0 
	IORWF       I2C_LCD_Chr_hi_n_L0+0, 0 
	MOVWF       FARG_Soft_I2C_Write_data_+0 
	BSF         FARG_Soft_I2C_Write_data_+0, 2 
	BSF         FARG_Soft_I2C_Write_data_+0, 3 
	CALL        _Soft_I2C_Write+0, 0
;lcd_i2c.h,64 :: 		Delay_us(50);
	MOVLW       2
	MOVWF       R12, 0
	MOVLW       75
	MOVWF       R13, 0
L_I2C_LCD_Chr10:
	DECFSZ      R13, 1, 1
	BRA         L_I2C_LCD_Chr10
	DECFSZ      R12, 1, 1
	BRA         L_I2C_LCD_Chr10
;lcd_i2c.h,65 :: 		Soft_I2C_Write(hi_n | rs | 0x00 | 0x08);
	MOVF        I2C_LCD_Chr_rs_L0+0, 0 
	IORWF       I2C_LCD_Chr_hi_n_L0+0, 0 
	MOVWF       FARG_Soft_I2C_Write_data_+0 
	BSF         FARG_Soft_I2C_Write_data_+0, 3 
	CALL        _Soft_I2C_Write+0, 0
;lcd_i2c.h,67 :: 		Delay_us(100);
	MOVLW       3
	MOVWF       R12, 0
	MOVLW       151
	MOVWF       R13, 0
L_I2C_LCD_Chr11:
	DECFSZ      R13, 1, 1
	BRA         L_I2C_LCD_Chr11
	DECFSZ      R12, 1, 1
	BRA         L_I2C_LCD_Chr11
	NOP
	NOP
;lcd_i2c.h,68 :: 		Soft_I2C_Write(lo_n | rs | 0x04 | 0x08);
	MOVF        I2C_LCD_Chr_rs_L0+0, 0 
	IORWF       I2C_LCD_Chr_lo_n_L0+0, 0 
	MOVWF       FARG_Soft_I2C_Write_data_+0 
	BSF         FARG_Soft_I2C_Write_data_+0, 2 
	BSF         FARG_Soft_I2C_Write_data_+0, 3 
	CALL        _Soft_I2C_Write+0, 0
;lcd_i2c.h,70 :: 		Delay_us(50);
	MOVLW       2
	MOVWF       R12, 0
	MOVLW       75
	MOVWF       R13, 0
L_I2C_LCD_Chr12:
	DECFSZ      R13, 1, 1
	BRA         L_I2C_LCD_Chr12
	DECFSZ      R12, 1, 1
	BRA         L_I2C_LCD_Chr12
;lcd_i2c.h,71 :: 		Soft_I2C_Write(lo_n | rs | 0x00 | 0x08);
	MOVF        I2C_LCD_Chr_rs_L0+0, 0 
	IORWF       I2C_LCD_Chr_lo_n_L0+0, 0 
	MOVWF       FARG_Soft_I2C_Write_data_+0 
	BSF         FARG_Soft_I2C_Write_data_+0, 3 
	CALL        _Soft_I2C_Write+0, 0
;lcd_i2c.h,73 :: 		Soft_I2C_Stop();
	CALL        _Soft_I2C_Stop+0, 0
;lcd_i2c.h,74 :: 		}
L_end_I2C_LCD_Chr:
	RETURN      0
; end of _I2C_LCD_Chr

_I2C_LCD_Chr_Cp:

;lcd_i2c.h,76 :: 		void I2C_LCD_Chr_Cp(char out_char) {
;lcd_i2c.h,79 :: 		char rs = 0x01;
	MOVLW       1
	MOVWF       I2C_LCD_Chr_Cp_rs_L0+0 
;lcd_i2c.h,81 :: 		hi_n = out_char & 0xF0;
	MOVLW       240
	ANDWF       FARG_I2C_LCD_Chr_Cp_out_char+0, 0 
	MOVWF       I2C_LCD_Chr_Cp_hi_n_L0+0 
;lcd_i2c.h,82 :: 		lo_n = (out_char << 4) & 0xF0;
	MOVF        FARG_I2C_LCD_Chr_Cp_out_char+0, 0 
	MOVWF       I2C_LCD_Chr_Cp_lo_n_L0+0 
	RLCF        I2C_LCD_Chr_Cp_lo_n_L0+0, 1 
	BCF         I2C_LCD_Chr_Cp_lo_n_L0+0, 0 
	RLCF        I2C_LCD_Chr_Cp_lo_n_L0+0, 1 
	BCF         I2C_LCD_Chr_Cp_lo_n_L0+0, 0 
	RLCF        I2C_LCD_Chr_Cp_lo_n_L0+0, 1 
	BCF         I2C_LCD_Chr_Cp_lo_n_L0+0, 0 
	RLCF        I2C_LCD_Chr_Cp_lo_n_L0+0, 1 
	BCF         I2C_LCD_Chr_Cp_lo_n_L0+0, 0 
	MOVLW       240
	ANDWF       I2C_LCD_Chr_Cp_lo_n_L0+0, 1 
;lcd_i2c.h,84 :: 		Soft_I2C_Start();
	CALL        _Soft_I2C_Start+0, 0
;lcd_i2c.h,86 :: 		Soft_I2C_Write(LCD_ADDR);
	MOVLW       126
	MOVWF       FARG_Soft_I2C_Write_data_+0 
	CALL        _Soft_I2C_Write+0, 0
;lcd_i2c.h,88 :: 		Soft_I2C_Write(hi_n | rs | 0x04 | 0x08);
	MOVF        I2C_LCD_Chr_Cp_rs_L0+0, 0 
	IORWF       I2C_LCD_Chr_Cp_hi_n_L0+0, 0 
	MOVWF       FARG_Soft_I2C_Write_data_+0 
	BSF         FARG_Soft_I2C_Write_data_+0, 2 
	BSF         FARG_Soft_I2C_Write_data_+0, 3 
	CALL        _Soft_I2C_Write+0, 0
;lcd_i2c.h,90 :: 		Delay_us(50);
	MOVLW       2
	MOVWF       R12, 0
	MOVLW       75
	MOVWF       R13, 0
L_I2C_LCD_Chr_Cp13:
	DECFSZ      R13, 1, 1
	BRA         L_I2C_LCD_Chr_Cp13
	DECFSZ      R12, 1, 1
	BRA         L_I2C_LCD_Chr_Cp13
;lcd_i2c.h,91 :: 		Soft_I2C_Write(hi_n | rs | 0x00 | 0x08);
	MOVF        I2C_LCD_Chr_Cp_rs_L0+0, 0 
	IORWF       I2C_LCD_Chr_Cp_hi_n_L0+0, 0 
	MOVWF       FARG_Soft_I2C_Write_data_+0 
	BSF         FARG_Soft_I2C_Write_data_+0, 3 
	CALL        _Soft_I2C_Write+0, 0
;lcd_i2c.h,93 :: 		Delay_us(100);
	MOVLW       3
	MOVWF       R12, 0
	MOVLW       151
	MOVWF       R13, 0
L_I2C_LCD_Chr_Cp14:
	DECFSZ      R13, 1, 1
	BRA         L_I2C_LCD_Chr_Cp14
	DECFSZ      R12, 1, 1
	BRA         L_I2C_LCD_Chr_Cp14
	NOP
	NOP
;lcd_i2c.h,94 :: 		Soft_I2C_Write(lo_n | rs | 0x04 | 0x08);
	MOVF        I2C_LCD_Chr_Cp_rs_L0+0, 0 
	IORWF       I2C_LCD_Chr_Cp_lo_n_L0+0, 0 
	MOVWF       FARG_Soft_I2C_Write_data_+0 
	BSF         FARG_Soft_I2C_Write_data_+0, 2 
	BSF         FARG_Soft_I2C_Write_data_+0, 3 
	CALL        _Soft_I2C_Write+0, 0
;lcd_i2c.h,96 :: 		Delay_us(50);
	MOVLW       2
	MOVWF       R12, 0
	MOVLW       75
	MOVWF       R13, 0
L_I2C_LCD_Chr_Cp15:
	DECFSZ      R13, 1, 1
	BRA         L_I2C_LCD_Chr_Cp15
	DECFSZ      R12, 1, 1
	BRA         L_I2C_LCD_Chr_Cp15
;lcd_i2c.h,97 :: 		Soft_I2C_Write(lo_n | rs | 0x00 | 0x08);
	MOVF        I2C_LCD_Chr_Cp_rs_L0+0, 0 
	IORWF       I2C_LCD_Chr_Cp_lo_n_L0+0, 0 
	MOVWF       FARG_Soft_I2C_Write_data_+0 
	BSF         FARG_Soft_I2C_Write_data_+0, 3 
	CALL        _Soft_I2C_Write+0, 0
;lcd_i2c.h,99 :: 		Soft_I2C_Stop();
	CALL        _Soft_I2C_Stop+0, 0
;lcd_i2c.h,100 :: 		}
L_end_I2C_LCD_Chr_Cp:
	RETURN      0
; end of _I2C_LCD_Chr_Cp

_I2C_LCD_Init:

;lcd_i2c.h,103 :: 		void I2C_LCD_Init() {
;lcd_i2c.h,105 :: 		char rs = 0x00;
	CLRF        I2C_LCD_Init_rs_L0+0 
;lcd_i2c.h,107 :: 		Soft_I2C_Start();
	CALL        _Soft_I2C_Start+0, 0
;lcd_i2c.h,109 :: 		Soft_I2C_Write(LCD_ADDR);
	MOVLW       126
	MOVWF       FARG_Soft_I2C_Write_data_+0 
	CALL        _Soft_I2C_Write+0, 0
;lcd_i2c.h,112 :: 		Delay_ms(30);
	MOVLW       4
	MOVWF       R11, 0
	MOVLW       12
	MOVWF       R12, 0
	MOVLW       51
	MOVWF       R13, 0
L_I2C_LCD_Init16:
	DECFSZ      R13, 1, 1
	BRA         L_I2C_LCD_Init16
	DECFSZ      R12, 1, 1
	BRA         L_I2C_LCD_Init16
	DECFSZ      R11, 1, 1
	BRA         L_I2C_LCD_Init16
	NOP
	NOP
;lcd_i2c.h,114 :: 		Soft_I2C_Write(0x30 | rs | 0x04 | 0x08);
	MOVLW       48
	IORWF       I2C_LCD_Init_rs_L0+0, 0 
	MOVWF       FARG_Soft_I2C_Write_data_+0 
	BSF         FARG_Soft_I2C_Write_data_+0, 2 
	BSF         FARG_Soft_I2C_Write_data_+0, 3 
	CALL        _Soft_I2C_Write+0, 0
;lcd_i2c.h,116 :: 		Delay_us(50);
	MOVLW       2
	MOVWF       R12, 0
	MOVLW       75
	MOVWF       R13, 0
L_I2C_LCD_Init17:
	DECFSZ      R13, 1, 1
	BRA         L_I2C_LCD_Init17
	DECFSZ      R12, 1, 1
	BRA         L_I2C_LCD_Init17
;lcd_i2c.h,117 :: 		Soft_I2C_Write(0x30 | rs | 0x00 | 0x08);
	MOVLW       48
	IORWF       I2C_LCD_Init_rs_L0+0, 0 
	MOVWF       FARG_Soft_I2C_Write_data_+0 
	BSF         FARG_Soft_I2C_Write_data_+0, 3 
	CALL        _Soft_I2C_Write+0, 0
;lcd_i2c.h,120 :: 		Delay_ms(10);
	MOVLW       2
	MOVWF       R11, 0
	MOVLW       4
	MOVWF       R12, 0
	MOVLW       186
	MOVWF       R13, 0
L_I2C_LCD_Init18:
	DECFSZ      R13, 1, 1
	BRA         L_I2C_LCD_Init18
	DECFSZ      R12, 1, 1
	BRA         L_I2C_LCD_Init18
	DECFSZ      R11, 1, 1
	BRA         L_I2C_LCD_Init18
	NOP
;lcd_i2c.h,122 :: 		Soft_I2C_Write(0x30 | rs | 0x04 | 0x08);
	MOVLW       48
	IORWF       I2C_LCD_Init_rs_L0+0, 0 
	MOVWF       FARG_Soft_I2C_Write_data_+0 
	BSF         FARG_Soft_I2C_Write_data_+0, 2 
	BSF         FARG_Soft_I2C_Write_data_+0, 3 
	CALL        _Soft_I2C_Write+0, 0
;lcd_i2c.h,124 :: 		Delay_us(50);
	MOVLW       2
	MOVWF       R12, 0
	MOVLW       75
	MOVWF       R13, 0
L_I2C_LCD_Init19:
	DECFSZ      R13, 1, 1
	BRA         L_I2C_LCD_Init19
	DECFSZ      R12, 1, 1
	BRA         L_I2C_LCD_Init19
;lcd_i2c.h,125 :: 		Soft_I2C_Write(0x30 | rs | 0x00 | 0x08);
	MOVLW       48
	IORWF       I2C_LCD_Init_rs_L0+0, 0 
	MOVWF       FARG_Soft_I2C_Write_data_+0 
	BSF         FARG_Soft_I2C_Write_data_+0, 3 
	CALL        _Soft_I2C_Write+0, 0
;lcd_i2c.h,128 :: 		Delay_ms(10);
	MOVLW       2
	MOVWF       R11, 0
	MOVLW       4
	MOVWF       R12, 0
	MOVLW       186
	MOVWF       R13, 0
L_I2C_LCD_Init20:
	DECFSZ      R13, 1, 1
	BRA         L_I2C_LCD_Init20
	DECFSZ      R12, 1, 1
	BRA         L_I2C_LCD_Init20
	DECFSZ      R11, 1, 1
	BRA         L_I2C_LCD_Init20
	NOP
;lcd_i2c.h,130 :: 		Soft_I2C_Write(0x30 | rs | 0x04 | 0x08);
	MOVLW       48
	IORWF       I2C_LCD_Init_rs_L0+0, 0 
	MOVWF       FARG_Soft_I2C_Write_data_+0 
	BSF         FARG_Soft_I2C_Write_data_+0, 2 
	BSF         FARG_Soft_I2C_Write_data_+0, 3 
	CALL        _Soft_I2C_Write+0, 0
;lcd_i2c.h,132 :: 		Delay_us(50);
	MOVLW       2
	MOVWF       R12, 0
	MOVLW       75
	MOVWF       R13, 0
L_I2C_LCD_Init21:
	DECFSZ      R13, 1, 1
	BRA         L_I2C_LCD_Init21
	DECFSZ      R12, 1, 1
	BRA         L_I2C_LCD_Init21
;lcd_i2c.h,133 :: 		Soft_I2C_Write(0x30 | rs | 0x00 | 0x08);
	MOVLW       48
	IORWF       I2C_LCD_Init_rs_L0+0, 0 
	MOVWF       FARG_Soft_I2C_Write_data_+0 
	BSF         FARG_Soft_I2C_Write_data_+0, 3 
	CALL        _Soft_I2C_Write+0, 0
;lcd_i2c.h,136 :: 		Delay_ms(10);
	MOVLW       2
	MOVWF       R11, 0
	MOVLW       4
	MOVWF       R12, 0
	MOVLW       186
	MOVWF       R13, 0
L_I2C_LCD_Init22:
	DECFSZ      R13, 1, 1
	BRA         L_I2C_LCD_Init22
	DECFSZ      R12, 1, 1
	BRA         L_I2C_LCD_Init22
	DECFSZ      R11, 1, 1
	BRA         L_I2C_LCD_Init22
	NOP
;lcd_i2c.h,138 :: 		Soft_I2C_Write(0x20 | rs | 0x04 | 0x08);
	MOVLW       32
	IORWF       I2C_LCD_Init_rs_L0+0, 0 
	MOVWF       FARG_Soft_I2C_Write_data_+0 
	BSF         FARG_Soft_I2C_Write_data_+0, 2 
	BSF         FARG_Soft_I2C_Write_data_+0, 3 
	CALL        _Soft_I2C_Write+0, 0
;lcd_i2c.h,140 :: 		Delay_us(50);
	MOVLW       2
	MOVWF       R12, 0
	MOVLW       75
	MOVWF       R13, 0
L_I2C_LCD_Init23:
	DECFSZ      R13, 1, 1
	BRA         L_I2C_LCD_Init23
	DECFSZ      R12, 1, 1
	BRA         L_I2C_LCD_Init23
;lcd_i2c.h,141 :: 		Soft_I2C_Write(0x20 | rs | 0x00 | 0x08);
	MOVLW       32
	IORWF       I2C_LCD_Init_rs_L0+0, 0 
	MOVWF       FARG_Soft_I2C_Write_data_+0 
	BSF         FARG_Soft_I2C_Write_data_+0, 3 
	CALL        _Soft_I2C_Write+0, 0
;lcd_i2c.h,143 :: 		Soft_I2C_Stop();
	CALL        _Soft_I2C_Stop+0, 0
;lcd_i2c.h,145 :: 		Delay_ms(10);
	MOVLW       2
	MOVWF       R11, 0
	MOVLW       4
	MOVWF       R12, 0
	MOVLW       186
	MOVWF       R13, 0
L_I2C_LCD_Init24:
	DECFSZ      R13, 1, 1
	BRA         L_I2C_LCD_Init24
	DECFSZ      R12, 1, 1
	BRA         L_I2C_LCD_Init24
	DECFSZ      R11, 1, 1
	BRA         L_I2C_LCD_Init24
	NOP
;lcd_i2c.h,147 :: 		I2C_LCD_Cmd(0x28);
	MOVLW       40
	MOVWF       FARG_I2C_LCD_Cmd_out_char+0 
	CALL        _I2C_LCD_Cmd+0, 0
;lcd_i2c.h,148 :: 		I2C_LCD_Cmd(0x06);
	MOVLW       6
	MOVWF       FARG_I2C_LCD_Cmd_out_char+0 
	CALL        _I2C_LCD_Cmd+0, 0
;lcd_i2c.h,149 :: 		}
L_end_I2C_LCD_Init:
	RETURN      0
; end of _I2C_LCD_Init

_I2C_LCD_Out:

;lcd_i2c.h,151 :: 		void I2C_LCD_Out(char row, char col, char *text) {
;lcd_i2c.h,152 :: 		while(*text)
L_I2C_LCD_Out25:
	MOVFF       FARG_I2C_LCD_Out_text+0, FSR0
	MOVFF       FARG_I2C_LCD_Out_text+1, FSR0H
	MOVF        POSTINC0+0, 1 
	BTFSC       STATUS+0, 2 
	GOTO        L_I2C_LCD_Out26
;lcd_i2c.h,153 :: 		I2C_LCD_Chr(row, col++, *text++);
	MOVF        FARG_I2C_LCD_Out_row+0, 0 
	MOVWF       FARG_I2C_LCD_Chr_row+0 
	MOVF        FARG_I2C_LCD_Out_col+0, 0 
	MOVWF       FARG_I2C_LCD_Chr_column+0 
	MOVFF       FARG_I2C_LCD_Out_text+0, FSR0
	MOVFF       FARG_I2C_LCD_Out_text+1, FSR0H
	MOVF        POSTINC0+0, 0 
	MOVWF       FARG_I2C_LCD_Chr_out_char+0 
	CALL        _I2C_LCD_Chr+0, 0
	INCF        FARG_I2C_LCD_Out_col+0, 1 
	INFSNZ      FARG_I2C_LCD_Out_text+0, 1 
	INCF        FARG_I2C_LCD_Out_text+1, 1 
	GOTO        L_I2C_LCD_Out25
L_I2C_LCD_Out26:
;lcd_i2c.h,154 :: 		}
L_end_I2C_LCD_Out:
	RETURN      0
; end of _I2C_LCD_Out

_I2C_LCD_Out_Cp:

;lcd_i2c.h,156 :: 		void I2C_LCD_Out_Cp(char *text) {
;lcd_i2c.h,157 :: 		while(*text)
L_I2C_LCD_Out_Cp27:
	MOVFF       FARG_I2C_LCD_Out_Cp_text+0, FSR0
	MOVFF       FARG_I2C_LCD_Out_Cp_text+1, FSR0H
	MOVF        POSTINC0+0, 1 
	BTFSC       STATUS+0, 2 
	GOTO        L_I2C_LCD_Out_Cp28
;lcd_i2c.h,158 :: 		I2C_LCD_Chr_Cp(*text++);
	MOVFF       FARG_I2C_LCD_Out_Cp_text+0, FSR0
	MOVFF       FARG_I2C_LCD_Out_Cp_text+1, FSR0H
	MOVF        POSTINC0+0, 0 
	MOVWF       FARG_I2C_LCD_Chr_Cp_out_char+0 
	CALL        _I2C_LCD_Chr_Cp+0, 0
	INFSNZ      FARG_I2C_LCD_Out_Cp_text+0, 1 
	INCF        FARG_I2C_LCD_Out_Cp_text+1, 1 
	GOTO        L_I2C_LCD_Out_Cp27
L_I2C_LCD_Out_Cp28:
;lcd_i2c.h,159 :: 		}
L_end_I2C_LCD_Out_Cp:
	RETURN      0
; end of _I2C_LCD_Out_Cp

_main:

;I2C LCD.c,48 :: 		void main() {
;I2C LCD.c,49 :: 		ADCON1 |= 0x0F;
	MOVLW       15
	IORWF       ADCON1+0, 1 
;I2C LCD.c,50 :: 		CMCON  |= 7;
	MOVLW       7
	IORWF       CMCON+0, 1 
;I2C LCD.c,52 :: 		TRISA =0x00;
	CLRF        TRISA+0 
;I2C LCD.c,53 :: 		TRISB=0x21;
	MOVLW       33
	MOVWF       TRISB+0 
;I2C LCD.c,54 :: 		TRISC=0x00;
	CLRF        TRISC+0 
;I2C LCD.c,55 :: 		TRISD=0x00;
	CLRF        TRISD+0 
;I2C LCD.c,57 :: 		PORTA=0x00;
	CLRF        PORTA+0 
;I2C LCD.c,58 :: 		PORTB=0x00;
	CLRF        PORTB+0 
;I2C LCD.c,59 :: 		PORTC=0b01000000;
	MOVLW       64
	MOVWF       PORTC+0 
;I2C LCD.c,60 :: 		PORTD=0x00;
	CLRF        PORTD+0 
;I2C LCD.c,62 :: 		I2C_LCD_Init();
	CALL        _I2C_LCD_Init+0, 0
;I2C LCD.c,63 :: 		I2C_LCD_Cmd(_LCD_CURSOR_OFF);
	MOVLW       12
	MOVWF       FARG_I2C_LCD_Cmd_out_char+0 
	CALL        _I2C_LCD_Cmd+0, 0
;I2C LCD.c,64 :: 		I2C_LCD_Cmd(_LCD_CLEAR);
	MOVLW       1
	MOVWF       FARG_I2C_LCD_Cmd_out_char+0 
	CALL        _I2C_LCD_Cmd+0, 0
;I2C LCD.c,74 :: 		SPI1_Init();
	CALL        _SPI1_Init+0, 0
;I2C LCD.c,75 :: 		SPI1_Init_Advanced(_SPI_MASTER_OSC_DIV64, _SPI_DATA_SAMPLE_MIDDLE, _SPI_CLK_IDLE_LOW, _SPI_LOW_2_HIGH);
	MOVLW       2
	MOVWF       FARG_SPI1_Init_Advanced_master+0 
	CLRF        FARG_SPI1_Init_Advanced_data_sample+0 
	CLRF        FARG_SPI1_Init_Advanced_clock_idle+0 
	MOVLW       1
	MOVWF       FARG_SPI1_Init_Advanced_transmit_edge+0 
	CALL        _SPI1_Init_Advanced+0, 0
;I2C LCD.c,76 :: 		Delay_us(100);
	MOVLW       3
	MOVWF       R12, 0
	MOVLW       151
	MOVWF       R13, 0
L_main29:
	DECFSZ      R13, 1, 1
	BRA         L_main29
	DECFSZ      R12, 1, 1
	BRA         L_main29
	NOP
	NOP
;I2C LCD.c,78 :: 		do{
L_main30:
;I2C LCD.c,79 :: 		I2C_LCD_Cmd(_LCD_CLEAR);
	MOVLW       1
	MOVWF       FARG_I2C_LCD_Cmd_out_char+0 
	CALL        _I2C_LCD_Cmd+0, 0
;I2C LCD.c,80 :: 		I2C_Lcd_Out(1,1,"NAO ENCONTRADO");
	MOVLW       1
	MOVWF       FARG_I2C_LCD_Out_row+0 
	MOVLW       1
	MOVWF       FARG_I2C_LCD_Out_col+0 
	MOVLW       ?lstr1_I2C_32LCD+0
	MOVWF       FARG_I2C_LCD_Out_text+0 
	MOVLW       hi_addr(?lstr1_I2C_32LCD+0)
	MOVWF       FARG_I2C_LCD_Out_text+1 
	CALL        _I2C_LCD_Out+0, 0
;I2C LCD.c,81 :: 		error = MMC_Init();
	CALL        _Mmc_Init+0, 0
	MOVF        R0, 0 
	MOVWF       _error+0 
;I2C LCD.c,82 :: 		delay_ms(1000);
	MOVLW       102
	MOVWF       R11, 0
	MOVLW       118
	MOVWF       R12, 0
	MOVLW       193
	MOVWF       R13, 0
L_main33:
	DECFSZ      R13, 1, 1
	BRA         L_main33
	DECFSZ      R12, 1, 1
	BRA         L_main33
	DECFSZ      R11, 1, 1
	BRA         L_main33
;I2C LCD.c,84 :: 		while(error);
	MOVF        _error+0, 1 
	BTFSS       STATUS+0, 2 
	GOTO        L_main30
;I2C LCD.c,87 :: 		I2C_LCD_Cmd(_LCD_CLEAR);
	MOVLW       1
	MOVWF       FARG_I2C_LCD_Cmd_out_char+0 
	CALL        _I2C_LCD_Cmd+0, 0
;I2C LCD.c,88 :: 		I2C_Lcd_Out(1,1,"CARTAO DETECTADO");
	MOVLW       1
	MOVWF       FARG_I2C_LCD_Out_row+0 
	MOVLW       1
	MOVWF       FARG_I2C_LCD_Out_col+0 
	MOVLW       ?lstr2_I2C_32LCD+0
	MOVWF       FARG_I2C_LCD_Out_text+0 
	MOVLW       hi_addr(?lstr2_I2C_32LCD+0)
	MOVWF       FARG_I2C_LCD_Out_text+1 
	CALL        _I2C_LCD_Out+0, 0
;I2C LCD.c,89 :: 		I2C_Lcd_Out(2,1,"INICIALIZADO");
	MOVLW       2
	MOVWF       FARG_I2C_LCD_Out_row+0 
	MOVLW       1
	MOVWF       FARG_I2C_LCD_Out_col+0 
	MOVLW       ?lstr3_I2C_32LCD+0
	MOVWF       FARG_I2C_LCD_Out_text+0 
	MOVLW       hi_addr(?lstr3_I2C_32LCD+0)
	MOVWF       FARG_I2C_LCD_Out_text+1 
	CALL        _I2C_LCD_Out+0, 0
;I2C LCD.c,90 :: 		Delay_ms(1000);
	MOVLW       102
	MOVWF       R11, 0
	MOVLW       118
	MOVWF       R12, 0
	MOVLW       193
	MOVWF       R13, 0
L_main34:
	DECFSZ      R13, 1, 1
	BRA         L_main34
	DECFSZ      R12, 1, 1
	BRA         L_main34
	DECFSZ      R11, 1, 1
	BRA         L_main34
;I2C LCD.c,167 :: 		}
L_end_main:
	GOTO        $+0
; end of _main
