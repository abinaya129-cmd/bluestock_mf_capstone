import requests
import pandas as pd
from pathlib import Path

# Create output folder if not exists
output_dir = Path("../data/raw")
output_dir.mkdir(exist_ok=True)

schemes = {
    "HDFC_Top100": 125497,
    "SBI_Bluechip": 119551,
    "ICICI_Bluechip": 120503,
    "Nippon_LargeCap": 118632,
    "Axis_Bluechip": 119092,
    "Kotak_Bluechip": 120841
}

for scheme_name, code in schemes.items():

    print(f"\nFetching {scheme_name} ({code})...")

    url = f"https://api.mfapi.in/mf/{code}"

    response = requests.get(url)

    if response.status_code == 200:

        data = response.json()

        nav_df = pd.DataFrame(data["data"])

        filename = output_dir / f"{scheme_name}.csv"

        nav_df.to_csv(filename, index=False)

        print(f"Saved: {filename}")

    else:
        print(f"Failed for {scheme_name}")