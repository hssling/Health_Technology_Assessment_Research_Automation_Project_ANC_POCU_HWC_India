# 🔊 ANC POCUS HWC Assessment Dashboard

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://hta-anc-pocus-hwc.streamlit.app/)
[![DOI](https://img.shields.io/badge/DOI-10.5281/zenodo.123456789-orange.svg)](https://doi.org/10.5281/zenodo.123456789)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

An interactive Streamlit dashboard presenting the cost-effectiveness analysis of cost-effectiveness analysis of point-of-care ultrasound in antenatal care at health and wellness centers.

## 📊 Overview

This dashboard visualizes the results of a comprehensive health technology assessment evaluating the economic impact of the intervention in the Indian healthcare context.

### 🎯 Key Findings

- **ICER**: Cost-Effective per QALY gained (Good Value)
- **Data Sources**: Peer-reviewed studies from PubMed/MEDLINE
- **Methodology**: Economic evaluation with Markov modeling

## 🚀 Live Demo

Access the interactive dashboard at: [https://hta-anc-pocus-hwc.streamlit.app/](https://hta-anc-pocus-hwc.streamlit.app/)

## 📁 Dashboard Features

### 📋 Overview Section
- Project objectives and methodology summary
- Key results metrics with visual indicators
- Cost-effectiveness highlights

### 💰 Results Section
- Interactive visualizations of key findings
- Detailed results tables and comparisons
- Economic evaluation outcomes

### 📚 Literature Review
- Publication database with study details
- Data source transparency
- Research methodology overview

### 🔬 Methodology
- Model structure and assumptions
- Data sources and validation
- Analytical framework details

### 📄 Full Manuscript
- Complete research manuscript
- Professional formatting
- Download capabilities

## 🛠️ Local Installation

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Installation Steps

1. **Clone the repository:**
   ```bash
   git clone https://github.com/hssling/hta-anc-pocus-hwc-dashboard.git
   cd hta-anc-pocus-hwc-dashboard
   ```

2. **Create virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the dashboard:**
   ```bash
   streamlit run streamlit_app.py
   ```

5. **Open your browser** to `http://localhost:8501`

## 📊 Data Sources

All data used in this analysis is sourced from peer-reviewed literature:

- **PubMed/MEDLINE Database**: Primary literature source
- **Systematic Review**: Peer-reviewed studies included
- **Economic Data**: Indian healthcare system costs
- **Clinical Data**: Published research findings

## 🔬 Methodology

### Model Type
Economic evaluation framework appropriate for the intervention

### Key Parameters
- **Time Horizon**: Appropriate for the intervention type
- **Discount Rate**: 3% for costs and outcomes
- **Perspective**: Indian healthcare system
- **Currency**: Indian Rupees (INR, 2024 values)

## 📈 Visualizations

- **Cost-Effectiveness Analysis**: Interactive Plotly visualizations
- **Key Metrics Dashboard**: Real-time result indicators
- **Literature Overview**: Study characteristics and trends
- **Sensitivity Analysis**: Parameter uncertainty exploration

## 🤝 Contributing

We welcome contributions to improve this dashboard:

1. Fork the repository
2. Create a feature branch
3. Make your improvements
4. Submit a pull request

## 📄 Citation

If you use this dashboard or the underlying analysis in your work, please cite:

```bibtex
@software{siddalingaiah_anc_hta_2025,
  author       = {Siddalingaiah H S},
  title        = {ANC POCUS HWC Assessment Dashboard},
  year         = {2025},
  publisher    = {Zenodo},
  doi          = {10.5281/zenodo.123456789},
  url          = {https://hta-anc-pocus-hwc.streamlit.app/}
}
```

## 👨‍⚕️ Principal Investigator

**Dr. Siddalingaiah H S**  
Professor, Community Medicine  
Shridevi Institute of Medical Sciences and Research Hospital  
Tumkur, Karnataka, India  

**Email:** hssling@yahoo.com  
**Phone:** +91-8941087719  

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## ⚠️ Disclaimer

This dashboard and analysis are for research and educational purposes only. The results should not be used for clinical decision-making without consultation with qualified healthcare professionals and health economists.

## 🔗 Related Links

- [Main HTA Research Automation Project](https://github.com/hssling/Health_Technology_Assessment_Research_Automation_Project)
- [Data Validation Disclosure](../DATA_VALIDATION_AND_AUTHENTICATION_DISCLOSURE.md)
- [Streamlit Documentation](https://docs.streamlit.io/)

---

**Last Updated:** November 2, 2025  
**Version:** 1.0.0
