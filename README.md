Regularization:

There are classes in sklearn that help us perform regularization with our linear regression. 

The csv file has data including six predictor variables and one outcome variable. We have used sklearn's Lasso class to fit a linear regression model to the data, while also using L1 regularization to control for model complexity.

Performed following steps:
1. Splitted the data so that the six predictor features (first six columns) are stored in X, and the outcome feature (last column) is stored in y.
2. Fitted data using linear regression with Lasso regularization.
Created an instance of sklearn's Lasso class and assigned it to the variable lasso_reg. Used the Lasso object's .fit() method to fit the regression model onto the data.
3. Obtained the coefficients of the fit regression model using the .coef_ attribute of the Lasso object. Stored this in the reg_coef variable.