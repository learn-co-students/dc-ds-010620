#population mean
mu = 500

# let's find the sample mean
x_bar = sample.mean()

# know let's find the standard error
# note that we don't know the population standard deviation
# so instead we will use sample standard deviation as an estimator

s = sample.std(ddof = 1)/np.sqrt(len(sample))

# know we will find a t-score by dividing the difference in means
# with standard error

t = (x_bar - mu)/s

# note that we know that t-score should lie on a t-distribution with
# degrees of freedom len(sample) - 1 as the parameter.
# let's use t method from scipy.stats

p_value = stats.t.sf(t, df = len(sample) -1)


## two sample t-test assuming same population variance
n1 = len(sample1)
n2 = len(sample2)

pooled_std = np.sqrt(((n1-1)*np.var(sample1, ddof =1) + (n2-1)*np.var(sample2, ddof = 1))/(n1+n2-2))

denom = pooled_std*np.sqrt(1/n1 + 1/n2)

num = sample1.mean() - sample2.mean()

t = num/denom

print("""t-value is %.7f"""%t)

## now we would use t-distribution with
## degrees of freedom equals to n1+n2-2
## to find the p_values of such t

## we are using two sided hypothesis testing
p_value = (stats.t.cdf(t,  df= n1+n2-2))*2

print("""p_value is %.7f"""%p_value)


n1 = len(sample1)
n2 = len(sample2)
var1 = np.var(sample1, ddof=1)
var2 = np.var(sample2, ddof =1)

num = (n1 -1 )*var1 + (n2-1)*var2

denom = (n1+n2 - 2)
s_W = np.sqrt(num/denom)

d = np.abs(sample1.mean() - sample2.mean())/s_W

print(d)

<img src="img/critical_value.png" alt="Cohen's d-table"
	title="Power of a test" width="650" />