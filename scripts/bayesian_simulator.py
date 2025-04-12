
import numpy as np
import pandas as pd

df = pd.read_csv('data/clean_historical_draws.csv')
numbers = df.iloc[:, 1:7].values.flatten()

prior = np.ones(52)
frequency = np.bincount(numbers, minlength=53)[1:]
posterior = (frequency + prior) / (sum(frequency) + sum(prior))

simulated_draw = np.random.choice(np.arange(1, 53), p=posterior / posterior.sum(), size=6, replace=False)
print(f"Simulated likely draw: {sorted(simulated_draw)}")
