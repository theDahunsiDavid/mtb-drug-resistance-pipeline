import marimo

__generated_with = "0.23.4"
app = marimo.App(width="medium")


@app.cell
def _():
    import pandas as pd
    import matplotlib.pyplot as plt
    import matplotlib.patches as mpatches
    import seaborn as sns
    import numpy as np
    from pathlib import Path

    # Paths
    SUMMARY_CSV = Path("results/tbprofiler/tbprofiler_summary.csv")
    FIGURES_DIR = Path("results/figures")
    FIGURES_DIR.mkdir(parents=True, exist_ok=True)

    # Load data
    df = pd.read_csv(SUMMARY_CSV)
    print(f"Loaded {len(df)} samples")
    print(df[["sample", "main_lineage", "drtype"]].to_string(index=False))
    return FIGURES_DIR, df, mpatches, pd, plt, sns


@app.cell
def _(df, pd):
    # Define the drugs we care about
    DRUGS = [
        "rifampicin", "isoniazid", "ethambutol", "pyrazinamide",
        "moxifloxacin", "levofloxacin", "bedaquiline", "delamanid",
        "streptomycin", "amikacin", "kanamycin", "ethionamide"
    ]

    # Create binary resistance matrix (1 = resistant, 0 = susceptible)
    def is_resistant(val):
        if pd.isna(val) or str(val).strip() == "-":
            return 0
        return 1

    resist_df = df[["sample", "main_lineage", "sub_lineage", "drtype"]].copy()
    for drug in DRUGS:
        if drug in df.columns:
            resist_df[drug] = df[drug].apply(is_resistant)

    print(resist_df[["sample"] + DRUGS].to_string(index=False))
    return DRUGS, resist_df


@app.cell
def _(DRUGS, FIGURES_DIR, mpatches, plt, resist_df):
    # Figure 1: Resistance frequency per drug
    drug_resistance_freq = resist_df[DRUGS].mean() * 100
    drug_resistance_freq = drug_resistance_freq.sort_values(ascending=False)

    fig1, ax1 = plt.subplots(figsize=(12, 6))
    bars = ax1.bar(
        drug_resistance_freq.index,
        drug_resistance_freq.values,
        color=["#d32f2f" if v == 100 else "#f57c00" if v >= 50 else "#388e3c" 
               for v in drug_resistance_freq.values],
        edgecolor="white",
        linewidth=0.8
    )

    ax1.set_xlabel("Drug", fontsize=12, labelpad=10)
    ax1.set_ylabel("Samples Resistant (%)", fontsize=12, labelpad=10)
    ax1.set_title("Drug Resistance Frequency Across 15 South African MTB Isolates", 
                 fontsize=14, fontweight="bold", pad=15)
    ax1.set_ylim(0, 110)
    ax1.tick_params(axis="x", rotation=45)

    for bar, val in zip(bars, drug_resistance_freq.values):
        ax1.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1.5,
                f"{val:.0f}%", ha="center", va="bottom", fontsize=9, fontweight="bold")

    legend_elements1 = [
        mpatches.Patch(color="#d32f2f", label="100% resistant"),
        mpatches.Patch(color="#f57c00", label="≥50% resistant"),
        mpatches.Patch(color="#388e3c", label="<50% resistant")
    ]
    ax1.legend(handles=legend_elements1, loc="upper right", fontsize=9)

    plt.tight_layout()
    plt.savefig(FIGURES_DIR / "fig1_resistance_frequency.png", dpi=300, bbox_inches="tight")
    plt.show()
    print("Figure 1 saved.")
    return


@app.cell
def _(FIGURES_DIR, plt, resist_df):
    # Figure 2: Lineage distribution
    lineage_counts = resist_df["main_lineage"].value_counts()
    lineage_labels = {
        "lineage1": "Lineage 1\n(Indo-Oceanic)",
        "lineage2": "Lineage 2\n(East Asian/Beijing)",
        "lineage4": "Lineage 4\n(Euro-American)"
    }
    labels = [lineage_labels.get(l, l) for l in lineage_counts.index]
    colors = ["#1565c0", "#6a1b9a", "#2e7d32"]

    fig2, ax2 = plt.subplots(figsize=(8, 8))
    wedges, texts, autotexts = ax2.pie(
        lineage_counts.values,
        labels=labels,
        autopct="%1.0f%%",
        colors=colors,
        startangle=140,
        pctdistance=0.75,
        wedgeprops={"edgecolor": "white", "linewidth": 2}
    )

    for text in texts:
        text.set_fontsize(11)
    for autotext in autotexts:
        autotext.set_fontsize(12)
        autotext.set_fontweight("bold")
        autotext.set_color("white")

    ax2.set_title("Lineage Distribution Across 15 South African MTB Isolates",
                 fontsize=14, fontweight="bold", pad=20)

    count_str = "\n".join([f"{lineage_labels.get(l, l).replace(chr(10), ' ')}: n={c}" 
                            for l, c in lineage_counts.items()])
    ax2.text(1.3, -1.1, count_str, fontsize=9, verticalalignment="bottom",
            bbox=dict(boxstyle="round", facecolor="lightgrey", alpha=0.5))

    plt.tight_layout()
    plt.savefig(FIGURES_DIR / "fig2_lineage_distribution.png", dpi=300, bbox_inches="tight")
    plt.show()
    print("Figure 2 saved.")
    return


@app.cell
def _(DRUGS, FIGURES_DIR, mpatches, plt, resist_df, sns):
    # Figure 3: Per-sample resistance heatmap
    heatmap_data = resist_df.set_index("sample")[DRUGS]

    # Sort samples by drtype severity
    drtype_order = {"XDR-TB": 0, "Pre-XDR-TB": 1, "MDR-TB": 2, "RR-TB": 3}
    sample_order = resist_df.assign(
        drtype_rank=resist_df["drtype"].map(drtype_order)
    ).sort_values(["drtype_rank", "main_lineage"])["sample"]
    heatmap_data = heatmap_data.loc[sample_order]

    # Add lineage and drtype annotations
    row_labels = [
        f"{s}  [{resist_df.loc[resist_df['sample']==s, 'main_lineage'].values[0].replace('lineage','')} | {resist_df.loc[resist_df['sample']==s, 'drtype'].values[0]}]"
        for s in heatmap_data.index
    ]

    fig3, ax3 = plt.subplots(figsize=(14, 8))
    sns.heatmap(
        heatmap_data,
        ax=ax3,
        cmap=["#f5f5f5", "#c62828"],
        linewidths=0.5,
        linecolor="white",
        cbar=False,
        yticklabels=row_labels,
        xticklabels=[d.replace("-", "\n") for d in DRUGS]
    )

    ax3.set_title("Per-Sample Drug Resistance Profile Across 15 South African MTB Isolates",
                  fontsize=14, fontweight="bold", pad=15)
    ax3.set_xlabel("Drug", fontsize=12, labelpad=10)
    ax3.set_ylabel("")
    ax3.tick_params(axis="x", labelsize=9)
    ax3.tick_params(axis="y", labelsize=8)

    legend_elements3 = [
        mpatches.Patch(color="#c62828", label="Resistant"),
        mpatches.Patch(color="#f5f5f5", label="Susceptible")
    ]
    ax3.legend(handles=legend_elements3, loc="upper right",
               bbox_to_anchor=(1.15, 1.1), fontsize=10)

    plt.tight_layout()
    plt.savefig(FIGURES_DIR / "fig3_resistance_heatmap.png", dpi=300, bbox_inches="tight")
    plt.show()
    print("Figure 3 saved.")
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
