"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
from reflex_google_auth import GoogleAuthState, require_google_login, google_login, google_oauth_provider

from rxconfig import config


class State(rx.State):
    """The app state."""
    pass


def login_page() -> rx.Component:
    """Login page with Google authentication."""
    # Check if already logged in, redirect to dashboard
    return google_oauth_provider(
        rx.container(
            rx.color_mode.button(position="top-right"),
            rx.cond(
                GoogleAuthState.token_is_valid,
                rx.vstack(
                    rx.spinner(size="3"),
                    rx.text("Already logged in, redirecting..."),
                    on_mount=rx.redirect("/dashboard"),
                ),
                rx.vstack(
                    rx.heading("JBank", size="9", margin_bottom="1rem"),
                    rx.text(
                        "Welcome to JBank - Your Joint Banking Application",
                        size="5",
                        color_scheme="gray",
                        margin_bottom="2rem",
                    ),
                    rx.card(
                        rx.vstack(
                            rx.heading("Sign In", size="6", margin_bottom="1rem"),
                            rx.text(
                                "Please sign in with your Google account to access your banking dashboard.",
                                size="3",
                                color_scheme="gray",
                                margin_bottom="1.5rem",
                                text_align="center",
                            ),
                            google_login(),
                            spacing="4",
                            align="center",
                        ),
                        padding="2rem",
                        max_width="500px",
                    ),
                    spacing="5",
                    justify="center",
                    align="center",
                    min_height="85vh",
                ),
            ),
        )
    )


def index() -> rx.Component:
    """Index page that redirects based on auth status."""
    return google_oauth_provider(
        rx.cond(
            GoogleAuthState.token_is_valid,
            rx.center(
                rx.vstack(
                    rx.spinner(size="3"),
                    rx.text("Redirecting to dashboard..."),
                ),
                min_height="100vh",
            ),
        ),
        on_mount=rx.cond(
            GoogleAuthState.token_is_valid,
            rx.redirect("/dashboard"),
            rx.redirect("/login"),
        ),
    )


@require_google_login(
    button=rx.center(
        rx.vstack(
            rx.card(
                rx.vstack(
                    rx.heading("Authentication Required", size="6", margin_bottom="1rem"),
                    rx.text(
                        "Please sign in with your Google account to access the dashboard.",
                        size="3",
                        color_scheme="gray",
                        margin_bottom="1.5rem",
                        text_align="center",
                    ),
                    google_login(),
                    spacing="4",
                    align="center",
                ),
                padding="2rem",
                max_width="500px",
            ),
            spacing="5",
            justify="center",
            align="center",
            min_height="85vh",
        ),
    )
)
def dashboard() -> rx.Component:
    """Protected landing page/dashboard for the banking app."""
    return rx.container(
        rx.color_mode.button(position="top-right"),
        rx.vstack(
            # Header
            rx.hstack(
                rx.heading("JBank Dashboard", size="8"),
                rx.spacer(),
                rx.hstack(
                    rx.avatar(
                        src=GoogleAuthState.tokeninfo.get("picture", ""),
                        fallback=GoogleAuthState.tokeninfo.get("given_name", "U")[0],
                        size="3",
                    ),
                    rx.vstack(
                        rx.text(
                            GoogleAuthState.user_name,
                            size="3",
                            weight="bold",
                        ),
                        rx.text(
                            GoogleAuthState.user_email,
                            size="2",
                            color_scheme="gray",
                        ),
                        spacing="0",
                        align="start",
                    ),
                    rx.button(
                        "Logout",
                        on_click=[GoogleAuthState.logout, rx.redirect("/login")],
                        variant="soft",
                        color_scheme="red",
                    ),
                    spacing="3",
                    align="center",
                ),
                width="100%",
                padding_y="1rem",
                border_bottom="1px solid var(--gray-5)",
                margin_bottom="2rem",
            ),
            # Main Content
            rx.vstack(
                rx.heading("Welcome to Your Banking Dashboard", size="6", margin_bottom="1rem"),
                rx.text(
                    f"Hello {GoogleAuthState.tokeninfo.get('given_name', 'User')}! You've successfully logged in.",
                    size="4",
                    color_scheme="gray",
                    margin_bottom="2rem",
                ),
                # Account Overview Cards
                rx.grid(
                    rx.card(
                        rx.vstack(
                            rx.heading("Total Balance", size="4", color_scheme="gray"),
                            rx.heading("$0.00", size="8", color_scheme="green"),
                            rx.text("Across all accounts", size="2", color_scheme="gray"),
                            spacing="2",
                            align="start",
                        ),
                        padding="1.5rem",
                    ),
                    rx.card(
                        rx.vstack(
                            rx.heading("Checking", size="4", color_scheme="gray"),
                            rx.heading("$0.00", size="8"),
                            rx.text("Available balance", size="2", color_scheme="gray"),
                            spacing="2",
                            align="start",
                        ),
                        padding="1.5rem",
                    ),
                    rx.card(
                        rx.vstack(
                            rx.heading("Savings", size="4", color_scheme="gray"),
                            rx.heading("$0.00", size="8"),
                            rx.text("Available balance", size="2", color_scheme="gray"),
                            spacing="2",
                            align="start",
                        ),
                        padding="1.5rem",
                    ),
                    columns="3",
                    spacing="4",
                    width="100%",
                    margin_bottom="2rem",
                ),
                # Quick Actions
                rx.card(
                    rx.vstack(
                        rx.heading("Quick Actions", size="5", margin_bottom="1rem"),
                        rx.hstack(
                            rx.button("Transfer Money", size="3", variant="solid"),
                            rx.button("Pay Bills", size="3", variant="soft"),
                            rx.button("View Transactions", size="3", variant="soft"),
                            rx.button("Add Account", size="3", variant="outline"),
                            spacing="3",
                        ),
                        align="start",
                    ),
                    padding="1.5rem",
                    width="100%",
                    margin_bottom="2rem",
                ),
                # Recent Activity
                rx.card(
                    rx.vstack(
                        rx.heading("Recent Activity", size="5", margin_bottom="1rem"),
                        rx.text(
                            "No recent transactions",
                            size="3",
                            color_scheme="gray",
                            padding="2rem",
                            text_align="center",
                        ),
                        align="start",
                        width="100%",
                    ),
                    padding="1.5rem",
                    width="100%",
                ),
                spacing="4",
                width="100%",
            ),
            spacing="5",
            padding_y="2rem",
            max_width="1200px",
        ),
        padding_x="2rem",
    )


app = rx.App()
app.add_page(index, route="/", title="JBank")
app.add_page(login_page, route="/login", title="JBank - Login")
app.add_page(dashboard, route="/dashboard", title="JBank - Dashboard")
