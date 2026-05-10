# Biological Interpretation Report

## Drug Resistance Profiling of Mycobacterium tuberculosis Genomes

**Pipeline:** TB-Profiler v6.3.0 | **Database:** tbdb (commit 72ef6fa, July 2024)
**Samples:** 15 paired-end Illumina WGS isolates | **Origin:** South Africa (BioProject PRJNA1256480)

---

## 1. Background

Tuberculosis (TB), caused by _Mycobacterium tuberculosis_ (MTB), is the world's leading cause of death from a single infectious agent. It was also the leading killer of people with HIV in 2024 [1]. Unfortunately, 69% of all HIV-associated TB cases in the world occur in the African Region, with South Africa being heavily affected [2].

It takes a standard 6-month regimen to treat drug-susceptible TB. However, mutations in certain MTB genes are fueling the emergence of drug-resistant TB. First-line drugs are ineffective against drug-resistant TB, so clinicians have to resort to later-generation drugs that are more expensive and toxic [3]. Additionally, treatment with these later-generation drugs can take up to 18–24 months [2].

Diagnosing TB is another hurdle. TB is an airborne disease, but it develops slowly. Traditional solid media culturing (in the lab) takes 4–6 weeks. Identifying which drugs a cultured isolate is resistant to also adds more weeks to the timeline [4]. Fortunately, recent progress in computational genomics offers a faster alternative. Whole-genome sequencing (WGS) of MTB, along with bioinformatics tools like TB-Profiler, makes it easier to comprehensively profile resistance directly from a cultured isolate. These tools can also do lineage classification and variant-level resolution of resistance mechanisms [5].

For this project, samples were drawn from BioProject PRJNA1256480 (B-Prepared, Columbia University), a whole-genome sequencing dataset of South African TB isolates deposited in April 2025 [6]. No associated publication was available at the time of analysis.

---

## 2. Lineage Distribution

To reflect the evolutionary history and geographic spread of the different TB strains in this cohort, it is important to classify the MTB isolates within the global phylogeny of the M. tuberculosis complex. The distribution of these lineages is summarized in Figure 1 below.

![Figure 1: Lineage Distribution across 15 South African MTB isolates](results/figures/fig2_lineage_distribution.png)

Of the 15 isolates analyzed:

- **Lineage 4 (Euro-American): n=7 (47%)**: This lineage is the most globally widespread lineage. It is dominant across sub-Saharan Africa, including South Africa, and it is associated with high transmissibility [7].

- **Lineage 2 (East-Asian/Beijing): n=7 (47%)**: This lineage is strongly associated with drug-resistance acquisition. It has been linked to outbreaks of multi-drug resistant TB (MDR-TB) and extensively drug-resistant TB (XDR-TB) in South Africa, especially in the Western Cape and KwaZulu-Natal provinces [8].

- **Lineage 1 (Indo-Oceanic): n=1 (7%)**: This is an ancestral lineage with restricted global distribution. Its presence in this South African cohort is likely due to importation or localised transmission.

The equal split between Lineage 2 and Lineage 4 is consistent with the high-resistance burden that's observed in this cohort, seeing as Lineage 2 is strongly associated with drug-resistance acquisition.

---

## 3. Drug Resistance Patterns

### 3.1 Resistance Classification

TB-Profiler classified the 15 isolates into resistance categories according to the updated WHO definitions [9].

| Category                                       | Definition                                                                                            | Count |
| ---------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ----- |
| Extensively Drug-Resistant TB (XDR-TB)         | Resistant to rifampicin, isoniazid, any fluoroquinolone, and at least one of bedaquiline or linezolid | 8     |
| Pre-Extensively Drug-Resistant TB (Pre-XDR-TB) | Resistant to rifampicin, isoniazid, and any fluoroquinolone                                           | 3     |
| Multidrug-Resistant TB (MDR-TB)                | Resistant to at least rifampicin and isoniazid                                                        | 2     |
| Rifampicin-Resistant TB (RR-TB)                | Rifampicin-resistant only                                                                             | 2     |

The predominance of XDR-TB (53% of isolates) in this cohort reflects high drug resistance in the B-Prepared dataset. Nonetheless, this is consistent with the documented XDR-TB burden in South Africa, where the country accounts for a disproportionate share of global XDR-TB cases [2, 10].

### 3.2 Resistance Frequency by Drug

The frequency of resistance in the analyzed isolates to 12 TB-treatment drugs are summarized in Figure 2 below.

![Figure 2: Drug Resistance Frequency across 15 MTB isolates](results/figures/fig1_resistance_frequency.png)

**Rifampicin (100%):** All 15 isolates were resistant to rifampicin. However, this is expected as the samples seem to be from a high-resistance setting. Rifampicin resistance is mainly caused by mutations in the _rpoB_ gene (the gene that encodes the beta subunit of RNA polymerase). The most common mutation observed was _rpoB_ p.Ser450Leu, which is a canonical resistance-conferring substitution at codon 450 of the rifampicin resistance-determining region (RRDR) [11].

**Isoniazid (87%):** 13 of the 15 isolates were isoniazid resistant. This resistance is mainly caused by _katG_ p.Ser315Thr. This gene encodes the catalase-peroxidase enzyme that activates isoniazid. Isoniazid is a prodrug. That is, it needs to be converted into its active form by _katG_ before it can work. However, the p.Ser315Thr mutation disables this activation so that isoniazid never gets activated. Resistance was also caused in some isolates by inhA promoter mutations, which confer lower-level resistance by overexpressing the isoniazid target enzyme.

**Fluoroquinolones - moxifloxacin and levofloxacin (73% each):** Nearly three-quarters of the 15 isolates were resistant to fluoroquinolone. This is mainly caused by mutations in Quinolone Resistance-Determining Regions (QRDR) of _gyrA_ (p.Asp94Gly, p.Ala90Val) and _gyrB_ (p.Glu501Asp). This 73% resistance greatly limits treatment options because fluoroquinolones are a cornerstone of MDR-TB treatment regimens.

**Bedaquiline and clofazimine (67% each):** 10 of the 15 isolates were bedaquiline and clofazimine resistant, mainly caused by mutations in the _mmpR5_ (also known as _Rv0678_). This gene encodes a repressor protein that normally keeps the MmpL5 efflux pump switched off. If not switched off, the efflux pump will push both drugs out of the bacterial cell before they can work. Frameshift mutations in _mmpR5_ disable this repressor, causing the efflux pump to run continuously. Now, bedaquiline is a relatively-new drug approved for MDR-TB treatment, so this much high resistance to a new drug is a major finding.

**Streptomycin (73%):** Streptomycin is an older aminoglycoside. Resistance to it was widespread and caused by mutations in _rrs_ and _gid_.

**Delamanid and linezolid (0%):** None of the 15 isolates showed resistance to delamanid or linezolid. Delamanid in particular is a newer nitroimidazole drug. This finding is clinically significant because it means delamanid is a viable treatment option for XDR-TB in this cohort.

### 3.3 Per-Sample Resistance Profiles

The binary resistance in the 15 isolates to the 12 drugs are summarized in Figure 3 below.

![Figure 3: Per-Sample Drug Resistance Profile across 15 MTB isolates](results/figures/fig3_resistance_heatmap.png)

Here are the key patterns:

- **XDR-TB Clustering:** The eight XDR-TB isolates at the top of the heatmap show broad resistance across most of the drug classes. There's notably dense resistance in the fluoroquinolone and bedaquiline columns, confirming the advanced resistance status of these strains.

- **Rifampicin Mono-Resistance (RR-TB):** Two RR-TB isolates (SRR33343103 and SRR33394873) show resistance to rifampicin only and almost nothing else. This could mean there's an emerging early-stage resistance. It could also mean the resistance to rifampicin was recently acquired but there are no subsequent mutations to transition to MDR and XDR status yet.

- **Quality Control Insight:** During QC, specifically in the reverse reads, SRR33394873 showed elevated adapter contamination (85.94% read pair survival versus >93% for other samples). Heavy trimming caused a significant portion of reverse reads to fall below the 36bp length threshold during the ILLUMINACLIP step in Trimmomatic. Despite this attrition, mapping rates remained high (>99%), meaning variant calling was still reliable.

---

## 4. Clinical and Epidemiological Implications

The findings observed in this project's cohort has public health and clinical implications for South Africa:

1. **Treatment crisis:** 53% of the 15 isolates were found to be XDR-TB, while 87% were resistant to isoniazid. This means the standard MDR-TB regimen would be ineffective for the majority of these patients. The next line of action would be to use newer drugs like bedaquiline, linezolid, and delamanid. However, these drugs are more expensive, require careful monitoring, and have significant side effects (such as cardiotoxicity).

2. **Delamanid and linezolid as viable options:** There was zero resistance to delamanid, linezolid, and pretomanid across all 15 isolates. This means these are effective drugs for the patients in this cohort and should be prioritized in XDR-TB treatment regimens in South Africa. It's also worth noting that there was zero resistance to para-aminosalicylic acid, though it's an older and much more toxic drug that is usually a last resort.

3. **Bedaquiline resistance concern:** Bedaquiline is a relatively-new drug that was introduced as a cornerstone of XDR-TB treatment. Hence, the 67% bedaquiline resistance that was noticed in this cohort is concerning. It could mean that resistance is evolving rapidly despite the drug's newness.

4. **Beijing lineage and resistance amplification:** Lineage 2 (Beijing) is strongly associated with drug-resistance acquisition. This means Lineage 2 acquires drug resistance faster than other lineages. Unfortunately, 47% (n=7) of the 15 isolates fall under Lineage 2. This likely explains the severe resistance burden observed in this cohort. Additionally, Lineage 4 is associated with high transmissibility. The other 47% (n=7) of the 15 isolates falls under Lineage 4. This co-existence of Lineage 2 and Lineage 4 XDR-TB strains in South Africa reflects a serious transmission risk.

5. **Genomic Drug Susceptibility Testing (DST) as a tool:** This analysis demonstrates the efficacy of WGS-based drug-resistance profiling. Using just the raw sequencing data of 15 isolates, TB-Profiler was able to predict resistance profiles, provide drug-level resolution, and provide lineage classification. This method of analysis will be significantly beneficial in clinical settings where conventional culture-based DST is relatively slower.

---

## 5. Limitations

- **Sample size:** The small sample size of 15 isolates limits the statistical power of frequency estimates. Therefore, the resistance frequencies observed in this cohort should be thought of as indicative, instead of representative of the entire South African MTB population.
- **Selection bias:** All the 15 isolates are from a single BioProject submitted by Columbia University (PRJNA1256480). Hence, there may be selection bias towards high-resistance isolates.
- **Temporal constraints:** The collection dates for the samples are not available ("Not collected"), as at the 8th of May, 2026. This prevents time-series analysis of the resistance that's observed.
- **Database dependency:** TB-Profiler uses known resistance-associated variants in the tbdb database to predict drug resistance. Hence, new or rare variants that are yet added to the tbdb database may cause false-susceptible predictions.

---

## 6. Conclusion

The 15 South African _MTB_ whole-genome sequences that were analyzed in this cohort reveal a high prevalence of extensively drug-resistant tuberculosis. There was universal rifampicin resistance, near-universal isoniazid resistance, and high rates of fluoroquinolone and bedaquiline resistance. The near-equal prevalence of Lineage 2 (_Beijing_) and Lineage 4 (_Euro-American_) strains reveal high transmissibility and high resistance acquisition. It also implies a compounding drug resistance crisis in South Africa. Delamanid, linezolid, and pretomanid are the new-generation drugs that recorded zero resistance across all 15 samples, and this signals their potential value in treatment regimens for the South African population. In conclusion, this cohort's findings demonstrate the importance of genomic surveillance in TB control efforts.

---

## References

1. World Health Organization. _Tuberculosis Fact Sheet_. https://www.who.int/news-room/fact-sheets/detail/tuberculosis

2. World Health Organization. _Global Tuberculosis Report 2025_. https://www.who.int/teams/global-tuberculosis-programme/tb-reports/global-tuberculosis-report-2025

3. World Health Organization. (2016). _WHO treatment guidelines for drug-resistant tuberculosis, 2016 update._ https://doi.org/10.1183/13993003.02308-2016

4. Pfyffer, G. E. (2015). _Mycobacterium_: General characteristics, laboratory detection, and staining procedures. _Manual of Clinical Microbiology_, 536-569.

5. Phelan, J. E., et al. (2019). Integrating informatics tools and portable sequencing technology for rapid detection of resistance to anti-tuberculous drugs. _Genome Medicine_, 11(41). https://doi.org/10.1186/s13073-019-0650-x

6. Columbia University. (2025). B-Prepared: Whole-genome sequencing of South African TB isolates. NCBI BioProject PRJNA1256480. https://www.ncbi.nlm.nih.gov/bioproject/PRJNA1256480

7. Gagneux, S., et al. (2006). Variable host–pathogen specificity in _Mycobacterium tuberculosis_, and its implications for TB epidemiology and vaccine efficacy. _PNAS_, 103(8), 2869-2873.

8. Chihota, V. N., et al. (2012). Population structure of _M. tuberculosis_ in South Africa: a review. _International Journal of Tuberculosis and Lung Disease_.

9. World Health Organization. (2021). WHO consolidated guidelines on tuberculosis. Module 3: Diagnosis - Rapid diagnostics for tuberculosis detection. Geneva: World Health Organization.

10. Conradie, F., et al. (2020). Treatment of Highly Drug-Resistant Pulmonary Tuberculosis. New England Journal of Medicine, 382(10), 893-902.

11. World Health Organization (2021). Catalogue of mutations in Mycobacterium tuberculosis complex and their association with drug resistance. Geneva: World Health Organization.
