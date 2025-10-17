# JBank - Joint Banking Application

A banking application built with Reflex and Google OAuth authentication.

## Setup Instructions

### 1. Install Dependencies

```bash
make sync
```

### 2. Configure Google OAuth

To enable Google authentication, you need to set up OAuth credentials:

1. Go to [Google Cloud Console](https://console.cloud.google.com/apis/credentials)
2. Create a new project (or select an existing one)
3. Enable the Google+ API or Google Identity Services
4. Go to "Credentials" → "Create Credentials" → "OAuth 2.0 Client ID"
5. Configure the OAuth consent screen if prompted
6. Select "Web application" as the application type
7. Add authorized redirect URI: `http://localhost:3000/oauth/google/callback`
8. Copy the Client ID and Client Secret

### 3. Update Environment Variables

Edit the `.env` file and replace the placeholders:

```bash
GOOGLE_CLIENT_ID=your_actual_client_id.apps.googleusercontent.com
GOOGLE_CLIENT_SECRET=your_actual_client_secret
```

### 4. Run the Application

```bash
make run
```

The app will start at `http://localhost:3000`

## Features

- ✅ Google OAuth authentication
- ✅ Protected dashboard page
- ✅ User profile display
- ✅ Banking dashboard UI with:
  - Account balance overview
  - Quick actions
  - Recent activity section
  - Logout functionality

## Project Structure

- `jbank/jbank.py` - Main application with login and dashboard pages
- `rxconfig.py` - Reflex configuration
- `.env` - Environment variables (Google OAuth credentials)

## Available Commands

- `make sync` - Install/sync dependencies
- `make run` - Run the development server
- `make test` - Run tests
- `make lint` - Run linters
- `make format` - Format code
- `make build` - Build the project

## Next Steps

After setting up OAuth credentials and running the app:

1. Visit `http://localhost:3000`
2. Click "Sign in with Google"
3. Authenticate with your Google account
4. You'll be redirected to the dashboard at `/dashboard`

## Security Notes

- Never commit the `.env` file to version control
- Keep your Google OAuth credentials secure
- For production, update the authorized redirect URI to your production domain

