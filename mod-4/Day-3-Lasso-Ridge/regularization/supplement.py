def model_experiment(num_iter=5,
                     models=['ols', 'ridge', 'lasso'], alpha=10,
                     complexity='simple', degree=3):
    """
    parameters:
    _________________________
    num_iter: int, number of times fit the models to the test data.
    note that for each iteration we split the data random train and test parts.
    models: list, list of models that we want to use. Options are 'ols' for simple linear regression
    'ridge' for ridge regression and 'lasso' for lasso regression.
    alpha: float, alpha parameter for ridge and lasso algorithms. Recall that higher values of alpha
    leads to more regularization.
    complexity: str, either 'simple' or 'polynomial'. We either use the original dataset or
    a dataset with polynomial powers generated.
    degree: int, if complexity is polynomial then degree is the degrees of polynomials to be generated.
    return: dict, it returns a dictionary with trained models as values and the 'complexity' parameters as keys.
    """

    x_axis = np.arange(num_iter)
    y_ols_test = []
    y_lasso_test = []
    y_ridge_test = []
    sample_models = {}
    for i in range(num_iter):

        if complexity == 'simple':
            ## split train_test
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
        elif complexity == 'polynomial':
            ## Create higher order terms
            poly = PolynomialFeatures(degree=degree)
            Xp = poly.fit_transform(X)
            ## test-train split
            X_train, X_test, y_train, y_test = train_test_split(Xp, y, test_size=0.2)

        ## Standard scale mean = 0, variance = 1
        sd = StandardScaler()

        sd.fit(X_train)

        X_train = sd.transform(X_train)

        X_test = sd.transform(X_test)

        ## Be careful about the leakage

        ## Vanilla model
        if 'ols' in models:
            lr = LinearRegression()

            lr.fit(X_train, y_train)

            sample_models['ols'] = lr

            test_score = lr.score(X_test, y_test)
            train_score = lr.score(X_train, y_train)

            y_ols_test.append(test_score)

        #       print('test score OLS is %.2f and train score is %.2f'%(test_score, train_score))

        if 'ridge' in models:
            ## Ridge in the simple setting
            ridge = Ridge(alpha=alpha, max_iter=10000)
            ridge.fit(X_train, y_train)
            sample_models['ridge'] = ridge
            y_ridge_test.append(ridge.score(X_test, y_test))
        #         print('test score Ridge is %.2f and train score is %.2f'%(ridge.score(X_test, y_test),
        #                                                             ridge.score(X_train, y_train)))

        if 'lasso' in models:
            ## Lasso in the simple setting
            lasso = Lasso(alpha=alpha, max_iter=10000)

            lasso.fit(X_train, y_train)

            sample_models['lasso'] = lasso

            y_lasso_test.append(lasso.score(X_test, y_test))
        #       print('test score Lasso is %.2f and train score is %.2f'%(lasso.score(X_test, y_test),
        #                                                             lasso.score(X_train, y_train)))

        i += 1
    if 'ols' in models:
        plt.plot(y_ols_test, label='ols')
    if 'ridge' in models:
        plt.plot(y_ridge_test, label='ridge')
    if 'lasso' in models:
        plt.plot(y_lasso_test, label='lasso')
    plt.ylabel('R2 test score')
    plt.xlabel('number of iterations')
    plt.ylim((0.50, 0.99))

    plt.legend()
    return sample_models