#!/usr/bin/env python

import re
from pprint import pprint

regexp = re.compile(
    r'^'
    r'(?=.*[a-z])'
    r'(?=.*[A-Z])'
    r'(?=.*[0-9])'
    r'(?=.*[ -\/:-@[-`{-~])'
    r'.{12,}'
    r'$',
    flags=re.M
)

string = '''
VÁLIDAS
6<s3Wk1v>ML?
QO71zk6,P;:w
+u`2e;OpO41T
}q1|P09W;lpN
0rL^"Q}B4q8c
::ggzu[6sgwW
SEM MINÚSCULAS
:3Q2>8~JQ^6R
!698/)Q6D\EA
#C111#B\K7$L
174]C1.\PTG^
?71Q\\E'FB99
*D)FI&KE:8$6#S
O(W*IG*}&|UR?G
IIG?L{^U6FZ4%E
SEM MINÚSCULAS E NÚMEROS
P?((}HB$CE%N
LP}|N\V^\?LZ
CRQ_FX^S_~\\
_`L+O'J[~NBI
XR]L}`DC$S~|
SEM NÚMEROS CARACTERES E MINÚSCULAS
RJUWEYGEWSSA
VXTJCDRTIKRT
QGDPAYHQVUTO
YJJGEUPBBSDM
DFLKZZKGOQSP
QUANTIDADE INVÁLIDA (6)
{jr4E0
vzK2=6
95;Pog
0>Zzj3
y9-iW1
'''

pprint(regexp.findall(string))