# Predicting prices presents a regression challenge within the realm of machine learning. 
# For the model fitting, We've opted for the Linear Regression model due to the observable moderate to strong associations between certain features and the target variable. 
# As for the alternative model, we've selected the Decision Tree regression model, primarily for its easy interpretability independent of outliers.
# For the model evaluation, we will use both R squared and RMSE (Root Mean Squared Error) to gauge the model's performance. 
# R squared assesses how effectively the model uses the features to model the dependent variables.
# On the other hand, RMSE quantifies the extent to which the predicted outcomes differ from the actual values.

# Prepare data to fit the model
# Normalize the numeric features
df['log_price'] = np.log(df['price'])

# Convert the categorical variables into numeric features
labelencoder = LabelEncoder()
df['model'] = labelencoder.fit_transform(df['model'])
df['transmission'] = labelencoder.fit_transform(df['transmission'])
df['fuelType'] = labelencoder.fit_transform(df['fuelType'])

# columns_to_encode = ['model', 'transmission', 'fuelType']
# df[columns_to_encode] = df[columns_to_encode].apply(lambda col: labelencoder.fit_transform(col))

# Split the data into a training set and a test set
features = ['year','transmission','fuelType','engineSize','tax','model','mileage']
X = df[features] 
y = df['log_price'] 

# Define the scaler 
scaler = PowerTransformer()
# Fit and transform the training set
X[['mileage']] = scaler.fit_transform(X[['mileage']])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=99)

# Build the linear regression
lr = LinearRegression()
lr.fit(X_train, y_train)

# Make the predictions
y_pred = lr.predict(X_test)

print('Linear Regression r2_score: ', r2_score(y_test,y_pred))
print('Linear Regression Root Mean Squared Error: ', np.sqrt(mean_squared_error(np.exp(y_test),np.exp(y_pred))))

