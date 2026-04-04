import pandas as pd
 
# --- 1. Create DataFrame ---
data = {
    'Name':    ['Ravi', 'Sita', 'Arjun', 'Priya', 'Kiran'],
    'Subject': ['Maths', 'Science', 'English', 'Maths', 'Science'],
    'Marks':   [85, 90, 78, 92, 70],
    'Age':     [20, 21, 22, 20, 23]
}
df = pd.DataFrame(data)
print("DataFrame:\n", df)
 
# --- 2. Basic Info ---
print("\nShape:", df.shape)
print("\nInfo:"); df.info()
print("\nDescribe:\n", df.describe())
 
# --- 3. Select Columns & Rows ---
print("\nNames Column:\n", df['Name'])
print("\nFirst 2 Rows:\n", df.head(2))
print("\nRow by index:\n", df.iloc[1])
 
# --- 4. Filtering ---
passed = df[df['Marks'] > 80]
print("\nStudents with Marks > 80:\n", passed)
 
# --- 5. Sorting ---
sorted_df = df.sort_values('Marks', ascending=False)
print("\nSorted by Marks:\n", sorted_df)
 
# --- 6. GroupBy ---
group = df.groupby('Subject')['Marks'].mean()
print("\nAverage Marks by Subject:\n", group)
 
# --- 7. Add & Drop Column ---
df['Grade'] = df['Marks'].apply(lambda x: 'A' if x >= 85 else 'B')
print("\nWith Grade Column:\n", df)
 
# --- 8. Save & Read CSV ---
df.to_csv('students.csv', index=False)
new_df = pd.read_csv('students.csv')
print("\nRead from CSV:\n", new_df)
