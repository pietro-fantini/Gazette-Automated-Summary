# Import functions
import summarize_GPT as sGPT
import extract_text as et

# Input data
api_key = "key"
pdf_path = "path"
summary_path = "path"

# Extract text from PDF
pdf_text = et.extract_text(pdf_path)

# Summarize PDF
summary = sGPT.summarize_GPT(pdf_text, api_key)

# Save the summary to a file
with open(summary_path, 'w', encoding='utf-8') as file:
    file.write(summary)

print(f"Summary saved to {summary_path}")