# Optima(Stress Analysis Prototype (TRL4))

## 1. Project Overview
**Optima** is a high-fidelity wellness prototype designed for rapid burnout detection and intervention. This project satisfies **Technology Readiness Level (TRL) 4** by demonstrating component validation in a laboratory (local) environment using real-time AI API integration and deterministic logic gates.
[![Live Demo](https://img.shields.io/badge/Demo-Live_Prototype-6366F1?style=for-the-badge&logo=streamlit)](https://optima-1.streamlit.app/)

## 2. TRL 4 Definition of Done
To meet the TRL4 criteria, this prototype validates the following:
* **Component Integration:** Seamless communication between the UI (Streamlit), the Classifier (Gemini 3.0 Flash preview), and the Protocol Engine.
* **Structured Output:** AI transformation of unstructured user text into actionable JSON data.
* **Simulated Validation:** System performance verified against 5+ simulated burnout scenarios.

---

## 3. System Architecture
The application is decoupled into three primary modules to ensure scalability and ease of testing.

| Module | File | Responsibility |
| :--- | :--- | :--- |
| **Frontend** | `app.py` | Manages state navigation, UI styling, and user interaction. |
| **AI Classifier** | `ai_module.py` | Handles API calls to Gemini 3.0 for emotional extraction. |
| **Protocol Engine** | `engine.py` | Executes deterministic Level 1-3 recovery logic. |

---

## 4. Core Logic: 3-Tier Intervention Gate
The system bypasses generic advice by routing the AI's `stress_level` output (1–10) through a strict deterministic gate:

### **LEVEL 1: OPTIMIZED STEADY-STATE** (Score 1-3)
* **Tone:** Systems nominal. Focus on sustainable pace.
* **Actions:** Hydration check, strict 5:00 PM logout, win-logging.

### **LEVEL 2: PERFORMANCE MAINTENANCE** (Score 4-7)
* **Tone:** High RPM detected. Scope trimming required.
* **Actions:** Task deletion, 50/10 Pomodoro, async meeting conversion.

### **LEVEL 3: HARD RESET** (Score 8-10)
* **Tone:** Hardware redlining. Critical intervention required.
* **Actions:** Emergency sick day, 12-hour digital detox, 9-hour sleep cycle.

---

## 5. Technical Stack
* **Core:** Python 3.10+
* **UI Framework:** Streamlit
* **AI Model:** Google Gemini 3.0 Flash
* **Config:** `python-dotenv` for local credential management

---

## 6. Setup & Installation (Local Development)

1.  **Clone the Repository:**
    ```bash
    git clone https://github.com/habrev/optima.git
    cd optima
    ```

2.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Environment Configuration:**
    Create a `.env` file in the root directory:
    ```env
    GEMINI_API_KEY=your_actual_api_key_here
    ```

4.  **Run the Prototype:**
    ```bash
    streamlit run app.py
    ```

---

## 7. TRL4 Test Scenarios
The prototype has been validated against the following simulated inputs:

1.  **"TC-01: Manual Inputs: Users give their journal inputs manually"** -> *Triggers Level 1*
2.  **"TC-02: Acute Overwork (Redline)": "Worked 14 hours today but I'm still behind. My heart is racing, my hands are shaking, and I can't think straight. I feel like a total failure."** -> *Triggers Level 2*
3.  **"TC-03: High Cynicism (Drift)": "My client ghosted me again. Honestly, I don't even care anymore. The whole project feels pointless and I’m just doing the bare minimum to stay afloat."** -> *Triggers Level 3*
4. **"TC-04: Scope/Agency Loss": "My manager added 4 'quick' syncs during my deep-work block. I have zero control over my schedule and I'm starting to snap at my teammates."** -> *Triggers Level 4*
5. **"TC-05: Anticipatory Anxiety": "It's Sunday night and I have a physical pit in my stomach thinking about the stand-up tomorrow. I didn't even enjoy my weekend because I was dreading Monday."** -> *Triggers Level 5*
6. **"TC-06: Steady State (Baseline)": "Had a productive sprint. Feeling a bit tired but satisfied with the PR I submitted. Looking forward to logging off at 5."** -> *Triggers Level 6*


---

## 8. License & Usage
This is a TRL4 research prototype. Developed for local environment validation and proof-of-concept for AI-driven burnout intervention.