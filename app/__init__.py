from pathlib import Path

from flask import Flask


def create_app() -> Flask:
    """Create and configure the Flask application."""
    base_dir = Path(__file__).resolve().parent.parent

    app = Flask(
        __name__,
        template_folder=base_dir / "templates",
        static_folder=base_dir / "static",
    )

    from app.routes import register_routes
    register_routes(app)
    return app