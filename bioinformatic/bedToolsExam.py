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

13. What alignment tool was used?
    % samtools view -H athal_wu_0_A.bam | grep 'PG'
    #stampy

14. What is the read identifier (name) for the first alignment?
    % samtools view athal_wu_0_A.bam | head -1 | cut -f1
        #GAII05_0002:1:113:7822:3886#0

15. What is the start position of this read’s mate on the genome? Give this as ‘chrom:pos’ if the read was mapped, or ‘*” if unmapped.
    % samtools view athal_wu_0_A.bam | head -n 1
    # Chr3:11700332

16. How many overlaps (each overlap is reported on one line) are reported?
    % bedtools intersect –abam athal_wu_0_A.sorted.bam –b athal_wu_0_A_annot.gtf –bed -wo > overlaps.bed
    % wc –l overlaps.bed  #3101

17. How many of these are 10 bases or longer?
    % cut -f22 overlaps.bed | grep -E '^[0-9]{2,}$' | wc -l # 2899


18. How many alignments overlap the annotations?
    % cut -f1-12 overlaps.bed | sort -u | wc -l #3101

19. Conversely, how many exons have reads mapped to them?
    % cut -f13-21 overlaps.bed | sort -u | wc -l #21

20. If you were to convert the transcript annotations in the file “athal_wu_0_A_annot.gtf” into BED format, how many BED records would be generated?
    % cut –f9 athal_wu_0_A_annot.gtf | cut –d ‘ ‘ –f1,2 | sort –u | wc -l #4