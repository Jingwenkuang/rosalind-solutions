decode 97 from 0000 0110 0001
#read from right to left

Bit (position)  hex value     meaning                set in 97?
0 (rightmost)   0x1           read paired            Yes
1               0x2           properly paired        No
2               0x4           read unmapped          No
3               0x8           mate unmapped          No
4               0x10          read reverse strand    No
5               0x20          mate reverse strand    Yes
6               0x40          first in pair          Yes
7               0x80          second in pair          No
8               0x100         not primary alignment   No 
9               0x200         QC fail                 No 
10              0x400         PCR/optical duplicate   No
11              0x800         supplementary alignment No 
