from flask import Flask, render_template

from app.analytics import (
    calculate_cost_by_service,
    calculate_total_cost,
    create_cost_chart,
    load_cost_data,
)


def register_routes(app: Flask) -> None:
    """Register application routes."""

    @app.get("/")
    def dashboard():
        dataframe = load_cost_data("data/cloud_cost.csv")

        total_cost = calculate_total_cost(dataframe)
        service_cost = calculate_cost_by_service(dataframe)

        create_cost_chart(
            service_cost,
            "static/charts/cost_chart.png",
        )

        return render_template(
            "index.html",
            total_cost=total_cost,
        )
