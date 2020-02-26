x = 'area_mean'
sns.lmplot(x=x, y='Target', data=df, ci=None)
plt.ylim([-0.5, 1.5])
plt.xlim([df[x].min()- df[x].std(), df[x].max() + df[x].std()])
plt.show(


from sklearn.linear_model import LinearRegression
linreg = LinearRegression().fit(df.area_mean.values.reshape(-1, 1), df.Target)
# compute prediction for area_mean=350 using the predict method
linreg.predict(np.array([[5], [350]]))

df['Pred_class'] = df.Prediction.map(lambda x: 1 if x> 0.05 else 0 )

# fit a logistic regression model and store the class predictions
from sklearn.linear_model import LogisticRegression
logreg = LogisticRegression(C=1e9, solver='lbfgs')
feature_cols = ['area_mean']
X = df[feature_cols]
y = df.Target
logreg.fit(X, y)
df['Log_Prediction'] = logreg.predict(X)
df['Log_probabilities'] = logreg.predict_proba(X)[:,1]

(df.Pred_class != df.Log_Prediction).sum()