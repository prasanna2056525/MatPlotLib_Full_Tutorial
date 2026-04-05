import pandas as pd 
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('netflix_titles.csv')

# Data Cleaning: Handle missing values
df = df.dropna(subset=['type','release_year', 'rating', 'country', 'duration'])

types_counts = df['type'].value_counts()
plt.figure(figsize=(8, 5))
plt.bar(types_counts.index, types_counts.values, color=['skyblue', 'salmon'])
plt.title('Distribution of Movies and TV Shows on Netflix')
plt.xlabel('Type')
plt.ylabel('Count')
plt.tight_layout()
plt.savefig('movies_vs_tvshows.png')
plt.show()

# Analyze the distribution of ratings
rating_counts = df['rating'].value_counts().head(10)  # Show top 10 ratings
plt.figure(figsize=(10, 6))
plt.pie(rating_counts.values, labels=rating_counts.index, autopct='%1.1f%%', startangle=90)
plt.title('Distribution of Ratings on Netflix') 
plt.tight_layout
plt.axis('equal')
plt.savefig('ratings_distribution.png')
plt.show()

# Analyze the duration of movies and TV shows
movies_df = df[df['type'] == 'Movie'].copy()
movies_df['duration'] = movies_df['duration'].str.replace(' min', '').astype(int)
plt.figure(figsize=(10, 6))
plt.hist(movies_df['duration'], bins=30, color='lightgreen', edgecolor='black')
plt.title('Distribution of Movie Durations on Netflix')
plt.xlabel('Duration (minutes)')    
plt.ylabel('Count')
plt.tight_layout()
plt.savefig('movie_durations_histogram.png')
plt.show()

# Analyze the release year distribution
release_year_counts = df['release_year'].value_counts().sort_index()
plt.figure(figsize=(12, 6))
plt.scatter(release_year_counts.index, release_year_counts.values, color='orange')
plt.title('Number of Titles Released Each Year on Netflix')
plt.xlabel('Release Year')
plt.ylabel('No of shows/movies released')
plt.tight_layout()
plt.savefig('release_year_distribution_scatter.png')
plt.show()

# Analyze the distribution of content by country
country_counts = df['country'].value_counts().head(10)
plt.figure(figsize=(12, 6))
plt.barh(country_counts.index, country_counts.values, color='purple')
plt.title('Top 10 Countries with Most Content on Netflix')
plt.xlabel('No of shows/movies')
plt.ylabel('Country')
plt.tight_layout()
plt.savefig('top_countries_content.png')
plt.show()

content_by_year = df.groupby('release_year')['type'].value_counts().unstack().fillna(0)

fig, ax = plt.subplots(1,2,figsize=(12, 6))

ax[0].plot(content_by_year.index, content_by_year['Movie'], label='Movies', color='blue')
ax[0].set_title('Number of Movies Released Each Year on Netflix')
ax[0].set_xlabel('Release Year')
ax[0].set_ylabel('Number of Movies')

ax[1].plot(content_by_year.index, content_by_year['TV Show'], label='TV Shows', color='red')
ax[1].set_title('Number of TV Shows Released Each Year on Netflix')
ax[1].set_xlabel('Release Year')
ax[1].set_ylabel('Number of TV Shows')

fig.suptitle('Trends in Movies and TV Shows Released on Netflix Over Time')
plt.tight_layout()
plt.savefig('movies_tvshows_trends.png')
plt.show()

