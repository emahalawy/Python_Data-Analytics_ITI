import requests
import pandas as pd
import json


def fetch_users():
    """Fetch users from DummyJSON API and return a cleaned DataFrame."""

    url = "https://dummyjson.com/users?limit=100"
    print("Fetching data from API")

    response = requests.get(url)

    if response.status_code != 200:
        raise Exception(f"API Error: {response.status_code}")

    data = response.json()
    df = pd.json_normalize(data["users"])
    print(f"Loaded {len(df)} users | {df.shape[1]} columns")

    #Extract nested fields 
    df["country"] = df.get("address.country", pd.Series(dtype=str))
    df["city"]    = df.get("address.city",    pd.Series(dtype=str))

    if "country" not in df.columns or df["country"].isnull().all():
        df["country"] = df["address"].apply(
            lambda x: x.get("country") if isinstance(x, dict) else None
        )
    if "city" not in df.columns or df["city"].isnull().all():
        df["city"] = df["address"].apply(
            lambda x: x.get("city") if isinstance(x, dict) else None
        )

    # Fill missing numeric values 
    for col in ["age", "height", "weight"]:
        if col in df.columns:
            n_missing = df[col].isnull().sum()
            if n_missing:
                df[col].fillna(df[col].median(), inplace=True)
                print(f" Filled {n_missing} missing values in '{col}' with median")

    # Save to CSV 
    df.to_csv("users.csv", index=False)
    print("Data saved to users.csv")

    return df


if __name__ == "__main__":
    df = fetch_users()
    print("\nPreview:")
    print(df[["firstName", "lastName", "age", "gender",
              "height", "weight", "city", "country"]].head(5))