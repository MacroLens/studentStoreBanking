import subprocess
output = open('output', 'w+');# Check for output file, if none make one and give write privielges.
try:
    var = subprocess.check_output('./quick_start_example1').decode('utf-8').strip(); # declare variable var, read the output of quick_start_example1 script and decode it from the UTF-8 format and strip it of any extra trailing characters like line breaks
    hex_list = var.split();#takes the string, splits it by spaces, and makes it into a list
    for x in range(len(hex_list)): #for every hex number in the list go through it and turn it into a decimal interger
        hex_list[x] = int(hex_list[x], 16) # converts Hexidecimal to decimal so it's easy to mess with.
    nfcUID = hex_list[3]; # Creating a unique code to identify a card, take the decimals and bitshift them around
    nfcUID <<= 8; nfcUID |= hex_list[2];# Shift left 8 bits, += the third decimal
    nfcUID <<= 8; nfcUID |= hex_list[1];# etc
    nfcUID <<= 8; nfcUID |= hex_list[0];# etc
    #print(nfcUID)
    #print(hex_list)
    output.write(str(nfcUID)); # Writes to the output file the nfcUID
except (OSError, subprocess.CalledProcessError) as e:
    print(e)
    #print("error: may not be able to read card. check card reader connection")
