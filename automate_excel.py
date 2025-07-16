import pandas as pd

# Step 1: Excel file ka path
file_path = "business.xlsx"

# Step 2: Excel read karo aur header force set karo
df = pd.read_excel(file_path, header=0)

# 👇 Debug line: Check actual column names
print("🧪 DEBUG Columns:", df.columns)

# Step 3: Remove old summary rows
df = df[~df['WORK'].astype(str).str.upper().isin(['TODAY', 'TOTAL'])]

# Step 4: Sab totals nikaalo
total_row = {
    'WORK': 'TODAY',
    'SELF': df['SELF'].sum(),
    'CASH': df['CASH'].sum(),
    'ONL': df['ONL'].sum(),
    'TRAN': df['TRAN'].sum(),
    'MOBILE': ''
}

final_row = total_row.copy()
final_row['WORK'] = 'TOTAL'

# Step 5: Total rows ko dataframe me jodo
df = pd.concat([df, pd.DataFrame([total_row, final_row])], ignore_index=True)

# Step 6: Output file banao
df.to_excel("business_updated.xlsx", index=False)

print("✅ DONE: 'TODAY' aur 'TOTAL' rows add kar diye gaye!")
