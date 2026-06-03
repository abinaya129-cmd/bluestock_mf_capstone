import pandas as pd
import matplotlib.pyplot as plt

nav = pd.read_csv("../data/processed/clean_nav.csv")

sample = nav[
    nav["amfi_code"] ==
    nav["amfi_code"].iloc[0]
]

plt.figure(figsize=(10,5))

plt.plot(
    pd.to_datetime(sample["date"]),
    sample["nav"]
)

plt.title("NAV Trend")

plt.xlabel("Date")
plt.ylabel("NAV")

plt.show()