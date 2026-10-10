# ⚡ ChipBuddy AI
Embedded C & Verilog Logic Verification Agent powered by NVIDIA models on NVIDIA Cloud / API.

## 🚀 Overview
ChipBuddy AI is a lightweight developer utility designed to assist microcontroller and FPGA developers (STM32, 8051, ESP32, Verilog) with:
1. **Code Analysis & Bug Fixing:** Detecting register mismatches, missing clock enables, and compiler optimization traps in Embedded C and Verilog.
2. **Testbench Generation:** Automatically writing synthesizable Verilog testbenches with clock generation and stimulus vectors.
3. **Datasheet QA:** Quick peripheral configuration and register lookup.

## 🛠️ Tech Stack
* **Core Model:** NVIDIA Nemotron-3.5 / Llama-3.1
* **Backend:** Python, OpenAI SDK, FastAPI/Streamlit
* **Infrastructure:** NVIDIA Build Serverless APIs

## ⚙️ Local Setup
1. Clone the repository:
   ```bash
   git clone [https://github.com/Amithel/chipbuddy-ai.git](https://github.com/Amithel/chipbuddy-ai.git)
   cd chipbuddy-ai