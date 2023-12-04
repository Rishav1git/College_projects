This is the Mini Project made by me 
It is a simple 16 bit microprocessor Build in iverilog 
It can do some operation such as ADD,SUB,AND,OR 
Output for this can Be seen in gtkwave refer to table given how it works the operation and refer screenshot to see Output

Running commands are:
1. iverilog -o test .\alu.v .\lib.v .\memory.v .\pc.v .\reg_alu.v .\16-bit_RISC_processor.v .\tb_16-bit_RISC_processor.v
2. vvp test(to  know the dumpfile name)
3. gtkwave <dumpfile filename>

Note : This all I runned in Linux u can try it in other operating system by changing some of commands
Note: This is Just a Mini Project So It cant be used for real microprocessor design

Author : Rishav Kumar Agrawal