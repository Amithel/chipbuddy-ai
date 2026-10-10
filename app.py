import streamlit as st
from nebius_client import call_nebius_agent

st.set_page_config(
    page_title="ChipBuddy AI | Logic & Embedded Verification",
    page_icon="⚡",
    layout="wide"
)

st.title("⚡ ChipBuddy AI")
st.caption("Embedded C & Verilog Logic Verification Agent powered by NVIDIA models on Nebius Cloud")

# Sidebar
with st.sidebar:
    st.header("Project Info")
    st.markdown("**Infrastructure:** Nebius Cloud API")
    st.markdown("**Engine:** NVIDIA Nemotron-70B")
    st.info("Verification assistant for STM32, 8051, ESP32, and Verilog digital designs.")

tab1, tab2, tab3 = st.tabs([
    "🔍 Code Verification & Analysis", 
    "🧪 Testbench Generator", 
    "📖 Datasheet QA"
])

with tab1:
    st.subheader("Embedded C / Verilog Bug Fixer")
    user_code = st.text_area(
        "Paste Embedded C or Verilog code:",
        height=200,
        placeholder="// Example: void GPIO_Init(void) { ... }"
    )
    if st.button("Analyze Code", type="primary"):
        if user_code.strip():
            with st.spinner("Analyzing registers and logic..."):
                res = call_nebius_agent("analyzer", user_code)
                st.markdown(res)
        else:
            st.warning("Please enter some code first.")

with tab2:
    st.subheader("Verilog Testbench Builder")
    module_code = st.text_area(
        "Paste Verilog Module:",
        height=200,
        placeholder="module full_adder(input a, b, cin, output sum, cout); ... endmodule"
    )
    if st.button("Generate Testbench"):
        if module_code.strip():
            with st.spinner("Generating testbench stimulus..."):
                tb_res = call_nebius_agent("testbench", module_code)
                st.code(tb_res, language="verilog")
        else:
            st.warning("Please paste a Verilog module.")

with tab3:
    st.subheader("Microcontroller Specs QA")
    qa_prompt = st.text_area(
        "Ask about MCU registers or peripherals:",
        height=100,
        placeholder="How do I configure Timer 1 in 8051 for 8-bit auto-reload?"
    )
    if st.button("Query Datasheet"):
        if qa_prompt.strip():
            with st.spinner("Retrieving hardware specs..."):
                ans = call_nebius_agent("datasheet", qa_prompt)
                st.markdown(ans)
        else:
            st.warning("Please enter a question.")