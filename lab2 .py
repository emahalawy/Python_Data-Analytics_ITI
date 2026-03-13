import pandas as pd 



# 1 - Load the file students.csv and make sure Score Date is parsed as datetime. 

df = pd.read_csv("students.CSV")
df["Score Date"] = pd.to_datetime(df["Score Date"]) 

# 2 - Print the shape, columns list, and data types of the DataFrame. 

print("Shape:", df.shape)
print("Columns:", df.columns.tolist())
print("Data Types:\n", df.dtypes)

# 3- Show the first 7 rows and the last 3 rows. 

print("First 7 rows:", df.head(7))

print("Last 3 rows:", df.tail(3))

# 4 - Show how many missing values in each column. 

print("Missing values in each column:\n", df.isnull().sum())

# 5 -  What is the average, minimum, and maximum Grade? 

print("Average:", df["Grade"].mean())
print("Minimum:", df["Grade"].min())
print("Maximum:", df["Grade"].max())

# 6 - How many unique cities are there? List them.

print("Number of unique cities:", len(df["City"].unique()))
print("Unique cities:", df["City"].unique())


# 7 - Use value_counts() to show how many students per Subject. 

print("Students per Subject:\n", df["Subject"].value_counts())  


# 8 - Select only the columns: Name, Grade, Subject, City. 

selected_columns = df[["Name", "Grade", "Subject", "City"]]
print("Selected columns:\n", selected_columns)

# 9 - Show all students who Passed and have Grade ≥ 85. 

passed_students = df[(df["Passed"] == True) & (df["Grade"] >= 85)]
print("Students who Passed and have Grade ≥ 85:\n", passed_students)

# 10 - Show students whose Name contains the letter "a" or "A" (case insensitive). 

students_with_a = df[df["Name"].str.contains("a", case=False)]
print("Students whose Name contains 'a' or 'A':\n", students_with_a)

# 11 - Show students in Cairo or Alexandria with Grade < 80. 

students_in_cities = df[((df["City"] == "Cairo") | (df["City"] == "Alexandria")) & (df["Grade"] < 80)]
print("Students in Cairo or Alexandria with Grade < 80:\n", students_in_cities)

# 12 - Show students with Grade between 80 and 90 (inclusive). 


print("Students with Grade between 80 and 90 (inclusive):\n")
print(df[(df["Grade"].between(80, 90))])


# 13 - Using .loc, change Khaled's grade from 55 to 68.

df.loc[df["Name"] == "Khaled", "Grade"] = 68
print("Updated DataFrame:\n", df)

# 14 - Add a new column Is_Excellent that is True if Grade ≥ 90, False otherwise (vectorized).

df["Is_Excellent"] = df["Grade"] >= 90
print("DataFrame with Is_Excellent column:\n", df)


# 15 - Fill missing Grade values with the average Grade. 

df["Grade"].fillna(df["Grade"].mean(), inplace=True)
print("DataFrame after filling missing Grade values:\n", df)


# 16 - Fill missing Score Date values with the most common date (mode)

df["Score Date"].fillna(df["Score Date"].mode()[0], inplace=True)
print("DataFrame after filling missing Score Date values:\n", df)   

# 17 - Add a new column Final_Grade = Grade + 5 (bonus points)

df["Final_Grade"] = df["Grade"] + 5
print("DataFrame with Final_Grade column:\n", df)

# 18 - •Create a column Grade_Category using pd.cut with bins:
#0–69 → "Fail" 
#70–79 → "Average" 
#80–89 → "Good" 
#90–100 → "Excellent" 

bins = [0, 69, 79, 89, 100]
labels = ["Fail", "Average", "Good", "Excellent"]
df["Grade_Category"] = pd.cut(df["Grade"], bins=bins, labels=labels)
print("DataFrame with Grade_Category column:\n", df)

# 19 - Remove the column Student ID. 
print(df.columns)  # Check column names before dropping
df.drop("Student ID", axis=1, inplace=True)
print("DataFrame after removing Student ID column:\n", df)

# 20 - Keep only students who Passed 

df = df[df["Passed"] == True]
print("DataFrame with only students who Passed:\n", df)

# 21 - Sort the DataFrame by Grade descending.

df.sort_values(by="Grade", ascending=False)
print("DataFrame sorted by Grade descending:\n", df)

# 22 - Sort by City ascending, then inside each city sort by Grade descending

df.sort_values(by=["City", "Grade"], ascending=[True, False])
print("DataFrame sorted by City ascending and Grade descending:\n", df)

# 23 - Add a column Rank that ranks students by Grade (1 = highest, handle ties with 'min'). 

df["Rank"] = df["Grade"].rank(method="min", ascending=False)
print("DataFrame with Rank column:\n", df)


# 24 - Show the top 4 students with the highest grades (use nlargest). 

print("Top 4 students with the highest grades:\n", df.nlargest(4, "Grade"))

# 25 - Show the 3 youngest students (use nsmallest on Age).

print("3 youngest students:\n", df.nsmallest(3, "Age"))

# 26 - Find the student(s) with the highest Grade and show their Name and Grade. 

print("Student(s) with the highest Grade:\n", df.loc[df["Grade"].idxmax(), ["Name", "Grade"]])  

# 27 - After filling missing grades, recalculate the average Grade per Subject. 

print("Average Grade per Subject:\n", df.groupby("Subject")["Grade"].mean())


# 28 - Create a new column City_Avg that shows the average grade of each student's city (using transform).

df["City_Avg"] = df.groupby("City")["Grade"].transform("mean")
print("DataFrame with City_Avg column:\n", df)

# 29 - Show the subject with the highest average grade. 

print("Subject with the highest average grade:\n", df.groupby("Subject")["Grade"].mean().idxmax())

