import pandas as pd

from app.analytics import (
    calculate_cost_by_environment,
    calculate_cost_by_service,
    calculate_total_cost,
)


def test_calculate_total_cost():
    dataframe = pd.DataFrame(
        {
            "service": ["EC2", "S3"],
            "environment": ["Production", "Development"],
            "cost": [100.0, 50.0],
        }
    )

    assert calculate_total_cost(dataframe) == 150.0


def test_calculate_cost_by_service():
    dataframe = pd.DataFrame(
        {
            "service": ["EC2", "EC2", "S3"],
            "environment": ["Production", "Development", "Production"],
            "cost": [100.0, 50.0, 25.0],
        }
    )

    result = calculate_cost_by_service(dataframe)

    assert result.iloc[0]["service"] == "EC2"
    assert result.iloc[0]["cost"] == 150.0


def test_calculate_cost_by_environment():
    dataframe = pd.DataFrame(
        {
            "service": ["EC2", "S3", "RDS"],
            "environment": ["Production", "Production", "Development"],
            "cost": [100.0, 50.0, 25.0],
        }
    )

    result = calculate_cost_by_environment(dataframe)

    assert result.iloc[0]["environment"] == "Production"
    assert result.iloc[0]["cost"] == 150.0
