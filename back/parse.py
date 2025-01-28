import pdfplumber
import pandas as pd

# Path to the PDF file
pdf_path = ("/home/max/projects/Medical_manager_helper/back/"
            "Приказ_Министерства_здравоохранения_Российской_Федерации_от_9_ноября_2012_г._№_711н.pdf")

# Initialize an empty list to store extracted tables
all_tables = []

with pdfplumber.open(pdf_path) as pdf:
    for page_number, page in enumerate(pdf.pages, start=1):
        print(f"Processing page {page_number}...")
        # Extract tables from the page
        tables = page.extract_tables()
        for table in tables:
            # Convert table into a DataFrame
            df = pd.DataFrame(table[1:], columns=table[0])
            all_tables.append(df)

print(all_tables)

# Save all tables into Excel or CSV
output_path = "extracted_tables.xlsx"
with pd.ExcelWriter(output_path) as writer:
    for i, table in enumerate(all_tables, start=1):
        sheet_name = f"Table_{i}"
        table.to_excel(writer, sheet_name=sheet_name, index=False)

print(f"All tables extracted and saved to {output_path}.")
