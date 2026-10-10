import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    base_url="https://integrate.api.nvidia.com/v1",
    api_key=os.getenv("NEBIUS_API_KEY")
)

MODEL_NAME = "nvidia/nemotron-3.5-lightning-30b-a3b"

SYSTEM_PROMPTS = {
    "analyzer": """
You are an expert Embedded Systems & Hardware Verification Engineer.
Analyze code for hardware issues:
1. Register configuration/address mismatches and pin direction errors.
2. Synth/timing warning traps, unhandled interrupts, or infinite loop issues.
3. Missing include/header dependencies.
Provide a formatted summary of issues and a corrected code block. Do not show internal thinking process.
""",
    "testbench": """
You are a Digital Design Verification Specialist in Verilog HDL.
Generate a clean, synthesizable/simulatable Verilog testbench block for the provided hardware code.
Include clock generation, reset sequence, stimulus vectors, and simple $display statements. Do not show internal thinking process.
""",
    "datasheet": """
You are a concise Microcontroller Datasheet QA Assistant.
Extract registers, pinouts, timing specs, or peripheral capabilities accurately. Do not show internal thinking process.
"""
}

def call_nebius_agent(task_type: str, input_text: str) -> str:
    system_prompt = SYSTEM_PROMPTS.get(task_type, SYSTEM_PROMPTS["analyzer"])
    
    try:
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": input_text}
            ],
            temperature=0.2,
            max_tokens=4096,  # Allows full code output without truncation
            extra_body={"chat_template_kwargs": {"enable_thinking": False}} # Hides thinking process
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"API Error: {str(e)}"