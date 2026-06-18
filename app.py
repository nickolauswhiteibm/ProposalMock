import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime
import os
from dotenv import load_dotenv
from streamlit_agraph import agraph, Node, Edge, Config

# Load environment variables
load_dotenv()

# Page configuration
st.set_page_config(
    page_title="AP Automation Proposal - Microsoft Copilot Agents",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #0078D4;
        text-align: center;
        margin-bottom: 2rem;
    }
    .section-header {
        font-size: 1.8rem;
        font-weight: bold;
        color: #106EBE;
        margin-top: 2rem;
        margin-bottom: 1rem;
        border-bottom: 3px solid #0078D4;
        padding-bottom: 0.5rem;
    }
    .metric-card {
        background-color: #f0f2f6;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 5px solid #0078D4;
        margin: 1rem 0;
    }
    .agent-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 1.5rem;
        border-radius: 10px;
        margin: 1rem 0;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    .cost-savings {
        font-size: 2rem;
        font-weight: bold;
        color: #28a745;
    }
    .stTabs [data-baseweb="tab-list"] {
        gap: 2rem;
    }
    .stTabs [data-baseweb="tab"] {
        font-size: 1.1rem;
        font-weight: 600;
    }
</style>
""", unsafe_allow_html=True)

# Title
st.markdown('<div class="main-header">🚀 AP Automation Transformation Proposal<br>Microsoft Copilot Agentic Solution</div>', unsafe_allow_html=True)

# Context Section
st.markdown("## Transforming Accounts Payable Through Agentic AI and Microsoft Copilot")

with st.expander("📋 **Client Context & Strategic Opportunity** - Click to expand", expanded=False):
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### Client Context")
        st.markdown("""
        A global tobacco manufacturing enterprise with annual revenue exceeding **$20B** operates a highly complex Accounts Payable (AP) environment across multiple business units and regions.
        
        The organization runs a mature SAP ecosystem with Signavio for process intelligence and uses Ariba for procurement. Current strategic priorities for 2026–2027 focus on expanding Ariba Supplier Network capabilities to automate purchase order (PO) collaboration with suppliers, while invoice automation remains out of scope.
        
        Today, the company processes approximately **800,000 invoices annually** through a legacy ODC-based invoice processing platform. Invoices are scanned, digitized, and ingested into the platform before being validated through complex three-way matching and ultimately paid through SAP.
        
        However, fragmented upstream purchasing and receiving processes across categories (materials, MRO, services) and regions create significant operational complexity and a poor vendor experience.
        """)
        
        st.markdown("### Current Challenges")
        st.markdown("""
        The AP operation is not performing at best-in-class levels due to:
        
        - Delayed vendor inquiry resolution and limited self-service capabilities
        - High manual effort required to investigate payment and invoice issues
        - High invoice volume with inconsistent invoice formats
        - Complex and inconsistent unit-of-measure conversions
        - PO funding shortages and approval delays
        - Complex three-way match scenarios
        - Partial shipments and backorders
        - Quality inspection dependencies
        - Contract and pricing variances
        - Freight surcharges and damaged goods
        - Complex tax and duty calculations associated with regulated tobacco operations
        - Data quality issues across SAP product, material, and pricing master data creating downstream finance impacts
        
        **These challenges result in:**
        - Payment delays
        - Increased operating cost
        - Low employee productivity
        - Poor supplier experience
        - Reduced visibility into root causes and process bottlenecks
        """)
    
    with col2:
        st.markdown("### Strategic Opportunity")
        st.markdown("""
        The organization is evaluating modernization through traditional AP automation platforms such as Roboyo or OpenText VIM.
        
        As transformation advisors, our recommendation is to maximize existing enterprise investments by leveraging the **Microsoft Copilot ecosystem and Agentic AI architecture** to enable intelligent AP automation rather than introducing additional workflow platforms.
        """)
        
        st.markdown("### Proposal Objective")
        st.markdown("""
        Design a cost-effective Agentic AP Transformation roadmap that:
        
        - ✅ Minimizes acquisition and ongoing operating costs
        - ✅ Leverages existing Microsoft and SAP investments
        - ✅ Improves supplier experience and response times
        - ✅ Increases employee productivity and reduces manual exception handling
        - ✅ Introduces intelligent orchestration across procurement, receiving, invoice validation, and vendor support
        - ✅ Creates a scalable foundation for autonomous AP operations
        
        The proposal defines the business case, target operating model, agent architecture, implementation roadmap, value realization plan, and expected outcomes across finance, procurement, and supplier operations.
        """)

st.markdown("---")

# Executive Summary
with st.container():
    st.markdown('<div class="section-header">📊 Executive Summary</div>', unsafe_allow_html=True)
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(
            label="Annual Invoice Volume",
            value="800,000",
            delta="Current ODC Platform"
        )
    
    with col2:
        st.metric(
            label="Estimated Annual Savings",
            value="$4.2M - $6.8M",
            delta="vs Traditional Solutions"
        )
    
    with col3:
        st.metric(
            label="Implementation Timeline",
            value="6-9 Months",
            delta="Phased Approach"
        )
    
    with col4:
        st.metric(
            label="ROI Period",
            value="12-18 Months",
            delta="Break-even"
        )

# Problem Statement
st.markdown('<div class="section-header">🎯 Current State Challenges</div>', unsafe_allow_html=True)

challenges_data = {
    'Challenge Category': [
        'Invoice Processing',
        'Data Quality',
        'Vendor Management',
        'Process Complexity',
        'System Integration',
        'Compliance & Tax'
    ],
    'Impact': ['Critical', 'High', 'Critical', 'High', 'Medium', 'Critical'],
    'Current Cost': ['$3.2M', '$1.8M', '$2.1M', '$1.5M', '$0.9M', '$1.2M'],
    'FTE Impact': [45, 25, 30, 20, 12, 15]
}

challenges_df = pd.DataFrame(challenges_data)

col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("### Key Pain Points")
    st.markdown("""
    - **Legacy ODC Platform**: Processing 800K invoices annually with manual intervention
    - **Complex 3-Way Matching**: Multiple exception types causing payment delays
    - **Data Quality Issues**: Errors in SAP master data (product, price, material)
    - **Fragmented P2P Process**: Different processes across regions and material categories
    - **Vendor Experience**: Delayed payments and unresolved queries
    - **Regulatory Complexity**: Tobacco industry tax calculations and duties
    - **High Exception Rate**: ~35-40% invoices require manual intervention
    """)

with col2:
    fig = px.bar(challenges_df, x='FTE Impact', y='Challenge Category', 
                 orientation='h', color='Impact',
                 color_discrete_map={'Critical': '#dc3545', 'High': '#ffc107', 'Medium': '#17a2b8'},
                 title='FTE Impact by Challenge Area')
    st.plotly_chart(fig, use_container_width=True)

# Solution Overview
st.markdown('<div class="section-header">💡 Proposed Solution: Microsoft Copilot Agentic Framework</div>', unsafe_allow_html=True)

tab1, tab2, tab3, tab4, tab5 = st.tabs(["🏗️ Architecture", "🤖 Agents", "💰 Cost Analysis", "📅 Roadmap", "📈 Benefits"])

with tab1:
    st.markdown("### Solution Architecture")
    
    # Create architecture diagram using streamlit-agraph
    nodes = []
    edges = []
    
    # Data Sources Layer
    nodes.extend([
        Node(id="email", label="Email/EDI\nInvoices", size=25, color="#E74C3C", shape="box"),
        Node(id="scan", label="Scanned\nDocuments", size=25, color="#E74C3C", shape="box"),
        Node(id="ariba", label="Ariba\nPO Data", size=25, color="#E74C3C", shape="box"),
        Node(id="sap_source", label="SAP\nERP", size=25, color="#E74C3C", shape="box"),
    ])
    
    # Microsoft Platform Layer
    nodes.extend([
        Node(id="doc_intel", label="Document\nIntelligence", size=25, color="#0078D4", shape="box"),
        Node(id="power_auto", label="Power\nAutomate", size=25, color="#0078D4", shape="box"),
        Node(id="copilot", label="Copilot\nStudio", size=25, color="#0078D4", shape="box"),
        Node(id="openai", label="Azure\nOpenAI", size=25, color="#0078D4", shape="box"),
    ])
    
    # Agentic Layer
    nodes.extend([
        Node(id="ingest", label="Invoice\nIngestion", size=25, color="#28a745", shape="ellipse"),
        Node(id="validate", label="Data\nValidation", size=25, color="#28a745", shape="ellipse"),
        Node(id="match", label="3-Way\nMatch", size=25, color="#28a745", shape="ellipse"),
        Node(id="exception", label="Exception\nResolution", size=25, color="#28a745", shape="ellipse"),
        Node(id="vendor", label="Vendor\nComm", size=25, color="#28a745", shape="ellipse"),
        Node(id="master", label="Master\nData", size=25, color="#28a745", shape="ellipse"),
        Node(id="tax", label="Tax &\nCompliance", size=25, color="#28a745", shape="ellipse"),
        Node(id="payment", label="Payment\nProcessing", size=25, color="#28a745", shape="ellipse"),
    ])
    
    # Integration Layer
    nodes.extend([
        Node(id="sap_conn", label="SAP\nConnector", size=25, color="#F39C12", shape="box"),
        Node(id="ariba_int", label="Ariba\nIntegration", size=25, color="#F39C12", shape="box"),
        Node(id="powerbi", label="Power BI\nAnalytics", size=25, color="#F39C12", shape="box"),
    ])
    
    # Edges - Data Sources to Platform
    edges.extend([
        Edge(source="email", target="doc_intel"),
        Edge(source="scan", target="doc_intel"),
        Edge(source="ariba", target="power_auto"),
        Edge(source="sap_source", target="power_auto"),
    ])
    
    # Platform to Agents
    edges.extend([
        Edge(source="doc_intel", target="ingest"),
        Edge(source="power_auto", target="ingest"),
        Edge(source="copilot", target="openai"),
        Edge(source="openai", target="ingest"),
    ])
    
    # Agent flows
    edges.extend([
        Edge(source="ingest", target="validate"),
        Edge(source="validate", target="match"),
        Edge(source="match", target="exception"),
        Edge(source="exception", target="vendor"),
        Edge(source="validate", target="master"),
        Edge(source="match", target="tax"),
        Edge(source="exception", target="payment"),
    ])
    
    # Agents to Integration
    edges.extend([
        Edge(source="payment", target="sap_conn"),
        Edge(source="vendor", target="ariba_int"),
        Edge(source="match", target="powerbi"),
        Edge(source="exception", target="powerbi"),
    ])
    
    config = Config(
        width=1000,
        height=600,
        directed=True,
        physics=True,
        hierarchical=True,
        nodeHighlightBehavior=True,
        highlightColor="#F7A7A6",
        collapsible=False,
        node={'labelProperty':'label'},
        link={'labelProperty': 'label', 'renderLabel': False}
    )
    
    st.markdown("#### Microsoft Copilot Agentic Architecture")
    agraph(nodes=nodes, edges=edges, config=config)
    
    # As-Is vs To-Be Process Maps
    st.markdown("### 📊 Process Transformation: As-Is vs To-Be")
    
    col_asis, col_tobe = st.columns(2)
    
    with col_asis:
        st.markdown("#### ❌ Current State (As-Is)")
        
        # As-Is Process using agraph
        asis_nodes = [
            Node(id="asis_1", label="Invoice\nReceipt", size=20, color="#E74C3C", shape="box"),
            Node(id="asis_2", label="Manual Data\nEntry\n⚠️ 15 min", size=20, color="#C0392B", shape="box"),
            Node(id="asis_3", label="Data\nValidation", size=20, color="#E74C3C", shape="box"),
            Node(id="asis_4", label="Manual\n3-Way Match", size=20, color="#C0392B", shape="box"),
            Node(id="asis_5", label="Exception\nHandling\n⚠️ 35-40%", size=20, color="#C0392B", shape="box"),
            Node(id="asis_6", label="Manual\nApproval", size=20, color="#E74C3C", shape="box"),
            Node(id="asis_7", label="Payment\nProcessing\n⚠️ 35 days", size=20, color="#C0392B", shape="box"),
        ]
        
        asis_edges = [
            Edge(source="asis_1", target="asis_2"),
            Edge(source="asis_2", target="asis_3"),
            Edge(source="asis_3", target="asis_4"),
            Edge(source="asis_4", target="asis_5"),
            Edge(source="asis_5", target="asis_6"),
            Edge(source="asis_6", target="asis_7"),
        ]
        
        asis_config = Config(
            width=450,
            height=400,
            directed=True,
            physics=False,
            hierarchical=True,
            nodeHighlightBehavior=True,
            node={'labelProperty':'label'},
            link={'renderLabel': False}
        )
        
        agraph(nodes=asis_nodes, edges=asis_edges, config=asis_config)
        
        st.markdown("""
        **Key Issues:**
        - 📝 Manual data entry (95% of time)
        - ⏱️ 15 minutes per invoice
        - ❌ 35-40% exception rate
        - 📞 2-day vendor query response
        - 💰 35-day payment cycle
        - 👥 147 FTEs required
        """)
    
    with col_tobe:
        st.markdown("#### ✅ Future State (To-Be)")
        
        # To-Be Process using agraph
        tobe_nodes = [
            Node(id="tobe_1", label="Auto\nIngestion\n✅ 2 min", size=20, color="#28a745", shape="ellipse"),
            Node(id="tobe_2", label="AI Data\nValidation", size=20, color="#27ae60", shape="ellipse"),
            Node(id="tobe_3", label="Auto\n3-Way Match", size=20, color="#28a745", shape="ellipse"),
            Node(id="tobe_4", label="AI Exception\nResolution\n✅ 60% auto", size=20, color="#27ae60", shape="ellipse"),
            Node(id="tobe_5", label="Auto\nApproval", size=20, color="#28a745", shape="ellipse"),
            Node(id="tobe_6", label="Smart\nPayment\n✅ 18 days", size=20, color="#27ae60", shape="ellipse"),
            Node(id="ai_layer", label="🤖 AI Agents\nOrchestration", size=25, color="#0078D4", shape="box"),
        ]
        
        tobe_edges = [
            Edge(source="tobe_1", target="tobe_2"),
            Edge(source="tobe_2", target="tobe_3"),
            Edge(source="tobe_3", target="tobe_4"),
            Edge(source="tobe_4", target="tobe_5"),
            Edge(source="tobe_5", target="tobe_6"),
            Edge(source="ai_layer", target="tobe_1", color="#0078D4"),
            Edge(source="ai_layer", target="tobe_2", color="#0078D4"),
            Edge(source="ai_layer", target="tobe_3", color="#0078D4"),
            Edge(source="ai_layer", target="tobe_4", color="#0078D4"),
        ]
        
        tobe_config = Config(
            width=450,
            height=400,
            directed=True,
            physics=False,
            hierarchical=True,
            nodeHighlightBehavior=True,
            node={'labelProperty':'label'},
            link={'renderLabel': False}
        )
        
        agraph(nodes=tobe_nodes, edges=tobe_edges, config=tobe_config)
        
        st.markdown("""
        **Key Benefits:**
        - 🤖 95% automated data capture
        - ⚡ 2 minutes per invoice
        - ✅ 75% auto-match rate
        - 💬 1-hour vendor response
        - 💰 18-day payment cycle
        - 👥 88 FTEs (40% reduction)
        """)
    
    st.markdown("### Architecture Components")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        #### Data Ingestion Layer
        - **Azure Document Intelligence**: OCR and data extraction
        - **Power Automate**: Workflow orchestration
        - **Email/EDI Integration**: Multi-channel invoice receipt
        
        #### Intelligence Layer
        - **Azure OpenAI GPT-4**: Natural language processing
        - **Copilot Studio**: Agent orchestration
        - **Semantic Kernel**: Agent framework
        """)
    
    with col2:
        st.markdown("""
        #### Integration Layer
        - **SAP OData/RFC**: Real-time ERP integration
        - **Ariba APIs**: PO and supplier data sync
        - **Power BI**: Analytics and reporting
        
        #### Security & Governance
        - **Azure AD**: Identity management
        - **Microsoft Purview**: Data governance
        - **Audit Logging**: Compliance tracking
        """)

with tab2:
    st.markdown("### Intelligent Agents Portfolio")
    
    agents = [
        {
            'name': '📥 Invoice Ingestion Agent',
            'description': 'Automated invoice capture from multiple channels (email, EDI, portal, scan)',
            'capabilities': [
                'Multi-format document processing (PDF, XML, EDI, images)',
                'Intelligent data extraction using Azure Document Intelligence',
                'Automatic vendor identification and routing',
                'Duplicate invoice detection',
                'Invoice classification by type (PO-based, non-PO, credit memo)'
            ],
            'integration': 'Power Automate, Azure Document Intelligence, SharePoint',
            'impact': 'Reduces manual data entry by 95%, processes invoices in <2 minutes'
        },
        {
            'name': '✅ Data Validation Agent',
            'description': 'Validates invoice data against SAP master data and business rules',
            'capabilities': [
                'Real-time validation against SAP master data',
                'Unit of measure conversion and standardization',
                'Price variance detection and tolerance checking',
                'Tax code validation for tobacco regulations',
                'Vendor master data verification',
                'PO availability and budget checking'
            ],
            'integration': 'SAP OData APIs, Azure OpenAI for fuzzy matching',
            'impact': 'Catches 98% of data errors before processing, reduces downstream exceptions'
        },
        {
            'name': '🔄 3-Way Match Agent',
            'description': 'Intelligent matching of invoice, PO, and goods receipt with exception handling',
            'capabilities': [
                'Automated 3-way matching (Invoice-PO-GR)',
                'Partial shipment reconciliation',
                'Quantity and price variance analysis',
                'Freight and surcharge allocation',
                'Quality inspection status verification',
                'Back-order management',
                'Tolerance-based auto-approval'
            ],
            'integration': 'SAP MM/FI modules, Ariba, Azure OpenAI',
            'impact': 'Auto-matches 75% of invoices, reduces match time from 15 min to 30 seconds'
        },
        {
            'name': '🔧 Exception Resolution Agent',
            'description': 'Proactive exception identification and resolution with human-in-the-loop',
            'capabilities': [
                'Exception categorization and prioritization',
                'Root cause analysis using historical patterns',
                'Automated resolution for common exceptions',
                'Intelligent routing to appropriate resolver',
                'Resolution recommendation engine',
                'Learning from past resolutions',
                'Escalation management'
            ],
            'integration': 'Copilot Studio, Azure OpenAI, Power Apps',
            'impact': 'Resolves 60% of exceptions automatically, reduces resolution time by 70%'
        },
        {
            'name': '💬 Vendor Communication Agent',
            'description': 'Automated vendor query handling and proactive communication',
            'capabilities': [
                'Natural language query understanding',
                'Payment status inquiries',
                'Invoice status tracking',
                'Automated email responses',
                'Proactive payment notifications',
                'Dispute management',
                'Multi-language support'
            ],
            'integration': 'Copilot Studio, Outlook, Teams, Ariba Supplier Network',
            'impact': 'Handles 80% of vendor queries automatically, improves response time to <1 hour'
        },
        {
            'name': '🗄️ Master Data Agent',
            'description': 'Continuous master data quality monitoring and correction',
            'capabilities': [
                'Real-time master data validation',
                'Anomaly detection in product/price/material masters',
                'Automated correction suggestions',
                'Data quality scoring',
                'Proactive data steward notifications',
                'Impact analysis of data errors',
                'Bulk data cleansing workflows'
            ],
            'integration': 'SAP MDM, Power Automate, Azure OpenAI',
            'impact': 'Improves master data accuracy by 85%, prevents cascading errors'
        },
        {
            'name': '📋 Tax & Compliance Agent',
            'description': 'Automated tax calculation and regulatory compliance for tobacco industry',
            'capabilities': [
                'Complex tax calculation (federal, state, local)',
                'Duty and excise tax computation',
                'Regulatory compliance checking',
                'Tax code validation and assignment',
                'Audit trail generation',
                'Tax reporting automation',
                'Jurisdiction-specific rule application'
            ],
            'integration': 'SAP Tax Engine, Azure OpenAI, Compliance databases',
            'impact': 'Ensures 100% tax compliance, reduces audit preparation time by 60%'
        },
        {
            'name': '💳 Payment Processing Agent',
            'description': 'Intelligent payment scheduling and execution',
            'capabilities': [
                'Payment term optimization',
                'Cash flow forecasting',
                'Early payment discount capture',
                'Payment batch creation',
                'Payment status tracking',
                'Remittance advice generation',
                'Payment exception handling'
            ],
            'integration': 'SAP FI, Banking systems, Power BI',
            'impact': 'Captures 95% of early payment discounts, optimizes working capital'
        }
    ]
    
    for agent in agents:
        with st.expander(f"**{agent['name']}**", expanded=False):
            st.markdown(f"**Description:** {agent['description']}")
            st.markdown("**Key Capabilities:**")
            for cap in agent['capabilities']:
                st.markdown(f"- {cap}")
            st.markdown(f"**Integration:** {agent['integration']}")
            st.markdown(f"**💡 Business Impact:** {agent['impact']}")

with tab3:
    st.markdown("### Cost-Benefit Analysis")
    
    # Cost comparison
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### Traditional Solutions (Roboyo/OpenText VIM)")
        traditional_costs = {
            'Cost Component': [
                'Software Licenses (3 years)',
                'Implementation Services',
                'Infrastructure',
                'Training & Change Management',
                'Annual Maintenance (Year 1-3)',
                'Integration Development',
                'Ongoing Support (3 years)'
            ],
            'Year 1': [1200000, 800000, 300000, 150000, 240000, 400000, 0],
            'Year 2': [0, 0, 50000, 50000, 280000, 0, 450000],
            'Year 3': [0, 0, 50000, 0, 320000, 0, 500000]
        }
        traditional_df = pd.DataFrame(traditional_costs)
        traditional_df['Total'] = traditional_df['Year 1'] + traditional_df['Year 2'] + traditional_df['Year 3']
        
        st.dataframe(traditional_df.style.format({'Year 1': '${:,.0f}', 'Year 2': '${:,.0f}', 
                                                   'Year 3': '${:,.0f}', 'Total': '${:,.0f}'}))
        
        total_traditional = traditional_df['Total'].sum()
        st.markdown(f"**Total 3-Year Cost: <span class='cost-savings'>${total_traditional:,.0f}</span>**", 
                   unsafe_allow_html=True)
    
    with col2:
        st.markdown("#### Microsoft Copilot Solution")
        copilot_costs = {
            'Cost Component': [
                'M365 Copilot Licenses (300 users)',
                'Azure OpenAI Consumption',
                'Document Intelligence',
                'Implementation Services',
                'Training & Change Management',
                'Power Platform Premium',
                'Ongoing Support (3 years)'
            ],
            'Year 1': [1080000, 180000, 120000, 450000, 100000, 180000, 0],
            'Year 2': [1080000, 200000, 130000, 0, 30000, 180000, 200000],
            'Year 3': [1080000, 220000, 140000, 0, 0, 180000, 220000]
        }
        copilot_df = pd.DataFrame(copilot_costs)
        copilot_df['Total'] = copilot_df['Year 1'] + copilot_df['Year 2'] + copilot_df['Year 3']
        
        st.dataframe(copilot_df.style.format({'Year 1': '${:,.0f}', 'Year 2': '${:,.0f}', 
                                               'Year 3': '${:,.0f}', 'Total': '${:,.0f}'}))
        
        total_copilot = copilot_df['Total'].sum()
        st.markdown(f"**Total 3-Year Cost: <span class='cost-savings'>${total_copilot:,.0f}</span>**", 
                   unsafe_allow_html=True)
    
    # Savings visualization
    st.markdown("### 💰 Cost Savings Analysis")
    
    savings = total_traditional - total_copilot
    savings_pct = (savings / total_traditional) * 100
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("3-Year Savings", f"${savings:,.0f}", f"{savings_pct:.1f}% reduction")
    
    with col2:
        st.metric("Year 1 Savings", f"${traditional_df['Year 1'].sum() - copilot_df['Year 1'].sum():,.0f}")
    
    with col3:
        st.metric("Annual Run Rate Savings", f"${(savings/3):,.0f}")
    
    # Operational savings
    st.markdown("### 📊 Operational Efficiency Gains")
    
    operational_savings = {
        'Metric': [
            'Invoice Processing Time',
            'Exception Resolution Time',
            'Vendor Query Response Time',
            'FTE Reduction',
            'Early Payment Discounts Captured',
            'Payment Cycle Time',
            'Data Quality Improvement'
        ],
        'Current State': ['15 min', '4 hours', '2 days', '147 FTEs', '45%', '35 days', '72%'],
        'Future State': ['2 min', '1.2 hours', '1 hour', '88 FTEs', '95%', '18 days', '98%'],
        'Improvement': ['87%', '70%', '96%', '40%', '111%', '49%', '36%'],
        'Annual Value': ['$2.1M', '$1.8M', '$900K', '$3.5M', '$1.2M', '$800K', '$1.1M']
    }
    
    operational_df = pd.DataFrame(operational_savings)
    st.dataframe(operational_df, use_container_width=True)
    
    total_operational_savings = sum([2.1, 1.8, 0.9, 3.5, 1.2, 0.8, 1.1])
    st.markdown(f"**Total Annual Operational Savings: <span class='cost-savings'>${total_operational_savings:.1f}M</span>**", 
               unsafe_allow_html=True)
    
    # ROI Chart
    years = ['Year 1', 'Year 2', 'Year 3']
    traditional_cumulative = [traditional_df['Year 1'].sum(), 
                             traditional_df['Year 1'].sum() + traditional_df['Year 2'].sum(),
                             total_traditional]
    copilot_cumulative = [copilot_df['Year 1'].sum(),
                         copilot_df['Year 1'].sum() + copilot_df['Year 2'].sum(),
                         total_copilot]
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=years, y=traditional_cumulative, name='Traditional Solution',
                            mode='lines+markers', line=dict(color='#dc3545', width=3)))
    fig.add_trace(go.Scatter(x=years, y=copilot_cumulative, name='Microsoft Copilot',
                            mode='lines+markers', line=dict(color='#28a745', width=3)))
    
    fig.update_layout(title='Cumulative Cost Comparison (3 Years)',
                     xaxis_title='Year', yaxis_title='Cumulative Cost ($)',
                     hovermode='x unified')
    
    st.plotly_chart(fig, use_container_width=True)

with tab4:
    st.markdown("### Implementation Roadmap")
    
    # Phased approach
    phases = {
        'Phase': ['Phase 1: Foundation', 'Phase 2: Core Agents', 'Phase 3: Advanced Intelligence', 'Phase 4: Optimization'],
        'Duration': ['Months 1-2', 'Months 3-5', 'Months 6-8', 'Months 9+'],
        'Key Deliverables': [
            'Platform setup, Data integration, Invoice Ingestion Agent, Initial training',
            'Data Validation Agent, 3-Way Match Agent, Exception Resolution Agent',
            'Vendor Communication Agent, Master Data Agent, Tax & Compliance Agent',
            'Payment Processing Agent, Analytics, Continuous improvement'
        ],
        'Success Metrics': [
            '100% invoice capture, 90% data extraction accuracy',
            '75% auto-match rate, 50% exception auto-resolution',
            '80% vendor query automation, 85% data quality',
            '95% discount capture, <18 day payment cycle'
        ]
    }
    
    phases_df = pd.DataFrame(phases)
    
    for idx, row in phases_df.iterrows():
        with st.expander(f"**{row['Phase']}** - {row['Duration']}", expanded=(idx==0)):
            col1, col2 = st.columns(2)
            with col1:
                st.markdown("**Key Deliverables:**")
                st.markdown(row['Key Deliverables'])
            with col2:
                st.markdown("**Success Metrics:**")
                st.markdown(row['Success Metrics'])
    
    # Gantt chart
    st.markdown("### Project Timeline")
    
    timeline_data = {
        'Task': [
            'Platform Setup & Integration',
            'Invoice Ingestion Agent',
            'Data Validation Agent',
            '3-Way Match Agent',
            'Exception Resolution Agent',
            'Vendor Communication Agent',
            'Master Data Agent',
            'Tax & Compliance Agent',
            'Payment Processing Agent',
            'Testing & UAT',
            'Training & Change Management',
            'Go-Live & Hypercare'
        ],
        'Start': [0, 0, 2, 3, 4, 5, 6, 6, 7, 7, 1, 8],
        'Duration': [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 8, 2]
    }
    
    timeline_df = pd.DataFrame(timeline_data)
    timeline_df['End'] = timeline_df['Start'] + timeline_df['Duration']
    
    # Create horizontal bar chart for timeline
    fig = go.Figure()
    
    colors = ['#0078D4', '#106EBE', '#2B88D8', '#50A0DC', '#74B8E0', 
              '#98D0E4', '#BCE8E8', '#50A0DC', '#2B88D8', '#106EBE', '#0078D4', '#005A9E']
    
    for idx, row in timeline_df.iterrows():
        fig.add_trace(go.Bar(
            y=[row['Task']],
            x=[row['Duration']],
            base=[row['Start']],
            orientation='h',
            name=row['Task'],
            marker=dict(color=colors[idx % len(colors)]),
            text=f"Month {row['Start']}-{row['End']}",
            textposition='inside',
            hovertemplate=f"<b>{row['Task']}</b><br>Start: Month {row['Start']}<br>Duration: {row['Duration']} months<br>End: Month {row['End']}<extra></extra>"
        ))
    
    fig.update_layout(
        title='Implementation Timeline (Months)',
        xaxis_title='Month',
        yaxis_title='',
        showlegend=False,
        height=500,
        xaxis=dict(range=[0, 10]),
        barmode='overlay'
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Risk mitigation
    st.markdown("### Risk Mitigation Strategy")
    
    risks = {
        'Risk': [
            'User Adoption',
            'Data Quality',
            'Integration Complexity',
            'Change Management',
            'Performance at Scale'
        ],
        'Mitigation': [
            'Comprehensive training, Champions program, Gradual rollout',
            'Master data cleansing sprint, Ongoing monitoring, Data steward enablement',
            'Phased integration, Robust testing, Fallback mechanisms',
            'Executive sponsorship, Communication plan, Quick wins demonstration',
            'Load testing, Scalable architecture, Performance monitoring'
        ],
        'Probability': ['Medium', 'Medium', 'Low', 'Medium', 'Low'],
        'Impact': ['High', 'High', 'High', 'Medium', 'Medium']
    }
    
    risks_df = pd.DataFrame(risks)
    st.dataframe(risks_df, use_container_width=True)

with tab5:
    st.markdown("### Business Benefits")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### Quantitative Benefits")
        st.markdown("""
        - **$4.2M - $6.8M** annual cost savings
        - **40% FTE reduction** (59 FTEs redeployed to value-add activities)
        - **87% faster** invoice processing (15 min → 2 min)
        - **70% reduction** in exception resolution time
        - **95% capture rate** for early payment discounts (+$1.2M annually)
        - **49% reduction** in payment cycle time (35 → 18 days)
        - **96% faster** vendor query response (2 days → 1 hour)
        - **36% improvement** in master data quality
        - **12-18 month** ROI period
        """)
    
    with col2:
        st.markdown("#### Qualitative Benefits")
        st.markdown("""
        - **Enhanced Vendor Experience**: Faster payments, proactive communication
        - **Improved Employee Experience**: Elimination of repetitive tasks, focus on strategic work
        - **Better Compliance**: 100% tax calculation accuracy, complete audit trails
        - **Scalability**: Handle volume growth without proportional cost increase
        - **Future-Ready**: Leverage existing Microsoft ecosystem, easy to extend
        - **Data-Driven Insights**: Real-time analytics and predictive capabilities
        - **Reduced Risk**: Automated controls, fraud detection, policy compliance
        - **Competitive Advantage**: Best-in-class AP operations
        """)
    
    # Benefits realization timeline
    st.markdown("### Benefits Realization Timeline")
    
    benefits_timeline = {
        'Quarter': ['Q1', 'Q2', 'Q3', 'Q4', 'Q5', 'Q6', 'Q7', 'Q8'],
        'Cumulative Savings ($M)': [0.3, 0.8, 1.5, 2.4, 3.5, 4.8, 6.2, 7.8],
        'Automation Rate (%)': [20, 35, 50, 65, 75, 82, 88, 92]
    }
    
    benefits_df = pd.DataFrame(benefits_timeline)
    
    fig = go.Figure()
    fig.add_trace(go.Bar(x=benefits_df['Quarter'], y=benefits_df['Cumulative Savings ($M)'],
                        name='Cumulative Savings', marker_color='#28a745'))
    fig.add_trace(go.Scatter(x=benefits_df['Quarter'], y=benefits_df['Automation Rate (%)'],
                            name='Automation Rate', yaxis='y2', mode='lines+markers',
                            line=dict(color='#0078D4', width=3)))
    
    fig.update_layout(
        title='Benefits Realization Over Time',
        xaxis_title='Quarter',
        yaxis_title='Cumulative Savings ($M)',
        yaxis2=dict(title='Automation Rate (%)', overlaying='y', side='right'),
        hovermode='x unified'
    )
    
    st.plotly_chart(fig, use_container_width=True)

# Technical Specifications
st.markdown('<div class="section-header">🔧 Technical Specifications</div>', unsafe_allow_html=True)

tech_col1, tech_col2 = st.columns(2)

with tech_col1:
    st.markdown("### Core Technologies")
    st.markdown("""
    - **Microsoft 365 Copilot**: Agent orchestration and user interface
    - **Azure OpenAI Service**: GPT-4 for natural language processing
    - **Copilot Studio**: Low-code agent development
    - **Azure Document Intelligence**: OCR and form recognition
    - **Power Automate**: Workflow automation
    - **Power Apps**: Custom user interfaces
    - **Semantic Kernel**: Agent framework and orchestration
    - **Azure Functions**: Serverless compute for integrations
    - **Azure Logic Apps**: Enterprise integration
    - **Power BI**: Analytics and reporting
    """)

with tech_col2:
    st.markdown("### Integration Points")
    st.markdown("""
    - **SAP ERP**: OData APIs, RFC, BAPI
    - **Ariba**: REST APIs, Supplier Network integration
    - **Email Systems**: Microsoft Graph API, Exchange
    - **Document Storage**: SharePoint, OneDrive
    - **Banking Systems**: SWIFT, ACH, payment gateways
    - **Tax Systems**: Vertex, Avalara integration
    - **Identity**: Azure AD, SSO
    - **Security**: Microsoft Purview, Azure Key Vault
    - **Monitoring**: Application Insights, Log Analytics
    """)

# Success Metrics
st.markdown('<div class="section-header">📈 Success Metrics & KPIs</div>', unsafe_allow_html=True)

kpi_col1, kpi_col2, kpi_col3 = st.columns(3)

with kpi_col1:
    st.markdown("### Efficiency Metrics")
    st.markdown("""
    - Invoice processing time
    - Exception resolution time
    - Vendor query response time
    - Payment cycle time
    - Straight-through processing rate
    - Auto-match rate
    """)

with kpi_col2:
    st.markdown("### Quality Metrics")
    st.markdown("""
    - Data extraction accuracy
    - Master data quality score
    - Tax calculation accuracy
    - Duplicate detection rate
    - Error rate
    - Compliance score
    """)

with kpi_col3:
    st.markdown("### Business Metrics")
    st.markdown("""
    - Cost per invoice
    - Early payment discount capture
    - Vendor satisfaction score
    - Employee satisfaction score
    - FTE productivity
    - ROI achievement
    """)

# Next Steps
st.markdown('<div class="section-header">🚀 Recommended Next Steps</div>', unsafe_allow_html=True)

next_steps = """
1. **Executive Alignment** (Week 1-2)
   - Present proposal to leadership
   - Secure executive sponsorship
   - Confirm budget and timeline

2. **Detailed Assessment** (Week 3-4)
   - Current state process mapping
   - Data quality assessment
   - Integration requirements analysis
   - User persona definition

3. **Proof of Concept** (Week 5-8)
   - Build Invoice Ingestion Agent prototype
   - Test with 1,000 sample invoices
   - Demonstrate ROI potential
   - Gather user feedback

4. **Business Case Finalization** (Week 9-10)
   - Refine cost-benefit analysis
   - Finalize implementation roadmap
   - Develop change management plan
   - Secure final approvals

5. **Implementation Kickoff** (Week 11+)
   - Assemble project team
   - Begin Phase 1 activities
   - Establish governance structure
   - Launch communication campaign
"""

st.markdown(next_steps)

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666; padding: 2rem;'>
    <p><strong>Prepared for: Large Cigarette Manufacturing Company</strong></p>
    <p>Confidential - For Internal Use Only</p>
    <p>Date: {}</p>
</div>
""".format(datetime.now().strftime("%B %d, %Y")), unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    col1, col2 = st.columns(2)
    with col1:
        st.image("https://img.icons8.com/color/96/000000/ibm.png", width=70)
    with col2:
        st.image("https://img.icons8.com/fluency/96/000000/microsoft.png", width=70)
    
    st.markdown("### Quick Navigation")
    st.markdown("""
    Use the tabs below to navigate:
    - **Architecture** - Solution design & process maps
    - **Agents** - 8 intelligent agents portfolio
    - **Cost Analysis** - ROI & savings breakdown
    - **Roadmap** - Implementation timeline
    - **Benefits** - Business value & metrics
    
    Scroll down for:
    - Technical Specifications
    - Success Metrics & KPIs
    - Recommended Next Steps
    """)
    
    st.markdown("---")
    st.markdown("### Key Contacts")
    st.markdown("""
    **Project Lead**  
    Shivendra Singh  
    Shivendra.Kumar.Singh@ibm.com
    
    **Technical Lead**  
    Nickolaus White  
    Nickolaus.White@ibm.com
    """)
    
    st.markdown("---")
    st.markdown("### Resources")
    st.markdown("""
    - [Microsoft Copilot Documentation](https://learn.microsoft.com/copilot/)
    - [Azure OpenAI Service](https://azure.microsoft.com/products/ai-services/openai-service)
    - [Power Platform](https://powerplatform.microsoft.com/)
    """)
