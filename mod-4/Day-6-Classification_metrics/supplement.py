col = [c for c in df.columns if c not in ['target']]
numclasses=[]
for c in col:
    numclasses.append(len(np.unique(df[[c]])))

threshold=10
categorical_variables = list(np.array(col)[np.array(numclasses)<threshold])

enc = OneHotEncoder( handle_unknown= 'ignore')
remaining_list = [i for i in df.columns.tolist() if i not in categorical_variables]
remaining_list.remove('target')
X_num = X_train[remaining_list].values

X_Cat = enc.fit_transform(X_train[categorical_variables]).toarray()
X = np.concatenate((X_num, X_Cat), axis = 1)

lr = LogisticRegression(C = 1e9, solver = 'lbfgs', max_iter=10000)
lr.fit(X, y_train)

cv = StratifiedKFold(n_splits= 5, random_state=1019, shuffle=True)

lr_vanilla = LogisticRegression(C = 1e9,
                                solver = 'newton-cg',
                                max_iter=1000)

l2_reg = LogisticRegression(C = 1,
                            solver = 'newton-cg',
                            max_iter=1000)

l1_reg = LogisticRegression(C = 1,
                           solver= 'saga',
                           penalty = 'l1',
                            max_iter=1000)

cv_vanilla = cross_validate(estimator=lr_vanilla,
                            X = X, y = y_train,
                            cv = cv,
                            n_jobs=-1,
                            return_estimator= True,
                            return_train_score=True)

cv_l2 = cross_validate(estimator=l2_reg, X = X, y = y_train,
                    cv = cv,
                    n_jobs=-1,
                    return_estimator= True,
                    return_train_score=True)

cv_l1 = cross_validate(estimator=l1_reg, X = X, y = y_train,
                    cv = cv,
                    n_jobs=-1,
                    return_estimator= True,
                    return_train_score=True)


## create an encoder object. This will help us to convert
## categorical variables to new columns
encoder = OneHotEncoder(handle_unknown= 'error',
                        drop='first',
                        categories= 'auto')

## Create an columntransformer object.
## This will help us to merge transformed columns
## with the rest of the dataset.

ct = ColumnTransformer(transformers =[('ohe', encoder, categorical_variables)],
                                    remainder= 'passthrough')
ct.fit(X_train)
X = ct.transform(X_train)


Xtest  = ct.transform(X_test)
Xtest.shape