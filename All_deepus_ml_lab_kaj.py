import scipy.stats as stats
import math

# Question No. 1
'''The number of customer returns in a retail chain per day follows a Poisson distribution at a rate of
25 returns per day. Write Python code to answer the following questions:
(a) Calculate the probability that the number of returns exceeds 30 in a day.
(b) If the chance of fraudulent return is 0.05, calculate the probability that there will be at least 2
fraudulent returns in any given day. '''
lambda_returns = 25
# Question No. 1 (a) => Answer
prob_exceeds_30 = 1 - stats.poisson.cdf(30,lambda_returns)
print(f"Probablity that the number of returnsbexceeds 30 in a day: {prob_exceeds_30:.4f}")

# Question No. 1 (b) => Answer
prob_fraudulent = 0.05
lambda_frudulent_returns = lambda_returns*prob_fraudulent
prob_at_least_2_frudulent = 1 - stats.poisson.cdf(1, lambda_frudulent_returns)
print(f"Probablity that there will be at least 2 fraudulent returns in any given day: {prob_at_least_2_frudulent:.4f}")

# Question No. 2 
'''. A student is applying for Masters course in 8 US Universities and believes that she has in each of
the eight universities a constant and independent 0.42 probability of getting selected. Write code to
answer the following questions:
(a) What is the probability that she will get call from at least 3 universities?
(b) What is the probability that she will get calls from exactly 4 universities?'''
p = 0.42
n = 8
# Question No. 2 (a) => Answer
prob_at_least_3 = 1 - stats.binom.cdf(2, n, p)
print(f"Probablity that She will get a call from at least 3 Universities: {prob_at_least_3:.4f}")

# Question No. 2 (b) => Answer
prob_exactly_4 = stats.binom.pmf(4, n, p)
print(f"Probablity that She will get calls from exactly 4 Universities: {prob_exactly_4:.4f}")

# Question No. 3
'''The time-of-failure of a machine follows exponential distribution with mean time between failures
(MTBF) estimated to be 85 hrs. Write code to answer the following questions:
(a) Calculate the probability that the system will fail before 85 hrs.
(b) Calculate the probability that it will not fail up to 150 hrs.'''
mtbf = 85

# Question No. 3 (a) => Answer
prob_fail_before_85 = stats.expon.cdf(85, scale = mtbf)
print(f"Probablity that the system will fail before 85 hrs: {prob_fail_before_85:.4f}")

# Question No. 3 (b) => Answer
prob_not_fail_up_to_150 = 1 - stats.expon.cdf(150, scale = mtbf)
print(f"Probablity that the system will not fail up to 150 hrs: {prob_not_fail_up_to_150:.4f}")

# Question No. 4
'''As per a survey on use of pesticides among 1000 farmers in grape farming for around 10 acres of
grape farmland, it was found that the grape farmers spray 38 liters of pesticides in a week on an average with the corresponding standard deviation of 5 liters. Assume that the pesticide spray per week
follows a normal distribution. Write code to answer the following questions:
(a) What proportion of the farmers is spraying more than 50 liters of pesticide in a week?
(b) What proportion of farmers is spraying less than 10 liters?
(c) What proportion of farmers is spraying between 30 liters and 60 liters?'''
mean_pesticide = 38
std_dev_pesticide = 5
# Question No. 4 (a) => Answer
prob_more_than_50 = 1 - stats.norm.cdf(50, mean_pesticide , std_dev_pesticide)
print(f"Probablity of farmers spraying more than 50 liters: {prob_more_than_50:.4f}")

# Question No. 4 (b) => Answer
prob_less_than_10 = stats.norm.cdf(10, mean_pesticide , std_dev_pesticide)
print(f"Probablity of farmers spraying less than 10 liters: {prob_less_than_10:.4f}")

# Question No. 4 (c) => Answer
prob_between_30_60 = stats.norm.cdf(60, mean_pesticide , std_dev_pesticide) - stats.norm.cdf(30, mean_pesticide , std_dev_pesticide)
print(f"Probablity of farmers spraying between 30 to 60 liters: {prob_between_30_60:.4f}")

# Question No. 5
'''A bottle filling machine fills water into 5 liters (5000 cm3
) bottles. The company wants to test the null
hypothesis that the average amount of water filled by the machine into the bottle is at least 5000 cm3
.
A random sample of 60 bottles coming out of the machine was selected and the exact contents of the
selected bottles are recorded. The sample mean was 4,998.1 cm3
. The population standard deviation is
known from the experience to be 1.30 cm3
. Assume that the population is normally distributed with
the standard deviation of 1.30 cm3
. Write code to test the hypothesis at a of 5%. Explain the results.'''
sample_mean = 4998.1
hypothesized_mean = 5000
population_std_dev = 1.3
n = 60
alpha = 0.05

z = (sample_mean - hypothesized_mean) / (population_std_dev / math.sqrt(n))

p_value = stats.norm.cdf(z)

z_critical = stats.norm.ppf(alpha)

print(f"Z-test Statistic: {z:.4f}")
print(f"P-Value : {p_value:.4f}")
print(f"Critical Z-Value: {z_critical:.4f}")

if z < z_critical:
    print("Reject the null hypothesis: The avarage amount of the water filled is less than 5000cm3.")
else:
    print("Fail to reject the null hypothesis: The avarage amount of the water filled is at least 5000cm3.")

# Question No. 6
'''A fabric manufacturer would like to understand the proportion of defective fabrics they produce.
His shop floor staff have been stating that the percentage of defective is not more than 18%. He
would like to test whether the claim made by his shop floor staff is correct. He picked up a random
sample of 100 fabrics and found 22 defectives. Use a = 0.05 and write code to test the hypothesis that
the percentage of defective components is less than 18%.'''
n_2 = 100
x = 22
sample_proportion = x / n
hypothesized_proportion = 0.18
alpha_2 = 0.05

standerd_error = math.sqrt((hypothesized_proportion * (1 - hypothesized_proportion)) / n_2)
z_2 = (sample_proportion - hypothesized_proportion) / standerd_error

p_value_2 = stats.norm.cdf(z_2)

z_critical_2 = stats.norm.ppf(alpha_2)

print(f"Z-test Statistic: {z_2:.4f}")
print(f"P-Value : {p_value_2:.4f}")
print(f"Critical Z-Value: {z_critical_2:.4f}")

if z_2 < z_critical_2:
    print("Reject the null hypothesis: The Percentage of defective fabbrics is less than 18%.")
else:
    print("Fail to reject the null hypothesis: The Percentage of defective fabbrics is not less than 18%.")
    
# Question No. 7
'''Suppose that the makers of ABC batteries want to demonstrate that their battery lasts an average of
at least 60 min longer than their competitor brand. Two independent random samples of 100 batteries of each kind are selected from both the brands, and the batteries are used continuously. The
sample average life of ABC is found to be 450 min. The average life of competitor batteries is 368 min
with the sample standard deviation of 82 min and 78 min, respectively. Frame a hypothesis and write
the code to test ABC’s claim at 95% significance.''' 
n_ABC = 100
n_Competitor = 100
mean_ABC = 450
mean_Competitor = 368
std_ABC = 82
std_Competitor = 78
alpha = 0.05
delta_0 = 60

# Calculate the test statistic
pooled_se = math.sqrt((std_ABC**2 / n_ABC) + (std_Competitor**2 / n_Competitor))
t_statistic = ((mean_ABC - mean_Competitor) - delta_0) / pooled_se

# Calculate the degrees of freedom
df_numerator = ((std_ABC**2 / n_ABC) + (std_Competitor**2 / n_Competitor))**2
df_denominator = ((std_ABC**2 / n_ABC)**2 / (n_ABC - 1)) + ((std_Competitor**2 / n_Competitor)**2 / (n_Competitor - 1))
degrees_of_freedom = df_numerator / df_denominator

# Calculate the critical t-value for one-tailed test
t_critical = stats.t.ppf(1 - alpha, degrees_of_freedom)

# Calculate the p-value for the t-test
p_value_3 = 1 - stats.t.cdf(t_statistic, degrees_of_freedom)

print(f"T-test statistic: {t_statistic:.4f}")
print(f"Degrees of freedom: {degrees_of_freedom:.4f}")
print(f"Critical t-value: {t_critical:.4f}")
print(f"P-value: {p_value_3:.4f}")

# Decision
if t_statistic > t_critical:
    print("Reject the null hypothesis: ABC batteries last at least 60 minutes longer than the competitor's batteries.")
else:
    print("Fail to reject the null hypothesis: ABC batteries do not last at least 60 minutes longer than the competitor's batteries.")

# Question No. 8
'''A training institute would like to check the effectiveness of their training programs and if the scores
of the people trained improve post the training. A sample of 30 students was taken and their scores
were calculated before and after the training. File trainingscores.csv contains scores of the students
before and afterthe training. Frame and write the code to test the hypothesis of training effectiveness
for the training institute.'''
'''
import pandas as pd
file_path = 'trainingscores.csv'
data = pd.read_csv(file_path)

data['Difference'] = data['After'] - data['Before']

t_statistic,p_value = stats.ttest_rel(data['After'],data['Before'], alternative = 'greater')

alpha = 0.05

print(f"The T-test statistic: {t_statistic:.4f}")
print(f"P-Value: {p_value:.4f}")

if p_value < alpha:
    print("Reject the null hypothesis: The training program is effective and improve scores.")
else:
    print("Fail to Reject the null hypothesis: The training program does not significantly improve scores.")
'''