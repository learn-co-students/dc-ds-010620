## Instantiate the PolynomialFeatures object with degree=3
poly = PolynomialFeatures(degree =7)

## Now transform data to create higher order features
X7 = poly.fit_transform(x.reshape(-1,1))


## fitting a linear model
lr = LinearRegression(fit_intercept= False)

x = x.reshape(-1,1)
lr.fit(X7,y)

y_pred = lr.predict(X7)

## plotting the results
plt.scatter(x,y, label = 'Training Data')
plt.scatter(x,y_pred, label ='lr with degree 7')

plt.legend()

plt.show()


## function returns the dataset of a given polynomial degree
def create_dataset(x, degree):
    ## Instantiate the PolynomialFeatures object with given 'degree'
    poly = PolynomialFeatures(degree=degree)

    ## Now transform data to create higher order features
    new_data = poly.fit_transform(x.reshape(-1, 1))
    return new_data


Note that true (population) parameters were:

$$ \beta_{0} = 1, \quad \beta_{1} = 0, \quad \beta_{2} = 0.4, \quad \beta_{3} = - 0.23 $$


plt.scatter(x,y)
plt.scatter(x, y_pred)
plt.ylabel('$\sin(x)$')

plt.xlabel('x values are randomly chosen from $[-2\pi, 2\pi]$')

plt.show()