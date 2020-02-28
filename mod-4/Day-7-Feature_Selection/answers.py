X_passengers = df.Passengers.values
y = df.MPG_Highway
X_passengers = sm.add_constant(X_passengers)
model = sm.OLS(y, X_passengers, hasconst=True)
result = model.fit()
result.summary()

## Multiple linear regression

X = df.drop(columns='MPG_Highway').values

y = df.MPG_Highway

# Fitting the actual model
X = sm.add_constant(X)
model = sm.OLS(y, X, hasconst=True )
result = model.fit()
labels = ['intercept'] + x_cols
print(labels)
result.summary(xname=labels)

### multilinear regression with more variables

X = df[cols_subset].values
X = sm.add_constant(X)
model = sm.OLS(y, X, hasconst=True, )
result = model.fit()
cols_subset = ['intercept'] + cols_subset
print(cols_subset)
result.summary(xname = cols_subset)


## Showing VIF is R2

## take the passenger as target
y_vif = df.Passengers
## remove Passenger from predictor list
refined_cols.remove('Passengers')
## prepare data for the linear model
X_vif = df[refined_cols]
## add intercept term
X_vif = sm.add_constant(X_vif.values)
## fit model
model_vif = sm.OLS(y_vif, X_vif, hasconst=True)
result_vif = model_vif.fit()
## check the r2-score
result_vif.summary()
## calculate vif score directly from r2-score
passenger_vif = 1/(1 - result_vif.rsquared)
passenger_vif

## Calculate Adjusted R2 from R2

R2_adj = 1- (1-R2)*(len(y)-1)/(len(y) - 3 - 1)
print(R2_adj)