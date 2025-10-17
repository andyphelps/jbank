import reflex as rx
from reflex_google_auth import GoogleAuthState

class AuthState(GoogleAuthState):
    @rx.var
    def login_url(self) -> str:
        # Assuming the plugin sets up the route at /auth/google/login or similar
        return "/auth/google/login"

def index():
    return rx.center(
        rx.vstack(
            rx.cond(
                AuthState.is_authenticated,
                rx.vstack(
                    rx.heading(f"Welcome to JBank, {AuthState.user['name']}!", size="xl"),
                    rx.text("You are logged in."),
                    # Add more content here for the main app
                    spacing="4",
                    align="center",
                ),
                rx.vstack(
                    rx.heading("Welcome to JBank", size="xl"),
                    rx.text("Joint Bank Tracking Application"),
                    rx.text("Please log in with your Google account to continue."),
                    rx.button(
                        "Login with Google",
                        size="lg",
                        on_click=rx.redirect(AuthState.login_url()),
                    ),
                    spacing="4",
                    align="center",
                ),
            ),
            spacing="4",
            align="center",
        ),
        height="100vh",
    )

app = rx.App()
app.add_page(index, route="/", title="JBank - Login")
