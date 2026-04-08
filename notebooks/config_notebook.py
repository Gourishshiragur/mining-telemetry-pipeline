dbutils.widgets.text("env", "dev")
env = dbutils.widgets.get("env")

if env == "dev":
    base_path = "dbfs:/FileStore"
else:
    base_path = "abfss://mining@storageaccount.dfs.core.windows.net"

paths = {
    "raw": f"{base_path}/raw",
    "bronze": f"{base_path}/bronze",
    "silver": f"{base_path}/silver",
    "gold": f"{base_path}/gold"
}