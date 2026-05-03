#!/bin/bash

ACC_LIST="data/SRR_Acc_List.txt"
OUT_DIR="data/raw"

mkdir -p "$OUT_DIR"

while IFS= read -r accession || [ -n "$accession" ]; do
  [[ -z "$accession" ]] && continue

  echo "------------------------------------------"
  echo "Processing: $accession"
  echo "------------------------------------------"

  # 1. Prefetch the .sra file (Compressed)
  prefetch "$accession" -O "$OUT_DIR"

  # 2. Extract to FASTQ (Uncompressed)
  # --split-files: essential for paired-end
  # --skip-technical: removes non-biological data to save space
  fasterq-dump "$accession" --split-files --outdir "$OUT_DIR" --skip-technical

  # 3. Optional: Remove the .sra file to save disk space
  # Once extracted to .fastq, the .sra file is redundant.
  # rm -rf "$OUT_DIR/$accession"

done <"$ACC_LIST"
