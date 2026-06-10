# Data Analytics Project 1 – Data Cleaning & Preparation 
## Overview 
This project is part of the DecodeLabs Industrial Training Kit 2026. 
The main goal of this project is to clean and prepare raw data by identifying missing values, removing 
duplicate records, and correcting incorrect data formats. --- 
## Objectives - Identify missing or null values - Remove duplicate records - Correct date, number, and text formats - Prepare clean and reliable data for analysis --- 
## Tools Used - Microsoft Excel - Python (Optional) - Pandas Library --- 
## Dataset 
The dataset contains raw and unclean data used for practicing data cleaning techniques. 
File: - Dataset for Data Analytics.xlsx 
--- 
## Steps Performed 
1. Checked for missing values 
2. Removed duplicate rows 
3. Corrected invalid date formats 
4. Standardized text formatting 
5. Verified data accuracy --- 
## Skills Learned - Data Cleaning - Data Preparation - Data Validation - Excel Basics - Python Basics --- 
## Project Outcome 
Successfully cleaned the dataset and prepared it for further analysis and visualization. 
## Author 
Kavali Shiva Shankar Vara Prasad



# Data Analytics Project 2 – Exploratory Data Analysis (EDA) 
## Overview 
This project is part of the DecodeLabs Industrial Training Kit 2026. 
The main goal of this project is to perform Exploratory Data Analysis (EDA) to understand patterns, 
trends, and distributions in the dataset. --- 
## Objectives - Analyze the dataset using statistics - Identify trends and patterns - Detect outliers in data - Summarize important observations --- 
## Key Requirements - Calculate mean, median, and count - Identify trends and outliers - Generate meaningful insights - Understand data distributions --- 
## Tools Used - Microsoft Excel - Python - Pandas - NumPy 
- Matplotlib --- 
## Dataset 
The dataset used in this project contains raw data for analysis and exploration. --- 
## Steps Performed 
1. Loaded the dataset 
2. Checked data types and structure 
3. Calculated statistical values 
4. Identified trends and patterns 
5. Detected outliers 
6. Summarized key findings --- 
## Skills Learned - Exploratory Data Analysis - Descriptive Statistics - Data Interpretation - Analytical Thinking - Data Visualization Basics --- 
## Project Outcome 
Successfully analyzed the dataset and discovered useful insights, trends, and patterns through EDA 
techniques. 
--- 
## Author  
Kavali Shiva Shankar Vara Prasad

An open-source README.md file layout tailored for this repository or project submission is outlined below.
------------------------------
## Project 3: SQL Data Analysis
The Project 3: SQL Data Analysis curriculum, powered by DecodeLabs, serves as the foundational milestone for the 2026 Industrial Training Kit (p. 1). It transitions technical skillsets from procedural thinking to pure declarative relational logic (p. 6). This shift ensures data analysis accurately extracts business intelligence from raw datasets (pp. 2, 4).
------------------------------
## 🎯 Project Goal
The primary objective is to use structured queries to filter, group, aggregate, and transform massive, unstructured datasets into actionable executive insights (pp. 2, 4, 11).
------------------------------
## ⚙️ Key Requirements & Core Concepts

* Declarative Querying: Master writing precise SELECT statements to state what data you need rather than how to fetch it (pp. 4, 6).
* Row-Level Funneling: Isolate crucial records using structural pattern matching, comparisons, and equalities via WHERE (p. 9).
* Categorical Bucketing: Group individual row metrics into organized, distinct relational buckets using GROUP BY (p. 10).
* Mathematical Aggregations: Apply operations like COUNT(), SUM(), and AVG() while accounting for hidden NULL structures (p. 11).
* Presentation Customization: Organize final human-readable outputs seamlessly with custom column aliases and ORDER BY sorting routines (p. 12).

------------------------------
## 🏗️ The Logical Execution Order
To avoid the common "Alias Trap" (attempting to reference a column alias inside a WHERE block before the SELECT sequence executes) (p. 15), this project requires structuring and reading scripts according to the database engine's true execution path (pp. 13-14):

1. FROM / JOIN   ➔ Locates the physical data tables
2. WHERE         ➔ Filters individual, granular rows
3. GROUP BY      ➔ Categorizes items into structured buckets
4. HAVING        ➔ Filters aggregated dataset buckets
5. SELECT        ➔ Picks designated columns & evaluates calculations
6. ORDER BY      ➔ Sorts the final presentation layer

------------------------------
## 🚀 Getting Started

   1. Set up your local relational database management environment (such as PostgreSQL, MySQL, or SQL Server).
   2. Load the project's designated baseline raw dataset into your workspace.
   3. Construct declarative, logic-driven scripts following the internal execution sequences outlined above (p. 14).
   4. Test and validate your aggregated buckets against edge cases and hidden null elements (pp. 11, 17).

------------------------------
## 📈 Qualification Criteria

* Requirement: You must complete Project 3 fully to unlock additional project paths for the following week (p. 3).
* Standard: All submitted query files are manually verified for exactness, query optimization, and structural code quality (p. 3).

# README.md

# Data Analytics Project 4 – E-Commerce Data Visualization Dashboard

## Project Overview

This project focuses on analyzing an E-Commerce dataset and creating interactive visualizations to uncover meaningful business insights. The objective is to transform raw data into easy-to-understand charts and dashboards that support data-driven decision-making.

The project demonstrates the complete data analytics process, including data cleaning, visualization, and interpretation of results.

---

## Objectives

* Import and understand the E-Commerce dataset.
* Clean and prepare the data for analysis.
* Create various visualizations to identify trends and patterns.
* Build an interactive dashboard.
* Generate business insights from the visualizations.

---

## Tools and Technologies Used

* Microsoft Excel
* Power BI (Recommended)
* Visual Studio Code (Optional)
* Python (Pandas, Matplotlib) – Optional

---

## Dataset Description

The dataset contains information related to customer orders placed through an online shopping platform.

### Key Attributes

* Order ID
* Order Date
* Customer ID
* Product Name
* Quantity
* Unit Price
* Total Price
* Shipping Address
* Payment Method
* Order Status
* Tracking Number
* Items in Cart
* Coupon Code
* Referral Source

---

## Project Workflow

### 1. Data Collection

* Import the provided Excel dataset into the selected analytics tool.

### 2. Data Cleaning

* Check for missing values.
* Remove duplicate records.
* Verify data types.
* Correct inconsistencies in the dataset.

### 3. Data Visualization

Create the following visualizations:

#### Product-wise Sales Analysis

* Bar Chart
* Displays revenue generated by each product.

#### Order Status Distribution

* Pie Chart
* Shows the proportion of delivered, cancelled, and shipped orders.

#### Monthly Sales Trend

* Line Chart
* Identifies sales patterns over time.

#### Payment Method Analysis

* Column Chart
* Highlights customers' preferred payment methods.

#### Referral Source Analysis

* Bar Chart
* Determines which marketing channels contribute most to sales.

#### Coupon Usage Analysis

* Donut Chart
* Evaluates the effectiveness of promotional coupons.

#### Quantity Sold by Product

* Stacked Bar Chart
* Identifies the most frequently purchased products.

---

## Dashboard Components

The dashboard includes:

* Total Sales
* Total Orders
* Total Quantity Sold
* Average Order Value
* Product-wise Revenue
* Monthly Sales Trend
* Order Status Breakdown
* Payment Method Analysis
* Referral Source Performance
* Coupon Usage Insights

---

## Key Insights

After completing the analysis, the dashboard helps answer questions such as:

* Which products generate the highest revenue?
* Which months experience peak sales?
* What are the most preferred payment methods?
* Which referral sources attract more customers?
* How effective are discount coupons?
* What percentage of orders are successfully delivered?

---

## Expected Outcomes

* Improved understanding of data visualization techniques.
* Ability to interpret business data effectively.
* Experience in designing analytical dashboards.
* Development of practical data storytelling skills.

---

## Project Structure

```
Project4/
│
├── Dataset for Data Analytics (3).xlsx
├── Data Analytics Project 4.pdf
├── Dashboard.pbix
├── README.md
└── Report.pdf
```

---

## How to Run the Project

### Using Power BI

1. Open Power BI Desktop.
2. Import the Excel dataset.
3. Perform data cleaning if required.
4. Create the specified visualizations.
5. Design the dashboard.
6. Save the dashboard as a `.pbix` file.

### Using Python (Optional)

Install the required libraries:

```bash
pip install pandas matplotlib openpyxl
```

Load the dataset:

```python
import pandas as pd

df = pd.read_excel("Dataset for Data Analytics (3).xlsx")
print(df.head())
```

---

## Conclusion

This project demonstrates how data visualization can transform raw E-Commerce data into actionable insights. By creating dashboards and interpreting trends, organizations can make informed business decisions and improve overall performance.

---

### Author

**Name:** Kavali Shiva Shankar Vara Prasad
**Course:** Data Analytics




