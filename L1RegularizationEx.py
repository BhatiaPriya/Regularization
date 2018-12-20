# -*- coding: utf-8 -*-
"""
Created on Thu Dec 20 12:23:07 2018

@author: abhik
"""

# TODO: Add import statements
import pandas as pd

# Lasso (least absolute shrinkage and selection operator) is a 
# regression analysis method that performs both variable selection
# and regularization in order to enhance the prediction accuracy and
# interpretability of the statistical model it produces.

from sklearn.linear_model import Lasso

# Assign the data to predictor and outcome variables
# TODO: Load the data

train_data = pd.read_csv('L1_Regularization_ExampleData.csv', header = None)
X = train_data.iloc[:, :-1]
y = train_data.iloc[:,-1 ]

# TODO: Create the linear regression model with lasso regularization.
lasso_reg = Lasso()

# TODO: Fit the model.
lasso_reg.fit(X,y)

# TODO: Retrieve and print out the coefficients from the regression model.
reg_coef = lasso_reg.coef_
print(reg_coef)
