import pandas as pd
from collections import Counter
import matplotlib.pyplot as trap
from wordcloud import WordCloud
import streamlit as st

# Load a small portion of the dataset
df = pd.read_csv("cord19_subset.csv", nrows=11, on_bad_lines='skip', engine='python')

# Preview the first 10 rows
print("the first five rows are \n")
print(df.head(10))

# Print the number of rows and columns
print("the number of rows and columns \n")
print(df.shape)

# Show data types for each column
print("the data types of the cols  \n")
print(df.dtypes)

# Count missing values per column
print("the missing values in the important cols \n")
print(df.isnull().sum())

# Display basic statistics for numeric columns
print("the basic statics is as follows: \n")
print(df.describe())

# Identify columns with missing values
print("the columns with many missing values are: \n")
cols_missing = df.columns[df.isnull().any()]
print(cols_missing)

# Show rows where the first column with missing values is null
the_most_missing_col = df[df[cols_missing[0]].isnull()] 
print("the column with many missing values are: \n")
print(the_most_missing_col)

# Fill missing values with 'not available' for all columns
for col in df.columns:
    if df[col].isnull().any():
        df[col].fillna('not available', inplace = True)

# Strip whitespace from string columns
df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)

# Convert publish_time to datetime
df["publish_year"] = pd.to_datetime(df["publish_time"], errors="coerce")
print(df.info())
print(df.isnull().sum())
df.head()

# Save cleaned CSV
df.to_csv('iris.csv', index = False)

# Extract year from publish_time
df['publication_year'] = df['publish_year'].dt.year

# Fill missing abstracts with empty string
df['abstract'] = df['abstract'].fillna('')

# Count words in abstracts
df['abstract_word_count'] = df['abstract'].apply(lambda x: len(x.split()))
df[['abstract', 'abstract_word_count']].head()

# Summary statistics of abstract word counts
df['abstract_word_count'].describe()

# Save CSV again (optional)
df.to_csv('iris.csv', index = False)

# Count papers per publication year
paper_per_year = df['publication_year'].value_counts().sort_index()
print("the paper per year is ")
print(paper_per_year)

# Filter journals containing certain words
words_to_look = ['research','covid']
pattern = '|'.join(words_to_look)
contains_words = df[df['journal'].str.contains(pattern, case=False, na=False)]
result = contains_words['title']
print("the top journals publishing COVID-19 research are: ")
print(result)

# Split titles into words
words_under_title = df['title'].dropna().astype(str).str.split()
words_flat = [word for sublist in words_under_title for word in sublist]

# Count occurrences of each word in titles
word_counts = Counter(words_flat)
most_common = word_counts.most_common(10)
print(most_common)

# Plot number of publications per year
trap.figure()
trap.plot(paper_per_year.index, paper_per_year.values, marker = 'o')
trap.title('Number of Publications over years')
trap.xlabel('year')
trap.ylabel('number of publications')
trap.grid(True)

# Get top 3 journals by number of publications
top_journals = df['journal'].value_counts().head(3)
print("the top journals published are: ")
print(top_journals)

# Plot top journals as a bar chart
trap.figure()
trap.bar(top_journals.index, top_journals.values)
trap.xlabel("journal")
trap.ylabel("number of publication")
trap.title("top publishing journals")

# Generate word cloud from paper titles
text = "".join(df['title'].dropna().astype(str))
wordcloud = WordCloud(width=100, height=100, background_color='white').generate(text)
trap.figure(figsize=(10,5))
trap.imshow(wordcloud, interpolation = 'bilinear')
trap.axis('off')

# Count papers by source
paper_counts = df['source'].dropna().value_counts()

# Plot distribution of papers by source
trap.figure()
trap.bar(paper_counts.index, paper_counts.values)
trap.xlabel("source")
trap.ylabel("number of papers")
trap.title("distribution of papers counts by source")
trap.show()

# Set up Streamlit dashboard title
st.title("COVID-19 Research Dashboard")
st.write("Welcome to the COVID-19 Research Dashboard")
st.header("Paper Analysis")
st.write("Here you can analyze the papers based on source, year or keyword")

# Streamlit sidebar for filters
st.sidebar.header("Filters")
sources = ["All"] + df['source'].dropna().unique().tolist()
selected_source = st.sidebar.selectbox("Select Sources", sources)

# Define min and max publication years for slider
min_year = int(df['publication_year'].min())
max_year = int(df['publication_year'].max())
year_range = st.sidebar.slider("Select Publication Year", min_value = min_year, max_value = max_year, value = (min_year, max_year))

# Filter DataFrame based on sidebar selections
filtered_df = df.copy()
if selected_source != "All":
    filtered_df = filtered_df[filtered_df['source'] == selected_source]

filtered_df = filtered_df[
    (filtered_df['publication_year']>= year_range[0]) &
    (filtered_df['publication_year']<= year_range[1])
]

# Display filtered papers
st.write(f"showing {len(filtered_df)} papers")
st.dataframe(filtered_df[['paper_id', 'title', 'source', 'publication_year',]])

# Top sources bar chart in Streamlit
top_sources = filtered_df['source'].value_counts().head()
st.subheader("top sources")
fig, ax = trap.subplots()
ax.bar(top_sources.index, top_sources.values)
trap.xlabel("sources")
trap.ylabel("number of papers")
st.pyplot(fig)

# Display a random sample of the data
st.subheader("random sample of data")
st.dataframe(df.head())
