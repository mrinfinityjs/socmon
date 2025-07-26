# Social Search CLI

A command-line tool to search for keywords across Hacker News and Reddit simultaneously. It fetches recent posts and comments and displays them in a clean, color-coded format directly in your terminal.

## Features

-   **Multi-Platform Search**: Searches both Hacker News (posts and comments) and Reddit.
-   **Keyword-Based**: Simple to use, just provide a search term.
-   **Clean Terminal Output**: Uses the `rich` library for beautifully formatted and readable results.
-   **Easy to Configure**: Manages API keys securely using a `.env` file.
-   **Lightweight Environment**: Uses `uv` for fast and efficient dependency management.

## Requirements

-   Python 3.8+
-   `uv` (for environment and package management)
-   Python libraries:
    -   `python-hn`
    -   `praw`
    -   `rich`
    -   `python-dotenv`

## Setup and Installation

Follow these steps to get the project set up and ready to run.

### 1. Clone the Repository

First, clone this repository to your local machine (or simply download the `search.py` script).

```bash
git clone https://github.com/mrinfinityjs/socmon.git
cd socmon
```

If you only have the script, create a project directory and place `search.py` inside it.

### 2. Set Up the Virtual Environment with `uv`

This project uses `uv` for fast virtual environment and package management. If you don't have `uv`, install it first:

```bash
pip install uv
```

Now, create and activate the virtual environment:

```bash
# Create the venv
uv venv

# Activate it (on macOS/Linux)
source .venv/bin/activate

# Or activate it (on Windows)
.venv\Scripts\activate
```

### 3. Install Dependencies

Install the required Python packages using `uv`:

```bash
uv pip install python-hn praw rich python-dotenv
```

### 4. Get Reddit API Credentials

To search Reddit, you need API credentials.

1.  Go to your [Reddit Apps](https://www.reddit.com/prefs/apps) page.
2.  Click "are you a developer? create an app...".
3.  Fill out the form:
    -   **name**: `SocialSearch` (or any name you prefer)
    -   **type**: select **script**
    -   **redirect uri**: `http://localhost:8080`
4.  Click "create app". You will now see your **client ID** (a string of characters under the app name) and your **client secret**.

### 5. Create the Environment File

Create a file named `.env` in the root of your project directory. This file will hold your secret credentials.

```bash
touch .env
```

Open the `.env` file and add your Reddit credentials in the following format:

```ini
REDDIT_CLIENT_ID=your_client_id_here
REDDIT_CLIENT_SECRET=your_client_secret_here
REDDIT_USER_AGENT=SocialSearchCLI/1.0 by YourUsername
```

Replace the placeholder text with your actual credentials. The `REDDIT_USER_AGENT` can be any unique string.

## Usage

To run the script, use the `python` command followed by the script name and the keyword(s) you want to search for. The keywords should be enclosed in quotes if they contain spaces.

**Syntax:**

```bash
python search.py "your keywords"
```

**Example:**

```bash
python search.py "serverless containers"
```

The script will search both platforms and print the results to your terminal before exiting.

## Example Output

The output is formatted for readability, with colors to distinguish titles, authors, and links.

```
─────────────────────────────── Hacker News Results ────────────────────────────────

Show HN: A new open-source serverless container platform
by some_user
https://news.ycombinator.com/item?id=123456
────────────────────────────────────────────────────────────────────────────────

Has anyone compared the cold start times for serverless containers on AWS vs Google Cloud?
by another_dev
https://news.ycombinator.com/item?id=789101

──────────────────────────────── Reddit Results ─────────────────────────────────

Finally moved my side project to serverless containers and the cost savings are insane.
in r/devops by reddit_user1
https://www.reddit.com/r/devops/comments/abcde/comment/
────────────────────────────────────────────────────────────────────────────────

What are the best practices for logging and monitoring in serverless containers?
in r/aws by another_redditor
https://www.reddit.com/r/aws/comments/fghij/comment/
```

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
