import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def generate_gaussian_simpsons_paradox(n_subgroups=3, n_samples=1000):

    overall_cov = 3*np.array([[1,0.9], [0.9,1]])

    means = np.random.multivariate_normal(mean=[0,0], cov=overall_cov, size=n_subgroups)
    
    weights = np.random.uniform(size=n_subgroups)
    weights /= np.sum(weights)
    covs = [np.random.uniform(0.2,0.8) for _ in range(n_subgroups)]
    covs = [np.array([[1,-c], [-c,1]]) for c in covs]


    samples = []

    for sg, (mean, cov, w) in enumerate(zip(means, covs, weights)):
        n = int(round(n_samples * w))
        sample = np.random.multivariate_normal(mean=mean, cov=cov, size=n)
        sample = pd.DataFrame(sample, columns=["x", "y"])
        sample["z"] = sg
        samples.append(sample)
        
    df = pd.concat(samples)
    
    return df



df = generate_gaussian_simpsons_paradox(2,30)
SPORT = "Heures de pratique de sport par semaine"
MOYENNE = "Moyenne en classe"
df[SPORT] = df["x"] + 10
df[MOYENNE] = df["y"] + 10
df.plot.scatter(x=SPORT, y = MOYENNE, grid=True, legend=True)
plt.show()
df.plot.scatter(x=SPORT, y=MOYENNE, c="z", colormap="viridis", grid = True)
plt.show()

print(df)