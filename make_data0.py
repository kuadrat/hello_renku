import numpy as np
import pandas as pd

y = np.random.rand(100)

df = pd.DataFrame(dict(y=y))
df.to_csv("data/data1.csv")
print("Goodby World!")