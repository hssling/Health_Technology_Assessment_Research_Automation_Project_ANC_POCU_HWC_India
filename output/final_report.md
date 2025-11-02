# HTA Automation Report – hta_project_06_anc_pocus_hwc

**Generated:** 2025-11-02 15:19:06

## 1. Protocol (parsed)
# HTA Protocol: Point-of-Care Ultrasound (PoCUS) and Basic Diagnostics for Early ANC Risk Detection at Health & Wellness Centres (HWCs) in India

## 1. Background
India continues to face preventable maternal and perinatal deaths arising from late detection of high-risk pregnancies (HRP) — including placenta previa, multiple pregnancy, malpresentation, fetal growth restriction, and oligohydramnios. Under Ayushman Bharat – Health & Wellness Centres (AB-HWC) and comprehensive PHC, there is a policy interest in decentralizing selected ANC diagnostics to the periphery. One such technology is portable/handheld point-of-care ultrasound (PoCUS) plus a basic diagnostic package (Hb, urine, BP, FHR) with tele-radiology backup. This HTA will compare PoCUS-at-HWC with the current referral-based USG model.

## 2. Objectives
**Primary objective:** To estimate the cost-effectiveness of introducing PoCUS + basic ANC diagnostics at HWCs compared to current practice (facility-level USG only).

**Secondary objectives:**
- Budget impact of providing PoCUS to all / selected HWCs.
- Effect of task-sharing (ANM/CHO-operated PoCUS) vs doctor-performed PoCUS.
- Contextual analysis for tribal / hard-to-reach districts.

## 3. PICO
- **Population:** Pregnant women taking ANC in public facilities (HWC/PHC/SC) in India.
- **Intervention:** PoCUS at HWC + basic ANC diagnostics + tele-report.
- **Comparator:** Current ANC with referral to higher facility for USG.
- **Outcomes:** HRP detected, maternal/perinatal adverse outcomes averted, DALYs averted.
- **Perspective:** Government health system.
- **Time horizon:** Pregnancy to 42 days postpartum (base case); 1 year (sensitivity).
- **Discounting:** 3%.

## 4. Methods
- Decision-tree comparing current vs PoCUS.
- Costs: device, O&M, training, scan, referral, management.
- Effectiveness: improvement in detection → reduction in adverse outcomes.
- Sensitivity: device price, scan volume, referral completion, diagnostic accuracy.

## 5. Outputs
1. Search strategy
2. Evidence/extraction sheet
3. Python decision model
4. BIA sheet
5. Draft manuscript


## 2. Search Strategy
PubMed search:
(("ultrasonography, prenatal"[Mesh] OR "prenatal ultrasound" OR "obstetric ultrasound" OR "antenatal ultrasound" OR "fetal ultrasound" OR "point-of-care ultrasound" OR PoCUS OR "handheld ultrasound")
AND (antenatal OR pregnancy OR maternal OR obstetric OR prenatal)
AND (India OR "low- and middle-income countries" OR LMIC OR "developing countries" OR "resource-limited settings")
AND (cost OR "cost-effectiveness" OR "cost analysis" OR "economic evaluation" OR "health technology assessment" OR HTA OR "budget impact" OR "cost-benefit"))
AND ("2000/01/01"[Date - Publication] : "3000"[Date - Publication])

Grey literature:
- MoHFW ANC / LaQshya guidelines
- UNFPA handheld ultrasound pilots in India
- WHO antenatal care guidelines
- Indian Medical Association ultrasound protocols
- State health department ANC programs


## 3. Model Output (stdout)
```
Base: 120.0 66.0 6.960000000000001 330000.0
Intervention: 120.0 102.0 5.52 192840.0
ICER per HRP detected: -3810.0
ICER per adverse outcome averted: -95249.99999999991

```

## 4. Draft Manuscript (template)
# Draft Manuscript – PoCUS at HWCs for Early ANC Risk Detection in India

## Title
Cost-Effectiveness of Point-of-Care Ultrasound at Health & Wellness Centres for Early Detection of High-Risk Pregnancies in India

## Abstract
...

## Sections
1. Introduction
2. Methods
3. Results
4. Discussion
5. Conclusion


## 5. Orchestrator Log
```
=== Processing project: hta_project_06_anc_pocus_hwc ===
Protocol: loaded.
Search strings: loaded.
Literature search: starting...
Literature search: completed, extracted 6 data points.
Data processing: starting...
Data processing: completed, filled 6 rows.
R: executed.
R stderr:
â”€â”€ Attaching core tidyverse packages â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€ tidyverse 2.0.0 â”€â”€
âœ” dplyr     1.1.4     âœ” readr     2.1.5
âœ” forcats   1.0.0     âœ” stringr   1.5.2
âœ” ggplot2   4.0.0     âœ” tibble    3.3.0
âœ” lubridate 1.9.4     âœ” tidyr     1.3.1
âœ” purrr     1.1.0     
â”€â”€ Conflicts â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€ tidyverse_conflicts() â”€â”€
âœ– dplyr::filter() masks stats::filter()
âœ– dplyr::lag()    masks stats::lag()
â„¹ Use the conflicted package (<http://conflicted.r-lib.org/>) to force all conflicts to become errors

Model: executed 04_anc_pocus_model.py
Model stdout:
Base: 120.0 66.0 6.960000000000001 330000.0
Intervention: 120.0 102.0 5.52 192840.0
ICER per HRP detected: -3810.0
ICER per adverse outcome averted: -95249.99999999991

Manuscript generation: starting...
Manuscript generation: completed.
```