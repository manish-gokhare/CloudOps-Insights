from pathlib import Path

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import pandas as pd


def load_cost_data(file_path: str) -> pd.DataFrame:
    """Load cloud cost data from a CSV file."""
    return pd.read_csv(Path(file_path))


def calculate_total_cost(dataframe: pd.DataFrame) -> float:
    """Calculate total cloud cost."""
    return float(dataframe["cost"].sum())


def calculate_cost_by_service(dataframe: pd.DataFrame) -> pd.DataFrame:
    """Calculate total cost for each cloud service."""
    return (
        dataframe.groupby("service", as_index=False)["cost"]
        .sum()
        .sort_values("cost", ascending=False)
    )


def calculate_cost_by_environment(dataframe: pd.DataFrame) -> pd.DataFrame:
    """Calculate total cost for each environment."""
    return (
        dataframe.groupby("environment", as_index=False)["cost"]
        .sum()
        .sort_values("cost", ascending=False)
    )


def create_cost_chart(dataframe: pd.DataFrame, output_path: str) -> None:
    """Create a bar chart showing cost by service."""
    output_file = Path(output_path)
    output_file.parent.mkdir(parents=True, exist_ok=True)

    plt.figure(figsize=(10, 6))
    plt.bar(dataframe["service"], dataframe["cost"])

    plt.title("Cloud Cost by Service")
    plt.xlabel("Cloud Service")
    plt.ylabel("Cost ($)")

    plt.tight_layout()
    plt.savefig(output_file)
    plt.close()
