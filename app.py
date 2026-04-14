import streamlit as st
import os
from dotenv import load_dotenv
from ai_module import analyze_burnout
from engine import get_recovery_protocol

# Initialize Environment and Page Config
load_dotenv()
st.set_page_config(page_title="Burnout Engine // TRL4", layout="wide", page_icon="🔋")

# --- UI STYLING ---
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: #fafafa; }
    div[data-testid="stMetricValue"] { color: #00ffcc; }
    .stAlert { background-color: #161b22; border: 1px solid #30363d; }
    </style>
    """, unsafe_allow_html=True)

# --- SESSION STATE MANAGEMENT ---
if 'user_input' not in st.session_state:
    st.session_state.user_input = ""

# --- SIDEBAR: TRL4 VALIDATION SUITE ---
with st.sidebar:
    st.header("TRL4 Validation Suite")
    st.info("Select a validated stress profile to test the Heuristic Engine logic.")
    
    test_scenarios = {
        "Manual Input": "",
        "TC-01: Acute Overwork (Redline)": "Worked 14 hours today but I'm still behind. My heart is racing, my hands are shaking, and I can't think straight. I feel like a total failure.",
        "TC-02: High Cynicism (Drift)": "My client ghosted me again. Honestly, I don't even care anymore. The whole project feels pointless and I’m just doing the bare minimum to stay afloat.",
        "TC-03: Scope/Agency Loss": "My manager added 4 'quick' syncs during my deep-work block. I have zero control over my schedule and I'm starting to snap at my teammates.",
        "TC-04: Anticipatory Anxiety": "It's Sunday night and I have a physical pit in my stomach thinking about the stand-up tomorrow. I didn't even enjoy my weekend because I was dreading Monday.",
        "TC-05: Steady State (Baseline)": "Had a productive sprint. Feeling a bit tired but satisfied with the PR I submitted. Looking forward to logging off at 5."
    }
    
    selected_name = st.selectbox("Select Test Scenario:", list(test_scenarios.keys()))
    
    if st.button("Load Scenario"):
        st.session_state.user_input = test_scenarios[selected_name]
        st.rerun()

    st.divider()
    st.caption("Engine: Gemini 3 Flash Preview")

# --- MAIN INTERFACE ---
st.title("Burnout Recovery Engine")
st.subheader("Adaptive Resilience: Recovery Protocols for Digital Professionals")

# Input Area
user_text = st.text_area(
    "System Status Update:", 
    value=st.session_state.user_input, 
    height=150, 
    placeholder="Describe your current workload, physical state, or 'vibe'..."
)

if st.button("Initialize Diagnostics", type="primary"):
    if not user_text:
        st.warning("Telemetry input required. Please describe your state or load a test case.")
    else:
        with st.spinner("Analyzing telemetry via Gemini 3 Flash..."):
            # 1. AI Analysis (Extraction Layer)
            data = analyze_burnout(user_text)
            
            if data:
                # 2. Results Display
                st.divider()
                col1, col2, col3 = st.columns(3)
                
                with col1:
                    st.metric("Stress Level", f"{data['stress_level_int']}/10")
                with col2:
                    risk_pct = int(data['burnout_risk_score'] * 100)
                    st.metric("Burnout Risk", f"{risk_pct}%")
                with col3:
                    st.metric("Primary State", data['primary_emotion'].upper())
                
                # 3. Heuristic Engine (Logic Layer)
                # We pass the stress_level_int directly to our deterministic logic
                protocol = get_recovery_protocol(data['stress_level_int'])
                
                # 4. Humanized Output
                st.markdown(f"### Strategy: `{protocol['tier']}`")
                
                with st.container():
                    st.markdown(f"**Engine Note:** *{protocol['tone']}*")
                    st.write("---")
                    st.write("**Recommended Optimization Protocols:**")
                    for action in protocol['actions']:
                        st.write(f"🔹 {action}")
                
                
            else:
                st.error("Analysis failed. Check your API key and connection.")

