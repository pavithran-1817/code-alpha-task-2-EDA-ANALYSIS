# 📚 Web Scraping and Exploratory Data Analysis (EDA)

## 📌 Project Overview

This project focuses on collecting book information from a website using Python Web Scraping techniques and performing Exploratory Data Analysis (EDA) to understand the dataset.

The project uses Python libraries such as BeautifulSoup, Requests, Pandas, Matplotlib, Seaborn, and SciPy to collect, clean, analyze, and visualize book data.

## 🎯 Project Objectives

- Collect book details from a website using web scraping.
- Extract book names, prices, and ratings.
- Store the collected data in a CSV file.
- Explore the dataset using Pandas.
- Identify patterns, trends, and possible outliers.
- Perform statistical analysis and hypothesis testing.
- Visualize the results using charts.

## 🛠️ Technologies Used

- Python
- BeautifulSoup
- Requests
- Pandas
- Matplotlib
- Seaborn
- SciPy
- VS Code

## 📂 Project Structure

```text
webscrapingproject/
│
├── scraper.py
├── eda.py
├── books.csv
└── README.md
```

## 🔹 Task 1: Web Scraping

Web scraping is the process of extracting information from websites.

### Data Collected

- Book Name
- Book Price (£)
- Book Rating

### Libraries Used

- Requests – To access website data.
- BeautifulSoup – To extract information from HTML.
- Pandas – To organize the collected data.

### Output

The scraped information was saved in `books.csv`.

Total records collected: **1000 books**

## 🔹 Task 2: Exploratory Data Analysis (EDA)

EDA is the process of examining and understanding a dataset using statistical methods and visualizations.

### 1. Dataset Overview

- Total Rows: 1000
- Total Columns: 3
- Book Name: Text data
- Price (£): Numerical data
- Rating: Categorical data

### 2. Data Cleaning

The following checks were performed:

- Missing value detection
- Duplicate record detection
- Invalid price detection
- Outlier detection using the IQR method

### Results

- Missing Values: 0
- Duplicate Records: 0
- Invalid Prices: 0
- Outliers: 0

### 3. Statistical Analysis

| Statistical Measure | Result |
|---|---:|
| Average Price | £35.07 |
| Highest Price | £59.99 |
| Lowest Price | £10.00 |
| Median Price | £35.98 |
| Standard Deviation | £14.45 |

### 4. Rating Distribution

| Rating | Number of Books |
|---|---:|
| One | 226 |
| Two | 196 |
| Three | 203 |
| Four | 179 |
| Five | 196 |

### 5. Data Visualization

The following visualizations were created:

- Histogram – To understand book price distribution.
- Count Plot – To analyze book rating distribution.
- Box Plot – To identify price variations and outliers.

### 6. Hypothesis Testing

Spearman Rank Correlation was used to examine the relationship between book prices and ratings.

**Results:**

- Correlation: 0.0292
- P-value: 0.3560

**Interpretation:**

Since the p-value is greater than 0.05, no statistically significant monotonic relationship was found between book prices and ratings in this dataset.

## 📊 Key Findings

1. The dataset contains 1000 book records.
2. The average book price is approximately £35.07.
3. The highest book price is £59.99.
4. The lowest book price is £10.00.
5. No missing or duplicate records were found.
6. No invalid prices or IQR outliers were detected.
7. No statistically significant relationship was found between price and rating.

## ▶️ How to Run the Project

### Step 1: Install Required Libraries

```bash
python -m pip install requests beautifulsoup4 pandas matplotlib seaborn scipy
```

### Step 2: Run Web Scraping

```bash
python scraper.py
```

### Step 3: Run Exploratory Data Analysis

```bash
python eda.py
```

## 🏁 Conclusion

This project successfully demonstrates how to collect real-world data through web scraping and analyze it using Exploratory Data Analysis techniques.

The analysis helped identify price distributions, rating patterns, statistical summaries, and data quality issues.

This project provided practical experience in Python programming, data collection, data cleaning, statistical analysis, and data visualization.

## 👨‍💻 Author

**Python Web Scraping and EDA Project**

**Tools:** Python | Pandas | BeautifulSoup | Matplotlib | Seaborn | SciPy
