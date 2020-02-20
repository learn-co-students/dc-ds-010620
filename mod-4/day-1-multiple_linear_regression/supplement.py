X = df[['TV', 'Radio', 'Newspaper']]
y = df.Sales
X = sm.add_constant(X)
mod = sm.OLS(y, X, hasconst= True)
res = mod.fit()
print(res.summary())


## compare the results with sklearn

from sklearn.linear_model import LinearRegression
features = ['TV', 'Newspaper', 'Radio']
lr = LinearRegression()

X = df[features]
y = df.Sales
lr.fit(df[features], df.Sales)
print(lr.intercept_, lr.coef_)

## compare also scores

lr.score(X,y)

from scipy.stats import stats
residuals = res.resid
plt.hist(residuals)

stats.normaltest(residuals)