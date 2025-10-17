import reflex as rx
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

config = rx.Config(
    app_name="jbank",
    frontend_port=3000,
    backend_port=8000,
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ]
)