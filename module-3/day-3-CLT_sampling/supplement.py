sampled_data = auto.sample(n = 20, random_state=110719)

x_bar = sampled_data.mpg.mean()

mu = auto.mpg.mean()



# taking repeating samples from auto dataset
thousand_rand_samp = [auto.sample(n = 20).mpg.mean() for i in range(1000)]

bars = plt.hist(thousand_rand_samp)

plt.vlines(x = mu, ymin= 0,
           ymax = bars[0].max() +1,
           color = 'r', label = 'pop mean')
plt.xticks(range(17,29))
plt.xlabel('sample_means')
plt.ylabel('frequencies of sample means')

plt.legend()
plt.show()

x1_bar = sample.mpg.mean()

x2_bar = sample2.mpg.mean()

s1_bar = sample.mpg.std()

s2_bar = sample2.mpg.std()

auto = pd.read_csv('data/auto-mpg.csv')
mu = auto.mpg.mean()
sampled_data.mpg.std()
sigma = auto.mpg.std()