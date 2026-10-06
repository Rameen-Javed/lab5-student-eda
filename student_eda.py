
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = {
    "StudentID": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 11],
    "Gender": [
        "Female", "Male", "Female", "Male",
        "Female", "Male", "Female", "Male",
        "Female", "Male", "Female", "Female"
    ],
    "StudyHours": [5, 3, 6, 2, 7, 4, 8, 3, 6, 5, 7, 7],
    "Attendance(%)": [90, 80, 95, 75, 92, 85, 96, 78, 88, 82, 94, 94],
    "Marks": [85, 70, 90, np.nan, 88, 72, 95, np.nan, 80, 75, 92, 92]
}

df = pd.DataFrame(data)

df.to_csv("student_performance.csv", index=False)

df = pd.read_csv("student_performance.csv")

print("Shape:", df.shape)
print("\nDataset Information:")
print(df.info())

print("\nMissing values per column:")
print(df.isnull().sum())

print("\nDuplicate rows:", df.duplicated().sum())

df = df.drop_duplicates()

median_marks = df["Marks"].median()
df["Marks"] = df["Marks"].fillna(median_marks)

print("\nMedian Marks:", median_marks)
print("After cleaning:", df.shape)

plt.hist(df["Marks"], bins=6, edgecolor="black")
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.title("Marks Distribution")
plt.savefig("marks_histogram.png")
plt.show()

plt.boxplot(df["Marks"])
plt.ylabel("Marks")
plt.title("Marks Boxplot")
plt.savefig("marks_boxplot.png")
plt.show()

plt.scatter(df["StudyHours"], df["Marks"])
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.title("Study Hours vs Marks")
plt.savefig("studyhours_vs_marks.png")
plt.show()

correlation_matrix = df[
    ["StudyHours", "Attendance(%)", "Marks"]
].corr()

print("\nCorrelation matrix:")
print(correlation_matrix)

gender_summary = df.groupby("Gender")[["Marks", "Attendance(%)"]].mean()

print("\nAverage Marks and Attendance by Gender:")
print(gender_summary)

print("\nSaved marks_histogram.png, marks_boxplot.png, studyhours_vs_marks.png")
