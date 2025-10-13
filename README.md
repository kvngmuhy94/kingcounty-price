
# 🏡 Project Title:
# Advanced House Price Prediction Using Machine Learning


# 🎯 Objective: 
To develop and evaluate multiple machine learning models that accurately predict house prices based on key features such as size, location, number of rooms, and construction year.

# 📁 Dataset  

Utilize the *King County House Sales dataset* o(sourced from Kaggle), which includes:

*size:* 4600 rows × 18 columns 

*location:* King County, USA

*Target:* Price

*Key Features:*

- `price` *(target variable)*  
- `Date`
- `bedrooms`  
- `bathrooms`  
- `sqft_living`  
- `sqft_lot`  
- `floors`  
- `waterfront`  
- `view`  
- `condition`  
- `sqft_above`  
- `sqft_basement`  
- `yr_built`  
- `yr_renovated`  
- `street`
- `city`
- `zipcode`
- `country`

The dataset includes both numerical and categorical variables useful for regression modeling.  


# 🔧 Project Workflow:

1. Data Cleaning & Preprocessing  
   - Handle missing values  
   - Encode categorical variables 
   - Feature engineering (house_age)
   - Normalize features   

2. Exploratory Data Analysis (EDA)
   - Correlation matrix  
   - Price distribution  

3. Model Training

    Train and compare the following models: 
   - Linear Regression  
   - Ridge Regression
   - Lasso Regression
   - ElasticNet  Regression 
   - Decision Tree Regressor  
   - Random Forest Regressor  
   - Gradient Boosting Regressor  
   - Support Vector Regressor  
   - K-Nearest Neighbors Regressor  

4. Evaluation Metrics
  
   Used the following metrics to access model        performance: 
   - MAE (Mean Absolute Error)  
   - MSE (Mean Squared Error)  
   - RMSE (Root Mean Squared Error)  
   - R² Score  

5. Model Comparison 
   - Visual and tabular Comparison of model score
   - Discussed strengths and weaknesses of each model 

6. Model Optimization
   - Hyperparameter using RandomizedSearchCV
   - 10-fold cross-validation 

7. Deployment
   - Deployed the best performing model using Streamlit 
   - created a user-friendly web interface for real time house Price Prediction 


🚀 *Live Demo*  
Check out the deployed Streamlit app 👉 [King County House Price Prediction App](https://isaac5886-kingcounty-price-app1-mxqgaq.streamlit.app/)
