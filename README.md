# Vanta API Repo

This repository contains scripts for managing and building Vanta-related resources. The code is organized into two main directories:

## build-vanta
Scripts for setting up and configuring Vanta environments:

- **build_auth.py**: Handles authentication setup for Vanta.
- **create_access_accounts.py**: Creates access accounts for Vanta users.
- **create_on_prem_db.py**: Sets up an on-premises database for Vanta.

## manage-vanta
Scripts for ongoing management and document handling:

- **create_document.py**: Generates and manages documents within Vanta.
- **list_controls.py**: Lists available controls in the Vanta environment.
- **manage_auth.py**: Manages authentication and access for Vanta users.

## Setup
1. Create a Python virtual environment (recommended: `vantavenv`).
2. Install required dependencies (see script headers or requirements).
3. Activate the environment:
   ```bash
   source vantavenv/bin/activate
   ```

## Usage
Run scripts as needed from their respective directories. Example:
```bash
python manage-vanta/list_controls.py
```

## Notes
- The `.gitignore` excludes the virtual environment, cache files, and environment variables.
- For more details, see individual script docstrings.
