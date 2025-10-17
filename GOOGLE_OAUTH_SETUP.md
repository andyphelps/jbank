# Google OAuth Setup Instructions
## Error: "no registered origin"
This error means the URL you're accessing the app from is not authorized in Google Cloud Console.
## Fix: Add Authorized Origins
1. Go to: https://console.cloud.google.com/apis/credentials
2. Click on your OAuth 2.0 Client ID (the one with the ID: 713177573993-c260ujfr9sqbonid4el8gtk9rd26a91f)
3. Under "Authorized JavaScript origins", add these URLs:
   - `http://localhost:3000`
   - `http://localhost`
   - `http://127.0.0.1:3000`
4. Under "Authorized redirect URIs", make sure you have:
   - `http://localhost:3000/oauth/google/callback`
5. Click "SAVE"
## After Saving
1. Restart your Reflex app:
   ```bash
   reflex run
   ```
2. Access the app at: http://localhost:3000
3. Click the Google login button
It may take a few minutes for Google's changes to propagate, so if it doesn't work immediately, wait 1-2 minutes and try again.
