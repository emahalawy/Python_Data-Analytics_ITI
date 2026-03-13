import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
import warnings

from read import fetch_users

warnings.filterwarnings("ignore")
sns.set_theme(style="whitegrid", palette="muted")
plt.rcParams["figure.figsize"] = (10, 5)

PLOTS_DIR = "plots"
os.makedirs(PLOTS_DIR, exist_ok=True)

# LOAD DATA
df = fetch_users()

# SECTION 2 — BASIC EXPLORATION
print("\n" + "═" * 60)
print("  SECTION 2 — BASIC DATA EXPLORATION")
print("═" * 60)

print(f"\n Shape:  {df.shape[0]} rows × {df.shape[1]} columns")

print("\n Column names:")
for c in df.columns:
    print(f"   {c}")

print("\n Data types:")
print(df.dtypes.to_string())

missing = df.isnull().sum()
print("\n Missing values per column:")
if missing.sum() == 0:
    print("No missing values ")
else:
    print(missing[missing > 0].to_string())

dupes = df.duplicated().sum()
print(f"\n Duplicate rows: {dupes}")

print("\n Summary statistics (numeric columns):")
print(df.describe().round(2).to_string())

print("\n Value counts — gender:")
print(df["gender"].value_counts().to_string())

print("\n Value counts — bloodGroup:")
print(df["bloodGroup"].value_counts().to_string())

print("\n Value counts — eyeColor:")
print(df["eyeColor"].value_counts().to_string())

print("\n Value counts — role:")
print(df["role"].value_counts().to_string())

print("\n Value counts — country:")
print(df["country"].value_counts().to_string())


# SECTION 4 — ANALYSIS
print("\n" + "═" * 60)
print("  SECTION 4 — ANALYSIS")
print("═" * 60)

# Q1 — Average age
avg_age = df["age"].mean()
print(f"\n❶  Average age of all users: {avg_age:.1f} years")

# Q2 — Average age by gender
avg_age_gender = df.groupby("gender")["age"].mean().round(1)
print("\n❷  Average age by gender:")
print(avg_age_gender.to_string())

# Q3 — Users per gender
gender_counts = df["gender"].value_counts()
print("\n❸  Number of users per gender:")
print(gender_counts.to_string())

# Q4 — Top 10 cities
top_cities = df["city"].value_counts().head(10)
print("\n❹  Top 10 cities with the most users:")
print(top_cities.to_string())

# Q5 — Average height & weight
print(f"\n❺  Average height: {df['height'].mean():.1f} cm")
print(f"    Average weight: {df['weight'].mean():.1f} kg")

# Q6 — Correlation
r_age_height = df["age"].corr(df["height"])
r_age_weight = df["age"].corr(df["weight"])
print(f"\n❻  Correlation  age ↔ height : {r_age_height:.3f}")
print(f"    Correlation  age ↔ weight : {r_age_weight:.3f}")
print("    → Values near 0 = weak / no linear relationship in this dataset")


# SECTION 5 — VISUALIZATIONS
print("\n" + "═" * 60)
print("  SECTION 5 — SEABORN VISUALIZATIONS")
print("═" * 60)


# ── Plot 1 : Age Distribution 
fig, ax = plt.subplots()
sns.histplot(data=df, x="age", bins=15, kde=True, color="steelblue", ax=ax)
ax.axvline(avg_age, color="red", linestyle="--",
           label=f"Mean: {avg_age:.1f} yrs")
ax.set_title("Age Distribution of Users", fontsize=14, fontweight="bold")
ax.set_xlabel("Age")
ax.set_ylabel("Count")
ax.legend()
plt.tight_layout()
path = f"{PLOTS_DIR}/plot1_age_distribution.png"
plt.savefig(path, dpi=150)
plt.show()
print(f" Saved {path}")


# Plot 2 : Average Age by Gender 
fig, ax = plt.subplots(figsize=(7, 5))
avg_age_g = df.groupby("gender")["age"].mean().reset_index()
bars = sns.barplot(data=avg_age_g, x="gender", y="age",
                   palette="pastel", ax=ax)
for p in ax.patches:
    ax.annotate(f"{p.get_height():.1f}",
                (p.get_x() + p.get_width() / 2, p.get_height()),
                ha="center", va="bottom", fontsize=12, fontweight="bold")
ax.set_title("Average Age by Gender", fontsize=14, fontweight="bold")
ax.set_xlabel("Gender")
ax.set_ylabel("Average Age")
plt.tight_layout()
path = f"{PLOTS_DIR}/plot2_avg_age_by_gender.png"
plt.savefig(path, dpi=150)
plt.show()
print(f"  Saved {path}")


#  Plot 3 : Top 10 Cities 
fig, ax = plt.subplots(figsize=(11, 5))
top10 = df["city"].value_counts().head(10).reset_index()
top10.columns = ["city", "count"]
sns.barplot(data=top10, x="city", y="count", palette="Blues_d", ax=ax)
ax.set_title("Top 10 Cities by Number of Users", fontsize=14, fontweight="bold")
ax.set_xlabel("City")
ax.set_ylabel("Number of Users")
plt.xticks(rotation=35, ha="right")
plt.tight_layout()
path = f"{PLOTS_DIR}/plot3_top_10_cities.png"
plt.savefig(path, dpi=150)
plt.show()
print(f" Saved {path}")


#  Plot 4 : Age vs Height Scatter 
fig, ax = plt.subplots()
sns.scatterplot(data=df, x="age", y="height", hue="gender", alpha=0.7, ax=ax)
sns.regplot(data=df, x="age", y="height", scatter=False,
            color="black", line_kws={"linestyle": "--", "linewidth": 1.2}, ax=ax)
ax.set_title(f"Age vs Height   (r = {r_age_height:.3f})",
             fontsize=14, fontweight="bold")
ax.set_xlabel("Age")
ax.set_ylabel("Height (cm)")
plt.tight_layout()
path = f"{PLOTS_DIR}/plot4_age_vs_height.png"
plt.savefig(path, dpi=150)
plt.show()
print(f"  Saved {path}")


#Plot 5 : Age vs Weight Scatter 
fig, ax = plt.subplots()
sns.scatterplot(data=df, x="age", y="weight", hue="gender",
                alpha=0.7, palette="Set2", ax=ax)
sns.regplot(data=df, x="age", y="weight", scatter=False,
            color="black", line_kws={"linestyle": "--", "linewidth": 1.2}, ax=ax)
ax.set_title(f"Age vs Weight   (r = {r_age_weight:.3f})",
             fontsize=14, fontweight="bold")
ax.set_xlabel("Age")
ax.set_ylabel("Weight (kg)")
plt.tight_layout()
path = f"{PLOTS_DIR}/plot5_age_vs_weight.png"
plt.savefig(path, dpi=150)
plt.show()
print(f" Saved {path}")


# Plot 6 : Height & Weight Boxplots by Gender 
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

sns.boxplot(data=df, x="gender", y="height", palette="pastel", ax=axes[0])
axes[0].set_title("Height by Gender", fontsize=13, fontweight="bold")
axes[0].set_xlabel("Gender")
axes[0].set_ylabel("Height (cm)")

sns.boxplot(data=df, x="gender", y="weight", palette="Set2", ax=axes[1])
axes[1].set_title("Weight by Gender", fontsize=13, fontweight="bold")
axes[1].set_xlabel("Gender")
axes[1].set_ylabel("Weight (kg)")

plt.tight_layout()
path = f"{PLOTS_DIR}/plot6_hw_by_gender.png"
plt.savefig(path, dpi=150)
plt.show()
print(f" Saved {path}")


#Plot 7 : Correlation Heatmap 
fig, ax = plt.subplots(figsize=(6, 5))
corr_matrix = df[["age", "height", "weight"]].corr()
sns.heatmap(corr_matrix, annot=True, fmt=".2f", cmap="coolwarm",
            center=0, linewidths=0.5, ax=ax)
ax.set_title("Correlation Matrix — Age, Height, Weight",
             fontsize=13, fontweight="bold")
plt.tight_layout()
path = f"{PLOTS_DIR}/plot7_correlation_heatmap.png"
plt.savefig(path, dpi=150)
plt.show()
print(f" Saved {path}")


print("\n" + "═" * 60)
print(" ALL DONE — check the 'plots/' folder for saved images")
print("═" * 60)