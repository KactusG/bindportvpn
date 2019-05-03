!/bin/bash

MYIP=$(wget -O - -q icanhazip.com);
echo $MYIP > ip.txt
