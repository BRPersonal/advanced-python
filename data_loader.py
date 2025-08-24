import polars as pl

print("loading data...")
url = "https://raw.githubusercontent.com/gakudo-ai/open-datasets/refs/heads/main/customers-100000.csv"
df = pl.read_csv(url)

print("querying data...")
lazy_result = df.lazy().filter(pl.col("Country") == "France").select("First Name", "Email").collect()

print(lazy_result)