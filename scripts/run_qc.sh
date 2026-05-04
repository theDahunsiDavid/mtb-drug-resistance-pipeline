#!/bin/bash
set -euo pipefail

RAW_DIR="data/raw"
TRIMMED_DIR="data/trimmed"
QC_RAW_DIR="results/qc/raw"
QC_TRIMMED_DIR="results/qc/trimmed"
ADAPTERS="$CONDA_PREFIX/share/trimmomatic/adapters/NexteraPE-PE.fa"

mkdir -p "$TRIMMED_DIR" "$QC_RAW_DIR" "$QC_TRIMMED_DIR"

while IFS= read -r acc || [ -n "$acc" ]; do
  [[ -z "$acc" ]] && continue

  # Skip if already trimmed
  if [[ -f "$TRIMMED_DIR/${acc}_1_paired.fastq.gz" && -f "$TRIMMED_DIR/${acc}_2_paired.fastq.gz" ]]; then
    echo "Skipping $acc — already trimmed"
    continue
  fi

  echo "------------------------------------------"
  echo "Processing: $acc"
  echo "------------------------------------------"

  # FastQC on raw reads
  fastqc "$RAW_DIR/${acc}_1.fastq" "$RAW_DIR/${acc}_2.fastq" \
    --outdir "$QC_RAW_DIR" --threads 2

  # Trimmomatic
  trimmomatic PE \
    "$RAW_DIR/${acc}_1.fastq" "$RAW_DIR/${acc}_2.fastq" \
    "$TRIMMED_DIR/${acc}_1_paired.fastq.gz" "$TRIMMED_DIR/${acc}_1_unpaired.fastq.gz" \
    "$TRIMMED_DIR/${acc}_2_paired.fastq.gz" "$TRIMMED_DIR/${acc}_2_unpaired.fastq.gz" \
    ILLUMINACLIP:"$ADAPTERS":2:30:10 \
    LEADING:3 TRAILING:3 SLIDINGWINDOW:4:20 MINLEN:36 \
    2>>"logs/${acc}_trimmomatic.log"

  # Remove raw FASTQs after successful trimming to save disk space
  rm -f "$RAW_DIR/${acc}_1.fastq" "$RAW_DIR/${acc}_2.fastq"
  echo "Removed raw FASTQs for $acc"

  # FastQC on trimmed reads
  fastqc "$TRIMMED_DIR/${acc}_1_paired.fastq.gz" "$TRIMMED_DIR/${acc}_2_paired.fastq.gz" \
    --outdir "$QC_TRIMMED_DIR" --threads 2

done <"data/SRR_Acc_List.txt"
