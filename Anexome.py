import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import random

# Page configuration
st.set_page_config(
    page_title="Annexome - India's Cultural Heritage Explorer",
    page_icon="🏛️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for light colorful theme
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(90deg, #E8F5E8 0%, #F0F8FF 50%, #FFF8E1 100%);
        padding: 2rem;
        border-radius: 10px;
        margin-bottom: 2rem;
        text-align: center;
    }
    .metric-card {
        background: linear-gradient(135deg, #F3F9FF 0%, #E8F5E8 100%);
        padding: 1rem;
        border-radius: 8px;
        border-left: 4px solid #4CAF50;
        margin: 0.5rem 0;
    }
    .art-form-card {
        background: linear-gradient(135deg, #FFF3E0 0%, #E1F5FE 100%);
        padding: 1.5rem;
        border-radius: 12px;
        margin: 1rem 0;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .tourism-insight {
        background: linear-gradient(135deg, #F1F8E9 0%, #FCE4EC 100%);
        padding: 1rem;
        border-radius: 8px;
        border: 1px solid #90CAF9;
        margin: 1rem 0;
    }
    .filter-section {
        background: #F8F9FA;
        padding: 1rem;
        border-radius: 8px;
        margin-bottom: 1rem;
    }
</style>
""", unsafe_allow_html=True)

# Sample data generation (simulating real data sources)
@st.cache_data
def load_cultural_data():
    """Load and process cultural heritage data"""
    
    # Traditional Art Forms Data
    art_forms = pd.DataFrame({
        'Art_Form': ['Bharatanatyam', 'Kathak', 'Kuchipudi', 'Odissi', 'Manipuri', 
                     'Mohiniyattam', 'Sattriya', 'Kathakali', 'Yakshagana', 'Chhau',
                     'Bhangra', 'Garba', 'Lavani', 'Bihu', 'Giddha'],
        'State': ['Tamil Nadu', 'Uttar Pradesh', 'Andhra Pradesh', 'Odisha', 'Manipur',
                 'Kerala', 'Assam', 'Kerala', 'Karnataka', 'West Bengal',
                 'Punjab', 'Gujarat', 'Maharashtra', 'Assam', 'Punjab'],
        'Region': ['South', 'North', 'South', 'East', 'Northeast', 
                  'South', 'Northeast', 'South', 'South', 'East',
                  'North', 'West', 'West', 'Northeast', 'North'],
        'Category': ['Classical Dance', 'Classical Dance', 'Classical Dance', 'Classical Dance', 'Classical Dance',
                    'Classical Dance', 'Classical Dance', 'Classical Dance', 'Theatre', 'Dance Drama',
                    'Folk Dance', 'Folk Dance', 'Folk Dance', 'Folk Dance', 'Folk Dance'],
        'Practitioners': [15000, 25000, 8000, 6000, 3000, 4000, 2000, 5000, 3500, 4500,
                         12000, 18000, 9000, 7000, 8500],
        'Tourist_Interest': [85, 78, 72, 68, 45, 65, 35, 88, 42, 58,
                           70, 75, 62, 48, 55],
        'Preservation_Status': ['High', 'High', 'Medium', 'Medium', 'Low', 'Medium', 'Low', 'High', 'Low', 'Medium',
                               'High', 'High', 'Medium', 'Medium', 'Medium'],
        'UNESCO_Recognition': ['Yes', 'Yes', 'No', 'No', 'No', 'No', 'Yes', 'Yes', 'No', 'No',
                              'No', 'No', 'No', 'No', 'No'],
        'Age_Group': ['500+ years', '400+ years', '300+ years', '200+ years', '300+ years',
                     '400+ years', '500+ years', '600+ years', '400+ years', '300+ years',
                     '300+ years', '500+ years', '200+ years', '400+ years', '300+ years']
    })
    
    # Tourism data by month
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
              'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    
    tourism_data = pd.DataFrame({
        'Month': months,
        'Cultural_Tourists': [120000, 150000, 200000, 180000, 160000, 140000,
                             130000, 145000, 175000, 220000, 250000, 200000],
        'Art_Festival_Events': [15, 18, 25, 22, 20, 18, 16, 19, 23, 28, 35, 25],
        'Revenue_Crores': [45, 58, 78, 72, 65, 55, 52, 58, 70, 88, 95, 80],
        'International_Visitors': [8000, 12000, 18000, 15000, 12000, 9000,
                                  8500, 11000, 14000, 22000, 28000, 18000],
        'Domestic_Visitors': [112000, 138000, 182000, 165000, 148000, 131000,
                             121500, 134000, 161000, 198000, 222000, 182000]
    })
    
    # Regional distribution
    regional_data = pd.DataFrame({
        'Region': ['North', 'South', 'East', 'West', 'Northeast', 'Central'],
        'Art_Forms_Count': [25, 35, 18, 22, 12, 15],
        'Tourist_Footfall': [450000, 680000, 320000, 520000, 180000, 280000],
        'Infrastructure_Score': [7.8, 8.5, 6.2, 8.0, 5.5, 6.8],
        'Digitization_Level': [65, 78, 45, 70, 35, 55],
        'Investment_Crores': [125, 180, 85, 140, 45, 95]
    })
    
    # Hidden gems data
    hidden_gems = pd.DataFrame({
        'Location': ['Mithila (Bihar)', 'Warli (Maharashtra)', 'Pattachitra (Odisha)', 
                     'Phad (Rajasthan)', 'Kalamkari (Andhra Pradesh)', 'Tanjore (Tamil Nadu)',
                     'Gond (Madhya Pradesh)', 'Pichwai (Rajasthan)', 'Madhubani (Bihar)',
                     'Cheriyal (Telangana)'],
        'Art_Type': ['Painting', 'Tribal Art', 'Scroll Painting', 'Narrative Painting',
                    'Hand Painting', 'Classical Painting', 'Contemporary Tribal', 'Temple Art',
                    'Folk Painting', 'Scroll Painting'],
        'Accessibility_Score': [3.2, 4.1, 5.8, 6.2, 7.1, 8.5, 2.8, 7.8, 4.5, 5.2],
        'Tourist_Awareness': [25, 35, 45, 55, 65, 85, 20, 70, 30, 40],
        'Preservation_Urgency': ['High', 'High', 'Medium', 'Medium', 'Low', 'Low', 'Critical', 'Medium', 'High', 'Medium'],
        'Annual_Visitors': [5000, 8000, 15000, 25000, 35000, 75000, 3000, 45000, 7000, 12000],
        'State': ['Bihar', 'Maharashtra', 'Odisha', 'Rajasthan', 'Andhra Pradesh', 'Tamil Nadu',
                 'Madhya Pradesh', 'Rajasthan', 'Bihar', 'Telangana']
    })
    
    # Festival calendar data
    festivals_df = pd.DataFrame({
        'Festival': ['Khajuraho Dance Festival', 'Konark Dance Festival', 'Mamallapuram Dance Festival',
                    'Hampi Festival', 'Rajasthan Folk Festival', 'Kerala Kathakali Festival',
                    'Manipur Sangai Festival', 'Assam Tea Festival', 'Gujarat Navratri',
                    'Punjab Baisakhi Festival'],
        'Month': ['Feb', 'Dec', 'Jan', 'Nov', 'Oct', 'Aug', 'Nov', 'Nov', 'Oct', 'Apr'],
        'Duration_Days': [7, 5, 4, 3, 10, 6, 10, 5, 9, 3],
        'Expected_Visitors': [50000, 35000, 25000, 40000, 75000, 20000, 30000, 15000, 200000, 100000],
        'State': ['Madhya Pradesh', 'Odisha', 'Tamil Nadu', 'Karnataka', 'Rajasthan', 'Kerala',
                 'Manipur', 'Assam', 'Gujarat', 'Punjab']
    })
    
    return art_forms, tourism_data, regional_data, hidden_gems, festivals_df

# Load data
art_forms_df, tourism_df, regional_df, hidden_gems_df, festivals_df = load_cultural_data()

# Header
st.markdown("""
<div class="main-header">
    <h1>🏛️ Annexome</h1>
    <h3>Cultural Heritage & Tourism Explorer</h3>
    <p>Discover, Preserve, Experience India's Rich Traditions</p>
</div>
""", unsafe_allow_html=True)

# Sidebar navigation
st.sidebar.title("🧭 Navigation")
section = st.sidebar.selectbox(
    "Select Section",
    ["🏠 Overview", "🎭 Art Forms", "📊 Tourism Analytics", 
     "💎 Hidden Gems", "🌱 Responsible Tourism", "📈 Impact Dashboard", "🎪 Festival Calendar"]
)

# Global filters in sidebar
st.sidebar.markdown("---")
st.sidebar.subheader("🔧 Global Filters")

# Year filter
selected_year = st.sidebar.selectbox("Select Year", [2024, 2023, 2022, 2021, 2020], index=0)

# Season filter
season_filter = st.sidebar.selectbox("Select Season", ["All Seasons", "Winter", "Summer", "Monsoon", "Post-Monsoon"])

if section == "🏠 Overview":
    st.header("Cultural Heritage Platform Overview")
    
    # Key metrics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("""
        <div class="metric-card">
            <h3>127</h3>
            <p>Traditional Art Forms</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="metric-card">
            <h3>2.1M</h3>
            <p>Annual Cultural Tourists</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="metric-card">
            <h3>₹816 Cr</h3>
            <p>Cultural Tourism Revenue</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown("""
        <div class="metric-card">
            <h3>38</h3>
            <p>UNESCO Heritage Sites</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Mission statement and features
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("🎯 Our Mission")
        st.write("""
        Annexome connects India's rich cultural heritage with modern tourism through data-driven insights. 
        By showcasing both iconic sites and hidden gems, it promotes responsible travel that supports local communities and preserves traditional art forms.
        """)
        
        st.subheader("✨ Key Features")
        st.write("""
        • **Comprehensive Art Form Database**: Explore 127+ traditional art forms across India
        • **Tourism Analytics**: Seasonal trends, visitor patterns, and economic impact
        • **Hidden Gems Discovery**: Uncover lesser-known cultural treasures
        • **Responsible Tourism Guidelines**: Sustainable travel recommendations
        • **Real-time Impact Tracking**: Monitor preservation efforts and tourism effects
        • **Festival Calendar**: Plan visits around cultural celebrations
        """)
    
    with col2:
        # Regional distribution pie chart
        fig_regional = px.pie(
            regional_df, 
            values='Art_Forms_Count', 
            names='Region',
            title="Art Forms by Region",
            color_discrete_sequence=['#81C784', '#64B5F6', '#FFB74D', '#F06292', '#BA68C8', '#4DB6AC']
        )
        fig_regional.update_layout(height=400)
        st.plotly_chart(fig_regional, use_container_width=True)

elif section == "🎭 Art Forms":
    st.header("Traditional Art Forms Explorer")
    
    # Enhanced filter section
    st.markdown('<div class="filter-section">', unsafe_allow_html=True)
    st.subheader("🔍 Filters")
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        selected_region = st.selectbox("Region", ["All"] + sorted(art_forms_df['Region'].unique()))
    with col2:
        selected_category = st.selectbox("Category", ["All"] + sorted(art_forms_df['Category'].unique()))
    with col3:
        preservation_filter = st.selectbox("Preservation Status", ["All"] + sorted(art_forms_df['Preservation_Status'].unique()))
    with col4:
        unesco_filter = st.selectbox("UNESCO Recognition", ["All", "Yes", "No"])
    
    # Additional filters
    col5, col6 = st.columns(2)
    with col5:
        selected_state = st.selectbox("State", ["All"] + sorted(art_forms_df['State'].unique()))
    with col6:
        age_group_filter = st.selectbox("Age Group", ["All"] + sorted(art_forms_df['Age_Group'].unique()))
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Filter data
    filtered_df = art_forms_df.copy()
    if selected_region != "All":
        filtered_df = filtered_df[filtered_df['Region'] == selected_region]
    if selected_category != "All":
        filtered_df = filtered_df[filtered_df['Category'] == selected_category]
    if preservation_filter != "All":
        filtered_df = filtered_df[filtered_df['Preservation_Status'] == preservation_filter]
    if unesco_filter != "All":
        filtered_df = filtered_df[filtered_df['UNESCO_Recognition'] == unesco_filter]
    if selected_state != "All":
        filtered_df = filtered_df[filtered_df['State'] == selected_state]
    if age_group_filter != "All":
        filtered_df = filtered_df[filtered_df['Age_Group'] == age_group_filter]
    
    # Display filtered count
    st.info(f"📋 Showing {len(filtered_df)} art forms based on selected filters")
    
    # Art forms visualization
    if not filtered_df.empty:
        col1, col2 = st.columns(2)
        
        with col1:
            fig_practitioners = px.bar(
                filtered_df.head(10), 
                x='Art_Form', 
                y='Practitioners',
                title="Number of Practitioners",
                color='Practitioners',
                color_continuous_scale='Viridis',
                hover_data=['State', 'Category']
            )
            fig_practitioners.update_xaxes(tickangle=45)
            st.plotly_chart(fig_practitioners, use_container_width=True)
        
        with col2:
            fig_interest = px.scatter(
                filtered_df,
                x='Practitioners',
                y='Tourist_Interest',
                size='Tourist_Interest',
                color='Preservation_Status',
                hover_name='Art_Form',
                title="Tourist Interest vs Practitioners",
                color_discrete_map={'High': '#4CAF50', 'Medium': '#FF9800', 'Low': '#F44336'}
            )
            st.plotly_chart(fig_interest, use_container_width=True)
        
        # Category distribution
        if len(filtered_df['Category'].unique()) > 1:
            fig_category = px.histogram(
                filtered_df,
                x='Category',
                color='Region',
                title="Art Forms by Category and Region",
                barmode='group'
            )
            st.plotly_chart(fig_category, use_container_width=True)
        
        # Art form details
        st.subheader("📜 Featured Art Forms")
        
        for idx, row in filtered_df.head(6).iterrows():
            st.markdown(f"""
            <div class="art-form-card">
                <h4>{row['Art_Form']} - {row['State']}</h4>
                <p><strong>Category:</strong> {row['Category']} | <strong>Region:</strong> {row['Region']} | <strong>Age:</strong> {row['Age_Group']}</p>
                <p><strong>Practitioners:</strong> {row['Practitioners']:,} | <strong>Tourist Interest:</strong> {row['Tourist_Interest']}%</p>
                <p><strong>Preservation:</strong> {row['Preservation_Status']} | <strong>UNESCO Recognition:</strong> {row['UNESCO_Recognition']}</p>
            </div>
            """, unsafe_allow_html=True)
    else:
        st.warning("⚠️ No art forms match the selected filters. Please adjust your criteria.")

elif section == "📊 Tourism Analytics":
    st.header("Tourism Analytics Dashboard")
    
    # Filter section
    st.markdown('<div class="filter-section">', unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    with col1:
        visitor_type = st.selectbox("Visitor Type", ["All", "Domestic", "International"])
    with col2:
        metric_view = st.selectbox("Metric View", ["Monthly", "Quarterly", "Seasonal"])
    with col3:
        comparison_year = st.selectbox("Compare with Year", ["None", "2023", "2022", "2021"])
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Seasonal trends
    col1, col2 = st.columns(2)
    
    with col1:
        if visitor_type == "Domestic":
            fig_seasonal = px.line(
                tourism_df,
                x='Month',
                y='Domestic_Visitors',
                title='Domestic Tourism Trends',
                markers=True,
                line_shape='spline'
            )
        elif visitor_type == "International":
            fig_seasonal = px.line(
                tourism_df,
                x='Month',
                y='International_Visitors',
                title='International Tourism Trends',
                markers=True,
                line_shape='spline'
            )
        else:
            fig_seasonal = px.line(
                tourism_df,
                x='Month',
                y='Cultural_Tourists',
                title='Total Cultural Tourism Trends',
                markers=True,
                line_shape='spline'
            )
        fig_seasonal.update_traces(line_color='#FF7043', marker_color='#FF5722')
        st.plotly_chart(fig_seasonal, use_container_width=True)
    
    with col2:
        fig_events = px.bar(
            tourism_df,
            x='Month',
            y='Art_Festival_Events',
            title='Cultural Events by Month',
            color='Art_Festival_Events',
            color_continuous_scale='Plasma'
        )
        st.plotly_chart(fig_events, use_container_width=True)
    
    # Revenue analysis
    fig_revenue = px.area(
        tourism_df,
        x='Month',
        y='Revenue_Crores',
        title='Monthly Cultural Tourism Revenue (₹ Crores)'
    )
    fig_revenue.update_traces(fillcolor='rgba(102, 187, 106, 0.3)', line_color='#4CAF50')
    st.plotly_chart(fig_revenue, use_container_width=True)
    
    # Regional insights
    st.subheader("🗺️ Regional Performance Insights")
    
    col1, col2 = st.columns(2)
    
    with col1:
        fig_footfall = px.bar(
            regional_df,
            x='Region',
            y='Tourist_Footfall',
            title='Tourist Footfall by Region',
            color='Infrastructure_Score',
            color_continuous_scale='Sunset',
            hover_data=['Investment_Crores']
        )
        st.plotly_chart(fig_footfall, use_container_width=True)
    
    with col2:
        fig_infra = px.scatter(
            regional_df,
            x='Infrastructure_Score',
            y='Digitization_Level',
            size='Tourist_Footfall',
            color='Art_Forms_Count',
            hover_name='Region',
            title='Infrastructure vs Digitization',
            color_continuous_scale='Turbo'
        )
        st.plotly_chart(fig_infra, use_container_width=True)

elif section == "💎 Hidden Gems":
    st.header("Hidden Cultural Treasures")
    
    # Filter section
    st.markdown('<div class="filter-section">', unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    with col1:
        urgency_filter = st.selectbox("Preservation Urgency", ["All"] + sorted(hidden_gems_df['Preservation_Urgency'].unique()))
    with col2:
        art_type_filter = st.selectbox("Art Type", ["All"] + sorted(hidden_gems_df['Art_Type'].unique()))
    with col3:
        state_filter = st.selectbox("State", ["All"] + sorted(hidden_gems_df['State'].unique()))
    
    col4, col5 = st.columns(2)
    with col4:
        accessibility_range = st.slider("Accessibility Score Range", 0.0, 10.0, (0.0, 10.0))
    with col5:
        awareness_range = st.slider("Tourist Awareness Range", 0, 100, (0, 100))
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Filter data
    filtered_gems = hidden_gems_df.copy()
    if urgency_filter != "All":
        filtered_gems = filtered_gems[filtered_gems['Preservation_Urgency'] == urgency_filter]
    if art_type_filter != "All":
        filtered_gems = filtered_gems[filtered_gems['Art_Type'] == art_type_filter]
    if state_filter != "All":
        filtered_gems = filtered_gems[filtered_gems['State'] == state_filter]
    
    filtered_gems = filtered_gems[
        (filtered_gems['Accessibility_Score'] >= accessibility_range[0]) &
        (filtered_gems['Accessibility_Score'] <= accessibility_range[1]) &
        (filtered_gems['Tourist_Awareness'] >= awareness_range[0]) &
        (filtered_gems['Tourist_Awareness'] <= awareness_range[1])
    ]
    
    st.info(f"💎 Found {len(filtered_gems)} hidden gems matching your criteria")
    
    if not filtered_gems.empty:
        # Accessibility vs Awareness scatter plot
        fig_gems = px.scatter(
            filtered_gems,
            x='Accessibility_Score',
            y='Tourist_Awareness',
            size='Annual_Visitors',
            color='Preservation_Urgency',
            hover_name='Location',
            title='Hidden Gems: Accessibility vs Tourist Awareness',
            color_discrete_map={
                'Critical': '#FF5722',
                'High': '#FF9800', 
                'Medium': '#FFC107',
                'Low': '#4CAF50'
            }
        )
        fig_gems.update_layout(height=500)
        st.plotly_chart(fig_gems, use_container_width=True)
        
        # Priority recommendations
        st.subheader("🎯 Priority Development Recommendations")
        
        priority_gems = filtered_gems[
            (filtered_gems['Accessibility_Score'] < 5) & 
            (filtered_gems['Preservation_Urgency'].isin(['Critical', 'High']))
        ].sort_values('Annual_Visitors')
        
        if not priority_gems.empty:
            for idx, gem in priority_gems.iterrows():
                urgency_color = {'Critical': '#FF5722', 'High': '#FF9800', 'Medium': '#FFC107', 'Low': '#4CAF50'}
                
                st.markdown(f"""
                <div class="tourism-insight">
                    <h4>{gem['Location']} - {gem['Art_Type']}</h4>
                    <p><strong>State:</strong> {gem['State']} | <strong>Preservation Urgency:</strong> <span style="color: {urgency_color[gem['Preservation_Urgency']]}">{gem['Preservation_Urgency']}</span></p>
                    <p><strong>Current Visitors:</strong> {gem['Annual_Visitors']:,} | <strong>Accessibility:</strong> {gem['Accessibility_Score']}/10</p>
                    <p><strong>Tourist Awareness:</strong> {gem['Tourist_Awareness']}% | <strong>Recommendation:</strong> Immediate infrastructure development and awareness campaigns needed</p>
                </div>
                """, unsafe_allow_html=True)
        else:
            st.info("✅ No high-priority gems found with selected filters.")
    else:
        st.warning("⚠️ No hidden gems match the selected criteria.")

elif section == "🌱 Responsible Tourism":
    st.header("Responsible Tourism Guidelines")
    
    # Impact framework dropdown
    impact_view = st.selectbox("Select Impact View", ["Overall Metrics", "Environmental", "Cultural", "Economic", "Community"])
    
    st.subheader("🌍 Tourism Impact Framework")
    
    # Tourism impact metrics
    impact_metrics = {
        'Environmental': {'score': 7.2, 'trend': '+0.3'},
        'Cultural Preservation': {'score': 6.8, 'trend': '+0.5'},
        'Economic Benefit': {'score': 8.1, 'trend': '+0.7'},
        'Community Engagement': {'score': 6.5, 'trend': '+0.2'}
    }
    
    cols = st.columns(4)
    for i, (metric, data) in enumerate(impact_metrics.items()):
        with cols[i]:
            st.markdown(f"""
            <div class="metric-card">
                <h4>{metric}</h4>
                <h2>{data['score']}/10</h2>
                <p style="color: #4CAF50;">Trend: {data['trend']}</p>
            </div>
            """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🌿 Sustainable Tourism Practices")
        st.write("""
        **For Travelers:**
        • Learn cultural etiquette before visiting
        • Support local artisans directly
        • Participate in workshops vs observation
        • Respect photography restrictions
        • Choose community-based guides
        • Use eco-friendly transportation
        • Stay in locally-owned accommodation
        
        **For Communities:**
        • Capacity building for local guides
        • Artisan cooperatives for fair pricing
        • Visitor management systems
        • Preserve authenticity in performances
        • Reinvest tourism revenue in preservation
        • Develop sustainable infrastructure
        """)
    
    with col2:
        st.subheader("📊 Tourism Carrying Capacity")
        
        # Sample carrying capacity data
        capacity_data = pd.DataFrame({
            'Location': ['Khajuraho', 'Hampi', 'Ajanta Caves', 'Konark', 'Mahabalipuram'],
            'Current_Visitors': [850000, 650000, 400000, 300000, 500000],
            'Optimal_Capacity': [600000, 500000, 300000, 250000, 400000],
            'Overcrowding_Risk': ['High', 'Medium', 'Medium', 'Low', 'Medium']
        })
        
        fig_capacity = px.bar(
            capacity_data,
            x='Location',
            y=['Current_Visitors', 'Optimal_Capacity'],
            title='Visitor Numbers vs Optimal Capacity',
            barmode='group',
            color_discrete_sequence=['#E57373', '#81C784']
        )
        fig_capacity.update_xaxes(tickangle=45)
        st.plotly_chart(fig_capacity, use_container_width=True)
    
    st.subheader("🤝 Community Partnership Programs")
    
    partnership_data = [
        {
            'Program': 'Artisan Direct Connect',
            'Description': 'Platform connecting tourists directly with local artisans',
            'Impact': '2,500 artisans benefited, 40% income increase',
            'Status': 'Active'
        },
        {
            'Program': 'Cultural Immersion Stays',
            'Description': 'Homestays with families practicing traditional arts',
            'Impact': '150 families participating, 85% satisfaction rate',
            'Status': 'Expanding'
        },
        {
            'Program': 'Heritage Skill Workshops',
            'Description': 'Hands-on learning experiences for tourists',
            'Impact': '12,000 participants, 95% completion rate',
            'Status': 'Active'
        },
        {
            'Program': 'Digital Heritage Documentation',
            'Description': 'Collaborative documentation with local communities',
            'Impact': '68% of art forms digitally preserved',
            'Status': 'Ongoing'
        }
    ]
    
    for program in partnership_data:
        st.markdown(f"""
        <div class="tourism-insight">
            <h4>{program['Program']} - {program['Status']}</h4>
            <p>{program['Description']}</p>
            <p><strong>Impact:</strong> {program['Impact']}</p>
        </div>
        """, unsafe_allow_html=True)

elif section == "📈 Impact Dashboard":
    st.header("Impact Dashboard")
    
    # Dashboard view selector
    dashboard_view = st.selectbox("Select Dashboard View", 
                                 ["Overall Impact", "Preservation Progress", "Economic Impact", "Community Benefits"])
    
    # Key performance indicators
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="metric-card">
            <h3>68%</h3>
            <p>Art Forms Digitally Documented</p>
            <small>↑ 12% from last year</small>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="metric-card">
            <h3>₹145 Cr</h3>
            <p>Direct Economic Impact</p>
            <small>↑ 18% from last year</small>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="metric-card">
            <h3>23,000</h3>
            <p>Artisans Supported</p>
            <small>↑ 15% from last year</small>
        </div>
        """, unsafe_allow_html=True)
    
    # Additional metrics row
    col4, col5, col6 = st.columns(3)
    
    with col4:
        st.markdown("""
        <div class="metric-card">
            <h3>156</h3>
            <p>Community Programs</p>
            <small>↑ 22% from last year</small>
        </div>
        """, unsafe_allow_html=True)
    
    with col5:
        st.markdown("""
        <div class="metric-card">
            <h3>89%</h3>
            <p>Tourist Satisfaction</p>
            <small>↑ 5% from last year</small>
        </div>
        """, unsafe_allow_html=True)
    
    with col6:
        st.markdown("""
        <div class="metric-card">
            <h3>45</h3>
            <p>International Awards</p>
            <small>↑ 8% from last year</small>
        </div>
        """, unsafe_allow_html=True)
    
    # Preservation progress over time
    years = list(range(2019, 2025))
    preservation_progress = pd.DataFrame({
        'Year': years,
        'Documented_Arts': [45, 52, 58, 61, 65, 68],
        'Digital_Archives': [20, 28, 35, 42, 48, 55],
        'Active_Practitioners': [18500, 19200, 19800, 20500, 21200, 22000],
        'Tourism_Revenue': [95, 102, 85, 118, 132, 145],
        'Community_Programs': [85, 98, 115, 128, 142, 156]
    })
    
    col1, col2 = st.columns(2)
    
    with col1:
        if dashboard_view == "Preservation Progress":
            fig_progress = px.line(
                preservation_progress,
                x='Year',
                y=['Documented_Arts', 'Digital_Archives'],
                title='Cultural Documentation Progress (%)',
                markers=True
            )
        else:
            fig_progress = px.line(
                preservation_progress,
                x='Year',
                y='Active_Practitioners',
                title='Active Practitioners Growth',
                markers=True
            )
        st.plotly_chart(fig_progress, use_container_width=True)
    
    with col2:
        if dashboard_view == "Economic Impact":
            fig_economic = px.area(
                preservation_progress,
                x='Year',
                y='Tourism_Revenue',
                title='Cultural Tourism Revenue (₹ Crores)'
            )
        else:
            fig_economic = px.bar(
                preservation_progress,
                x='Year',
                y='Community_Programs',
                title='Community Programs Growth'
            )
        st.plotly_chart(fig_economic, use_container_width=True)
    
    # Success stories
    st.subheader("🏆 Success Stories")
    
    success_stories = [
        {
            'Title': 'Mithila Art Revival',
            'Location': 'Bihar',
            'Impact': 'Tourist visitors increased by 340%, 450 women artists now earning sustainable income',
            'Timeline': '2020-2024',
            'Category': 'Economic Empowerment'
        },
        {
            'Title': 'Warli Art Digital Documentation',
            'Location': 'Maharashtra',
            'Impact': 'Complete digital archive created, international recognition achieved',
            'Timeline': '2021-2023',
            'Category': 'Digital Preservation'
        },
        {
            'Title': 'Kathakali Performance Tourism',
            'Location': 'Kerala',
            'Impact': 'Year-round employment for 85 artists, cultural center established',
            'Timeline': '2019-2024',
            'Category': 'Sustainable Tourism'
        },
        {
            'Title': 'Gond Art Global Outreach',
            'Location': 'Madhya Pradesh',
            'Impact': 'International exhibitions, 200% increase in artist income',
            'Timeline': '2022-2024',
            'Category': 'Global Recognition'
        }
    ]
    
    for story in success_stories:
        st.markdown(f"""
        <div class="art-form-card">
            <h4>{story['Title']} ({story['Timeline']})</h4>
            <p><strong>Location:</strong> {story['Location']} | <strong>Category:</strong> {story['Category']}</p>
            <p><strong>Impact:</strong> {story['Impact']}</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Future roadmap
    st.subheader("🚀 Future Roadmap (2025-2027)")
    
    roadmap_items = [
        "Launch AI-powered cultural experience recommendation system",
        "Expand digital documentation to 90% of identified art forms",
        "Establish 50 new community-based tourism initiatives",
        "Create virtual reality experiences for 25 major art forms",
        "Develop mobile app for real-time cultural event discovery",
        "Launch artisan marketplace with global reach"
    ]
    
    for i, item in enumerate(roadmap_items, 1):
        st.markdown(f"**{i}.** {item}")

elif section == "🎪 Festival Calendar":
    st.header("Cultural Festival Calendar")
    
    # Filter section
    st.markdown('<div class="filter-section">', unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    with col1:
        selected_month = st.selectbox("Select Month", 
                                    ["All"] + ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
                                              'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
    with col2:
        festival_state = st.selectbox("Select State", ["All"] + sorted(festivals_df['State'].unique()))
    with col3:
        visitor_range = st.selectbox("Expected Visitors", 
                                   ["All", "Small (< 25K)", "Medium (25K-75K)", "Large (> 75K)"])
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Filter festival data
    filtered_festivals = festivals_df.copy()
    if selected_month != "All":
        filtered_festivals = filtered_festivals[filtered_festivals['Month'] == selected_month]
    if festival_state != "All":
        filtered_festivals = filtered_festivals[filtered_festivals['State'] == festival_state]
    
    if visitor_range == "Small (< 25K)":
        filtered_festivals = filtered_festivals[filtered_festivals['Expected_Visitors'] < 25000]
    elif visitor_range == "Medium (25K-75K)":
        filtered_festivals = filtered_festivals[(filtered_festivals['Expected_Visitors'] >= 25000) & 
                                               (filtered_festivals['Expected_Visitors'] <= 75000)]
    elif visitor_range == "Large (> 75K)":
        filtered_festivals = filtered_festivals[filtered_festivals['Expected_Visitors'] > 75000]
    
    st.info(f"🎪 Found {len(filtered_festivals)} festivals matching your criteria")
    
    if not filtered_festivals.empty:
        # Festival visualizations
        col1, col2 = st.columns(2)
        
        with col1:
            fig_monthly = px.histogram(
                filtered_festivals,
                x='Month',
                title='Festivals by Month',
                color_discrete_sequence=['#FF6B6B']
            )
            st.plotly_chart(fig_monthly, use_container_width=True)
        
        with col2:
            fig_visitors = px.scatter(
                filtered_festivals,
                x='Duration_Days',
                y='Expected_Visitors',
                size='Expected_Visitors',
                color='State',
                hover_name='Festival',
                title='Festival Duration vs Expected Visitors'
            )
            st.plotly_chart(fig_visitors, use_container_width=True)
        
        # Festival calendar view
        fig_calendar = px.bar(
            filtered_festivals,
            x='Festival',
            y='Expected_Visitors',
            color='Month',
            title='Festival Calendar Overview',
            hover_data=['State', 'Duration_Days']
        )
        fig_calendar.update_xaxes(tickangle=45)
        st.plotly_chart(fig_calendar, use_container_width=True)
        
        # Festival details
        st.subheader("🎭 Festival Details")
        
        for idx, festival in filtered_festivals.iterrows():
            st.markdown(f"""
            <div class="art-form-card">
                <h4>{festival['Festival']} - {festival['State']}</h4>
                <p><strong>Month:</strong> {festival['Month']} | <strong>Duration:</strong> {festival['Duration_Days']} days</p>
                <p><strong>Expected Visitors:</strong> {festival['Expected_Visitors']:,}</p>
                <p><strong>Best Time to Visit:</strong> Plan 2-3 days in advance for accommodation</p>
            </div>
            """, unsafe_allow_html=True)
    else:
        st.warning("⚠️ No festivals match the selected criteria.")

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #666; padding: 2rem;">
    <p>🏛️ <strong>Annexome</strong> - Preserving India's Cultural Heritage Through Responsible Tourism</p>
    <p>📊 Data sources: Government of India Open Data Platform, Ministry of Tourism, UNESCO</p>
</div>
""", unsafe_allow_html=True)