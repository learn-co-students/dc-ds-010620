def estimate_alpha(sample):
    cov = np.cov(sample.T)
    num = cov[1, 1] - cov[0, 1]
    denom = cov[0, 0] + cov[1, 1] - 2 * cov[0, 1]
    alpha = num / denom
    return (alpha)


alpha_hats = []
for i in range(10000):
    s  = np.random.multivariate_normal(mean, covariant, size = 100)
    alpha_hats.append(estimate_alpha(s))

print(np.mean(alpha_hats))
print(np.std(alpha_hats, ddof = 1))

a = [alpha_hat(resample(sample,
                    replace = True,
                    n_samples = 100)) for i in range(10000)]

difference = []
for i in range(1000):
    bootstrapped = resample(X, replace = True, n_samples = 100)
    difference.append(len(set(X) - set(bootstrapped) ))
    