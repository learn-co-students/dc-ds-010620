def least_squares(X,y):
    x_bar = X.mean()
    y_bar = y.mean()
    b1_num = (X - x_bar).dot(y - y_bar)
    b1_denom = ((X - x_bar)**2).sum()
    b1 = b1_num /b1_denom
    b0 = y_bar - b1*x_bar
    RSS = ((y - (b0 + b1*X))**2).sum()
    return  b0,b1, RSS


# import LinearRegression class

from sklearn.linear_model import LinearRegression

# instantiate the class
# check parameters

lr = LinearRegression()

# now fit the data
# note that in sklearn this procedure is very standard
# but before we should reshape X
print('Shape of X before reshape:', X.shape)
X = X.reshape(-1,1)
print('Shape of X after reshape:', X.shape)
# when you fit model learns b0_hat and b1_hat
lr.fit(X,y)

# now we can use fitted object lr to get parameters or learn parameters

print(lr.intercept_, lr.coef_)


## your work is here
coef_list_b0 = []
coef_list_b1 = []
for i in range(100):
    X = np.random.uniform(low = 0, high = 10, size = 100)
    X = X.reshape(-1,1)
    irr_error = np.random.normal(loc= 0, scale = 1, size = 100)
    y = 3*X + 5 + irr_error.reshape(-1,1)
    lr = LinearRegression()
    lr.fit(X,y)
    b0_hat= lr.intercept_
    b1_hat = lr.coef_
    coef_list_b0.append(b0_hat[0])
    coef_list_b1.append(b1_hat[0,0])


X = sm.add_constant(X)
model = sm.OLS(y,X, hasconst=True)
results = model.fit()
results.summary()