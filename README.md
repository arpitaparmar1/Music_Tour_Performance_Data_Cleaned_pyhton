# Music_Tour_Performance_Data_Cleaned_pyhton
This project is a comprehensive Data Engineering and Analytics pipeline designed to transform raw, unstructured music industry data into actionable insights. It specifically targets the complexities of concert tour datasets, which often contain "messy" artifacts like Wikipedia-style citations and varied currency formatting.

This project focuses on cleaning and visualizing a dataset of the world's highest-grossing concert tours. The script processes raw, "messy" data—typically sourced from web-based tables like Wikipedia—to handle inconsistent formatting, currency symbols, and reference citations.

📂 Project Structure:

clean_data.py: The main Python script containing the cleaning logic and visualization code.

messy_data.csv: The raw dataset containing symbols ($ , †, ‡) and Wikipedia-style reference brackets (e.g., [1]).

clean_data.csv: The processed, analysis-ready dataset produced by the script.

🛠️ Data Cleaning Process:

The script performs several automated cleaning steps using pandas and numpy:

Column Normalization: Cleans whitespace and special characters from headers.

Citation Removal: Removes bracketed references (e.g., [5]) and special status symbols from tour titles and artists.

Financial Conversion: Converts currency strings (like $1,200,000) into numeric floats for mathematical analysis.

Sorting Logic: Extracts start years from date ranges (e.g., "2002–2005") to allow for chronological sorting.

📊 Key Visualizations:

The script generates several insights using seaborn and matplotlib:

Top 5 Tours by Shows: A bar chart comparing the number of shows per tour, colored by artist.

Revenue Growth Over Time: A line plot showing the trend of total shows by year.

Correlation Analysis: A regression plot showing the relationship between the number of shows and actual gross revenue.

Market Share: A pie chart illustrating the revenue distribution among the top 5 highest-earning artists.

Revenue Density: A violin plot showing the distribution and density of gross revenue for the top artists.

🚀 How to Run:

1.Ensure you have Python installed.

2.Install the required libraries:

Bash

pip install pandas numpy matplotlib seaborn

3.Update the file path in clean_data.py to point to your local messy_data.csv.

4.Run the script:

Bash

python clean_data.py
