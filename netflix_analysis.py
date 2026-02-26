import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

plt.close('all')

df = pd.read_csv(r"C:\Users\Admin\Desktop\Netflix_Content_Analysis\netflix_titles.csv")

print("First 5 Rows:")
print(df.head())

print("\nShape of Dataset:")
print(df.shape)

print("\nColumns:")
print(df.columns)

type_counts = df['type'].value_counts()
print("\nMovies vs TV Shows Count:")
print(type_counts)

plt.figure()
sns.countplot(x='type', data=df)
plt.title("Movies vs TV Shows Distribution")
plt.show()

genre_counts = df['genre'].value_counts()
print("\nGenre Distribution:")
print(genre_counts)

plt.figure()
genre_counts.plot(kind='bar')
plt.title("Genre Distribution")
plt.show()

year_counts = df['release_year'].value_counts().sort_index()
print("\nRelease Trend by Year:")
print(year_counts)

plt.figure()
year_counts.plot(kind='line', marker='o')
plt.title("Release Trend by Year")
plt.show()

country_counts = df['country'].value_counts()
print("\nContent by Country:")
print(country_counts)

plt.figure()
country_counts.plot(kind='bar')
plt.title("Content by Country")
plt.show()

print("\nAverage Duration Overall:")
print(df['duration_min'].mean())

print("\nAverage Duration by Type:")
print(df.groupby('type')['duration_min'].mean())

plt.figure()
sns.boxplot(x='type', y='duration_min', data=df)
plt.title("Duration Comparison")
plt.show()

print("\nBusiness Insights:")
print("Movies slightly dominate over TV Shows.")
print("Focus more on top-performing genres.")
print("Maintain consistent yearly releases.")
print("Invest more in top content-producing countries.")
print("Optimize content duration based on audience preference.")

print("\nAnalysis Completed Successfully")