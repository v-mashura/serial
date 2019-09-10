# serial-rci.py
This is python script for getting data from Linx industrial coding printers and marking machines over Remote
Communications Interface (RCI). The value returned is the total print count for the printer.
# how it works
To get print count value we send command 8 to printer’s serial port (rs232), hex sequence is 
- 1b 02 08 1b 03 where
- 1b 02 – begin
- 08 – command to read count value
- 1b 03 – end
Then we receive answer 1b 06 00 00 08 3a 41 bb 01 1b 03 where payload is 3a 41 bb 01 and it can be converted to 29049146 (DCBA).
