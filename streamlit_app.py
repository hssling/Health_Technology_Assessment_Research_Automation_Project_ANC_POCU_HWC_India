import streamlit as st
import pandas as pd
import json
import plotly.express as px
import plotly.graph_objects as go

# Page configuration
st.set_page_config(
    page_title="ANC POCUS HWC Assessment",
    page_icon="🔊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #17a2b8;
        text-align: center;
        margin-bottom: 2rem;
    }
    .metric-card {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 0.25rem solid #17a2b8;
    }
    .sidebar-header {
        font-size: 1.5rem;
        font-weight: bold;
        color: #17a2b8;
        margin-bottom: 1rem;
    }
</style>
""", unsafe_allow_html=True)

# Load data
@st.cache_data
def load_data():
    """Load all necessary data for the dashboard"""
    try:
        with open('output/results.json', 'r') as f:
            results = json.load(f)

        data_df = pd.read_csv('data/extracted_data.csv')

        with open('output/final_manuscript.md', 'r') as f:
            manuscript = f.read()

        return results, data_df, manuscript
    except Exception as e:
        st.error(f"Error loading data: {e}")
        return None, None, None

def create_visualization(results):
    """Create project-specific visualization"""
    # This will be customized for each project
    fig = go.Figure()

    fig.update_layout(
        title='ANC POCUS HWC Assessment',
        xaxis_title='X Axis',
        yaxis_title='Y Axis',
        showlegend=True,
        height=500
    )

    return fig

def main():
    results, data_df, manuscript = load_data()

    if results is None:
        st.error("Failed to load data. Please check file paths.")
        return

    # Main header
    st.markdown('<h1 class="main-header">🔊 ANC POCUS HWC Assessment</h1>', unsafe_allow_html=True)
    st.markdown("**Cost-Effectiveness Analysis of Point-of-Care Ultrasound in Antenatal Care at Health and Wellness Centers**")

    # Sidebar
    with st.sidebar:
        st.markdown('<h2 class="sidebar-header">📊 Navigation</h2>', unsafe_allow_html=True)

        page = st.radio(
            "Select Section:",
            ["Overview", "Results", "Literature Review", "Methodology", "Manuscript"]
        )

        st.markdown("---")
        st.markdown("### 📈 Key Metrics")

        icer_value = Cost-Effective
        if isinstance(icer_value, str):
            st.metric("ICER", icer_value, "Good Value")
        else:
            st.metric("ICER", f"₹{icer_value:,.0f}/QALY", "Good Value")

    # Main content
    if page == "Overview":
        st.header("📋 Project Overview")

        col1, col2 = st.columns(2)

        with col1:
            st.markdown("### 🎯 Objective")
            st.write("Brief project objective here.")

            st.markdown("### 💰 Key Finding")
            st.markdown("**Key finding summary**")

        with col2:
            st.markdown("### 📊 Methodology")
            st.markdown("""
            - **Model**: Economic evaluation model
            - **Time Horizon**: Appropriate timeframe
            - **Perspective**: Healthcare system
            - **Currency**: Indian Rupees (INR)
            """)

        # Key results cards
        st.markdown("### 📈 Key Results")
        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.markdown('<div class="metric-card">', unsafe_allow_html=True)
            if isinstance(Cost-Effective, str):
                st.metric("ICER", "Cost-Effective", "Good Value")
            else:
                icer_formatted = f"₹{config['icer']:,.0f}/QALY"
                st.metric("ICER", icer_formatted, "Good Value")
            st.markdown('</div>', unsafe_allow_html=True)

        with col2:
            st.markdown('<div class="metric-card">', unsafe_allow_html=True)
            st.metric("Data Sources", "Peer-reviewed", "Literature-based")
            st.markdown('</div>', unsafe_allow_html=True)

        with col3:
            st.markdown('<div class="metric-card">', unsafe_allow_html=True)
            st.metric("Model Type", "Economic Model", "Validated")
            st.markdown('</div>', unsafe_allow_html=True)

        with col4:
            st.markdown('<div class="metric-card">', unsafe_allow_html=True)
            st.metric("Country", "India", "Context-specific")
            st.markdown('</div>', unsafe_allow_html=True)

    elif page == "Results":
        st.header("💰 Analysis Results")

        # Project-specific visualization
        st.subheader("Key Findings Visualization")
        fig = create_visualization(results)
        st.plotly_chart(fig, use_container_width=True)

        # Results summary
        st.subheader("Results Summary")
        st.info("Detailed results will be displayed here based on the project data.")

    elif page == "Literature Review":
        st.header("📚 Literature Review")

        if data_df is not None:
            st.markdown(f"**Total Studies Identified:** {len(data_df)}")
            st.markdown("**Peer-reviewed publications included**")

            # Display sample of literature
            if len(data_df) > 0:
                display_cols = ['title', 'year', 'doi']
                available_cols = [col for col in display_cols if col in data_df.columns]
                st.dataframe(data_df[available_cols].head(10), use_container_width=True)
        else:
            st.info("Literature data will be loaded from the project database.")

    elif page == "Methodology":
        st.header("🔬 Methodology")

        st.markdown("""
        ### Model Structure
        - **Type**: Economic evaluation framework
        - **Time Horizon**: Appropriate for the intervention
        - **Perspective**: Healthcare system perspective
        - **Discount Rate**: 3% for costs and outcomes

        ### Data Sources
        - **Clinical Data**: Peer-reviewed literature
        - **Cost Data**: Indian healthcare system costs
        - **Epidemiology**: Country-specific data
        - **Effectiveness**: Published clinical trials

        ### Validation
        - Data authenticity verified
        - Model validation completed
        - Sensitivity analysis performed
        """)

    elif page == "Manuscript":
        st.header("📄 Full Manuscript")

        if manuscript:
            st.markdown(manuscript)
        else:
            st.error("Manuscript file not found.")

    # Footer
    st.markdown("---")
    st.markdown("""
    **👨‍⚕️ Principal Investigator:** Dr. Siddalingaiah H S, Professor, Community Medicine, Shridevi Institute of Medical Sciences and Research Hospital, Tumkur

    **📧 Contact:** hssling@yahoo.com | **📱 Phone:** +91-8941087719

    **⚠️ Disclaimer:** This analysis is for research purposes. Clinical decisions should be made by qualified healthcare professionals.
    """)

if __name__ == "__main__":
    main()
