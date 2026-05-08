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

To reflect the evolutionary history and geographic spread of the different TB strains in this cohort, it is important to classify the MTB isolates within the global phylogeny of the M. tuberculosis complex.

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
| Extensively Drug-Resistant TB (XDR-TB)         | Resistant to Rifampicin, Isoniazid, any fluoroquinolone, and at least one of Bedaquiline or Linezolid | 8     |
| Pre-Extensively Drug-Resistant TB (Pre-XDR-TB) | Resistant to Rifampicin, Isoniazid, and any fluoroquinolone                                           | 3     |
| Multidrug-Resistant TB (MDR-TB)                | Resistant to at least Rifampicin and Isoniazid                                                        | 2     |
| Rifampicin-Resistant TB (RR-TB)                | Rifampicin-resistant only                                                                             | 2     |

The predominance of XDR-TB (53% of isolates) in this cohort reflects high drug resistance in the B-Prepared dataset. Nonetheless, this is consistent with the documented XDR-TB burden in South Africa, where the country accounts for a disproportionate share of global XDR-TB cases [2, 10].

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
