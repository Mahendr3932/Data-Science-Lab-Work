# IMDB Movie Ratings Prediction using Machine Learning

## Author

Mahendra C

## Description

The objective of this project is to predict IMDB movie ratings using machine learning techniques and analyze the key factors that influence movie success. This project applies regression models and advanced analysis to understand patterns in movie data.

## Dataset

* **Source:** IMDB Movie Metadata Dataset
* **File:** movie_metadata.csv
* **Description:**
  The dataset contains information about movies including budget, gross earnings, director name, genre, language, and other features. These attributes are used to predict the IMDB rating of movies.

## Steps Performed

### 1. Data Cleaning

* Handled missing values using forward fill method
* Removed irrelevant or inconsistent data
* Ensured dataset quality for analysis

### 2. Exploratory Data Analysis (EDA)

* Analyzed distributions of features such as IMDB score, budget, and gross
* Explored relationships between different variables
* Identified patterns and trends in movie data

### 3. Data Visualization

* Created bar plots, pie charts, and histograms
* Visualized top languages, directors, and score distributions
* Used visual insights to better understand the dataset

### 4. Feature Engineering

* Converted categorical variables into numerical format
* Selected important features for model training

### 5. Model Building

Applied multiple regression models:

* Linear Regression (baseline model)
* Random Forest Regressor
* Gradient Boosting Regressor

### 6. Model Evaluation

Models were evaluated using:

* Mean Absolute Error (MAE)
* Root Mean Squared Error (RMSE)
* R² Score

### 7. Hyperparameter Tuning

* Used GridSearchCV to optimize Random Forest parameters
* Improved model performance through tuning

### 8. Feature Importance

* Identified important features influencing movie ratings
* Analyzed contribution of variables such as budget and gross earnings

## Results

* Gradient Boosting and Random Forest performed better than Linear Regression
* Non-linear models captured complex relationships in the data
* Key factors such as budget, gross, and popularity significantly affect ratings

## Tools and Technologies Used

* Python
* NumPy
* Pandas
* Matplotlib / Seaborn
* Scikit-learn

## Key Insights

* Budget and gross earnings strongly influence movie ratings
* Popular directors and actors contribute to higher ratings
* Certain genres consistently perform better
* Data-driven analysis helps understand audience preferences

## Conclusion

This project demonstrates the use of advanced machine learning techniques for predicting movie ratings. Ensemble models such as Random Forest and Gradient Boosting provide better performance compared to basic models. The insights gained from this analysis can help in making informed decisions in the entertainment industry.

## Future Improvements

* Use more advanced models like XGBoost or Neural Networks
* Perform deeper feature engineering
* Deploy the model as a web application

## Project Structure

Advanced_Project/
│
├── imdb_movie_ratings_prediction.ipynb
├── movie_metadata.csv
├── README.md
