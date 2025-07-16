import pandas as pd
import os

# 📁 Folder jahan sab employee files hain
folder_path = "employee_data"
summary = []

for file in os.listdir(folder_path):
    if file.endswith(".xlsx") and not file.startswith("~$"):  # Skip temp Excel files
        file_path = os.path.join(folder_path, file)
        df = pd.read_excel(file_path, header=0)

        # Old summary rows remove karo
        df = df[~df['WORK'].astype(str).str.upper().isin(['TODAY', 'TOTAL'])]

        # Total values calculate karo
        totals = {
            'EMPLOYEE': file.replace('.xlsx', ''),
            'SELF': df['SELF'].sum(),
            'CASH': df['CASH'].sum(),
            'ONL': df['ONL'].sum(),
            'TRAN': df['TRAN'].sum(),
        }

        summary.append(totals)

# Final summary table
summary_df = pd.DataFrame(summary)

# Master summary file save karo
summary_df.to_excel("master_summary.xlsx", index=False)

print("✅ DONE: Sab employees ka summary ban gaya → master_summary.xlsx")
