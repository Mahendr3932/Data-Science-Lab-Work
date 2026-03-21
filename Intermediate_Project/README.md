# Customer Segmentation using Machine Learning

## Description

The objective of this project is to perform customer segmentation using machine learning techniques. The goal is to group customers into different segments based on their characteristics, which can help businesses understand customer behavior and improve decision-making.

## Dataset

* **Source:** Provided dataset (train.csv)
* **Description:**
  The dataset contains customer-related information such as demographic details, profession, spending habits, and other attributes. These features are used to segment customers into different categories.

## Steps Performed

### 1. Data Cleaning

* Handled missing values using forward fill method
* Checked for null values using `isnull().sum()`
* Ensured data consistency for analysis

### 2. Exploratory Data Analysis (EDA)

* Analyzed distribution of features
* Identified relationships between variables
* Observed patterns in customer attributes

### 3. Data Visualization

* Used plots such as count plots, histograms, and bar charts
* Visualized relationships between features
* Identified trends and patterns in customer data

### 4. Feature Engineering

* Encoded categorical variables using label encoding
* Prepared data for machine learning models

### 5. Model Building

* Applied multiple machine learning models:

  * Decision Tree Classifier
  * Random Forest Classifier
* Also used K-Means Clustering for unsupervised learning

### 6. Model Evaluation

* Evaluated model using:

  * Accuracy Score
  * Confusion Matrix
  * Classification Report

## Results

* Successfully segmented customers into different groups
* Achieved good accuracy using classification models
* Identified meaningful patterns in customer behavior

## Tools Used

* Python
* NumPy
* Pandas
* Matplotlib / Seaborn
* Scikit-learn

## Conclusion

Customer segmentation helps in understanding different customer groups and their behavior. Machine learning models can effectively classify and cluster customers, enabling better business strategies and targeted marketing.

## Author

Mahendra C
