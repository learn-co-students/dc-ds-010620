cv = cross_validate(rf,
                    X_train,
                    y_train,
                    return_train_score=True,
                    return_estimator=True,
                    cv=5)


mean_test = np.mean(validator['test_score'])
std_test = np.std(validator['test_score'])

mean_train = np.mean(validator['train_score'])
std_train = np.std(validator['train_score'])


print("Train score: %.3f +/- %.3f"%(mean_train, std_train))
print("Test score: %.3f +/- %.3f"%(mean_test, std_test))


clf = RandomForestClassifier(n_estimators= 100,
                             criterion= 'gini',
                             max_features= 'auto', max_depth= 2,
                             oob_score= True)

clf.fit(Xtrain, y_train);
clf.score(Xtrain, y_train)
clf.oob_score_