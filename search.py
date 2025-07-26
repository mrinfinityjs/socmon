import os
import argparse
import praw
from hn import search_by_date
from rich.console import Console
from rich.rule import Rule
from rich.text import Text
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize Rich Console for beautiful terminal output
console = Console()

def search_hacker_news(keywords):
    """
    Searches Hacker News for the given keywords.
    """
    try:
        # search_by_date returns a generator, so we convert it to a list
        results = list(search_by_date(
            q=keywords,
            stories=True,
            comments=True,
            hits_per_page=10
        ))
        return results
    except Exception as e:
        console.print(f"[bold red]Error searching Hacker News: {e}[/bold red]")
        return []

def search_reddit(keywords):
    """
    Searches Reddit for the given keywords.
    """
    try:
        reddit = praw.Reddit(
            client_id=os.getenv("REDDIT_CLIENT_ID"),
            client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
            user_agent=os.getenv("REDDIT_USER_AGENT"),
        )
        subreddit = reddit.subreddit("all")
        # The 'praw' search returns a generator, so we convert it to a list
        results = list(subreddit.search(keywords, limit=10))
        return results
    except Exception as e:
        console.print(f"[bold red]Error searching Reddit: {e}[/bold red]")
        return []

def display_results(hn_results, reddit_results):
    """
    Displays the search results with a simple line separator.
    """
    console.rule("[bold cyan]Hacker News Results[/bold cyan]", style="cyan")
    if not hn_results:
        console.print("[dim]No results found on Hacker News.[/dim]")
    else:
        # Enumerate to add a separator between items but not after the last one
        for i, result in enumerate(hn_results):
            title_or_comment = result.get('title') or result.get('comment_text', 'No Title/Comment')
            # Clean the text to prevent Rich from misinterpreting brackets as style tags
            title_or_comment = title_or_comment.replace('[', r'\[')
            
            author = result.get('author', 'N/A')
            url = result.get('story_url') or result.get('url') or f"https://news.ycombinator.com/item?id={result.get('objectID')}"

            # Create a Text object for formatted content
            text_content = Text()
            text_content.append(f"{title_or_comment}\n", style="bold magenta")
            text_content.append(f"by {author}\n", style="green")
            text_content.append(url, style="blue underline")

            # Print the formatted text directly, without a panel
            console.print(text_content)

            # If it's not the last item, print a separator
            if i < len(hn_results) - 1:
                console.print(Rule(style="grey50"))

    console.print() # Add a blank line for spacing
    console.rule("[bold orange3]Reddit Results[/bold orange3]", style="orange3")
    if not reddit_results:
        console.print("[dim]No results found on Reddit.[/dim]")
    else:
        for i, submission in enumerate(reddit_results):
            title = submission.title.replace('[', r'\[')
            author = submission.author.name if submission.author else '[deleted]'
            subreddit = submission.subreddit.display_name
            url = f"https://www.reddit.com{submission.permalink}"

            text_content = Text()
            text_content.append(f"{title}\n", style="bold magenta")
            text_content.append(f"in r/{subreddit} by {author}\n", style="green")
            text_content.append(url, style="blue underline")
            
            console.print(text_content)
            
            # If it's not the last item, print a separator
            if i < len(reddit_results) - 1:
                console.print(Rule(style="grey50"))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Search Hacker News and Reddit for keywords.")
    parser.add_argument("keywords", type=str, help="The keywords to search for.")
    args = parser.parse_args()

    # Use a status indicator while searching
    with console.status("[bold green]Searching...") as status:
        hn_results = search_hacker_news(args.keywords)
        status.update("[bold green]Searching Reddit...")
        reddit_results = search_reddit(args.keywords)
    
    console.print()
    display_results(hn_results, reddit_results)
