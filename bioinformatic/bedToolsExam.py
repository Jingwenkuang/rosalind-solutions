1. How many alignments does the set contain? 
    % samtools flagstat athal_wu_0_A.bam     #221372
         or
    % samtools view athal_wu_0_A.bam | wc -l

2. How many alignments show the read’s mate unmapped?
    % samtools view athal_wu_0_A.bam | cut -f7 | grep -c '*' #65521

3. How many alignments contain a deletion (D)? 
    % samtools view athal_wu_0_A.bam | cut -f6 | grep -c 'D'  #2451

4. How many alignments show the read’s mate mapped to the same chromosome?
    % samtools view athal_wu_0_A.bam | cut -f7 | grep -c '=' #150913

5. How many alignments are spliced?
    % samtools view athal_wu_0_A.bam | cut -f6 | grep -c 'N'  #0

6. How many alignments does the set contain?
    % samtools sort athal_wu_0_A.bam -o athal_wu_0_A.sorted.bam
    % samtools index athal_wu_0_A.sorted.bam
    % samtools view -b athal_wu_0_A.sorted.bam “Chr3:11777000-11794000” > athal_wu_0_A.region.bam
    % samtools flagstat athal_wu_0_A.region.bam         #7081

7. How many alignments show the read’s mate unmapped?
    % samtools view athal_wu_0_A.region.bam | cut -f7 | grep -c '*' #1983

8. How many alignments contain a deletion (D)?
    % samtools view athal_wu_0_A.region.bam | cut -f6 | grep -c 'D' #31

9. How many alignments show the read’s mate mapped to the same chromosome?
    % samtools view athal_wu_0_A.region.bam | cut -f7 | grep -c '=' #4670

10. How many alignments are spliced?
    % samtools view athal_wu_0_A.region.bam | cut -f7 | grep -c 'N' #0

11. How many sequences are in the genome file? 
    % samtools view -H athal_wu_0_A.bam | grep -c 'SN' #7

12. What is the length of the first sequence in the genome file?
    % samtools view –H athal_wu_0_A.bam | grep “SN:” | more #29923332