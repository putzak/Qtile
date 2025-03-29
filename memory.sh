#!/bin/bash
MemUsed=$(free | awk 'FNR == 2 {print $3}')
MemTotal=$(free | awk 'FNR == 2 {print $2}')
FracUsed=$(bc <<< "scale=2 ; $MemUsed / $MemTotal")
echo $(bc <<< "scale=2 ; 100 * $FracUsed")
