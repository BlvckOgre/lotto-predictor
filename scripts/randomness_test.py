
import pandas as pd
import numpy as np
from scipy.stats import chisquare

df = pd.read_csv('data/clean_historical_draws.csv')
numbers = df.iloc[:, 1:7].values.flatten()
counts = np.bincount(numbers, minlength=53)[1:]

expected = [np.mean(counts)] * 52
chi2, p = chisquare(counts, f_exp=expected)

print(f"Chi-square test statistic: {chi2:.2f}, p-value: {p:.4f}")
