import pandas as pd

# Master file ka path
master_file = "master_report.xlsx"

# Empty DataFrame with same columns
columns = ['DATE', 'EMPLOYEE', 'SELF', 'CASH', 'ONL', 'TRAN']
empty_df = pd.DataFrame(columns=columns)

# Save blank DataFrame to file (overwrite)
empty_df.to_excel(master_file, index=False)

print("✅ DONE: master_report.xlsx file cleaned (content removed, structure retained).")
