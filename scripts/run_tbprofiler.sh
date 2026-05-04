#!/bin/bash
set -euo pipefail

export JAVA_HOME=/usr/lib/jvm/java-21-openjdk
export PATH=$JAVA_HOME/bin:$PATH

TRIMMED_DIR="data/trimmed"
OUT_DIR="results/tbprofiler"

mkdir -p "$OUT_DIR"

while IFS= read -r acc || [ -n "$acc" ]; do
  [[ -z "$acc" ]] && continue

  # Skip if already processed
  if [[ -f "$OUT_DIR/results/${acc}.results.json" ]]; then
    echo "Skipping $acc — already processed"
    continue
  fi

  echo "------------------------------------------"
  echo "Processing: $acc"
  echo "------------------------------------------"

  tb-profiler profile \
    -1 "$TRIMMED_DIR/${acc}_1_paired.fastq.gz" \
    -2 "$TRIMMED_DIR/${acc}_2_paired.fastq.gz" \
    --prefix "$acc" \
    --dir "$OUT_DIR" \
    --threads 2 \
    --csv \
    --call_whole_genome \
    --no_delly \
    2>>"logs/${acc}_tbprofiler.log"

done <"data/SRR_Acc_List.txt"

echo "TB-Profiler complete. Collating results..."

tb-profiler collate --dir "$OUT_DIR" --prefix tbprofiler_summary

echo "Done. Summary files in current directory."
mv tbprofiler_summary* "$OUT_DIR/" 2>/dev/null || true
