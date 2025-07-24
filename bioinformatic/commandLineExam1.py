1. How many chromosomes are there in the genome?
    % grep -c ">" apple.genome #3

# geneID        transcriptID chrom strand transcriptStart transcriptEnd transcriptStructure 
# MDP0000303933 MDP0000303933 chr1  -      4276            5447          (4276-4368,4423-4542,4733-4911,5321-5447)
2. How many genes?
    % cut -f1 apple.genes | sort -u | wc -l 
        or 
    % cut -f1 apple.genes | uniq | wc -l   #5453

3. How many transcript variants?
    % cut -f2 apple.genes | sort -u | wc -l 
        or 
    % cut -f2 apple.genes | uniq | wc -l   #5456

4. How many genes have a single splice variant?
    % cut -f1 apple.genes | sort | uniq -c | grep -c “ 1 “ #5450

5. How may genes have 2 or more splice variants?
    % cut -f1 apple.genes | sort | uniq -c | grep -v “ 1 “ | wc -l #3


    % cut -f1,4 apple.genes | sort -u | cut -f2 | sort | uniq -c #For question 6 and 7
6. How many genes are there on the '+' strand?
    % cut -f1,4 apple.genes | sort -u | cut -f2 | grep -c "+" #2662
7. How many genes are there on the '-' strand?
    % cut -f1,4 apple.genes | sort -u | cut -f2 | grep -c "-" #2791


    % cut -f1,3 apple.genes | sort -u | cut -f2 | sort | uniq -c # For question 8,9 and 10
8. How many genes are there on chromosome chr1? 
    % cut -f1,3 apple.genes | sort -u | cut -f2 | grep -c "chr1" #1624
9. How many genes are there on chromosome chr2?
    % cut -f1,3 apple.genes | sort -u | cut -f2 | grep -c "chr2" #2058
10. How many genes are there on chromosome chr3?
    % cut -f1,3 apple.genes | sort -u | cut -f2 | grep -c "chr3" #1771


    % cut -f2,3 apple.genes | sort -u | cut -f2 |sort | uniq -c # For question 11,12 and 13
11. How many transcripts are there on chr1?
    % cut -f2,3 apple.genes | sort -u | cut -f2 | grep -c "chr1" #1625
12. How many transcripts are there on chr2?
    % cut -f2,3 apple.genes | sort -u | cut -f2 | grep -c "chr2" #2059
13. How many transcripts are there on chr3?
    % cut -f2,3 apple.genes | sort -u | cut -f2 | grep -c "chr3" #1772



14. How many genes are in common between condition A and condition B?
    % cut -f1 apple.conditionA | sort -u > apple.conditionA.sorted.genes
    % cut -f1 apple.conditionB | sort -u > apple.conditionB.sorted.genes
    % comm -1 -2 apple.conditionA.sorted.genes apple.conditionB.sorted.genes | wc -l #2410

15. How many genes are exclusively specific to condition A? 
    % comm -2 -3 apple.conditionA.sorted.genes apple.conditionB.sorted.genes | wc -l #1205

16. How many genes are exclusively specific to condition B?
    % comm -1 -3 apple.conditionA.sorted.genes apple.conditionB.sorted.genes | wc -l #1243

17. How many genes are in common to all three conditions?
    % cut -f1 apple.conditionC | sort -u > apple.conditionC.sorted.genes
    % cat apple.conditionA.sorted.genes apple.conditionB.sorted.genes apple.conditionC.sorted.genes | sort | uniq -c | grep -c " 3 "
    or
    % cat apple.condition{A,B,C}.sorted.genes | sort | uniq -c | grep -c " 3 " #1608