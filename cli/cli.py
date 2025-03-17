import os
import typer
import requests

app = typer.Typer()

# Load API URLs from environment variables
SECOND_BRAIN_API = "http://second-brain:8000"
WEAVIATE_URL = "http://weaviate:8080"

def print_response(response: requests.Response) -> None:
    """Helper function to print HTTP response details."""
    try:
        typer.secho(f"Response Status Code: {response.status_code}", fg="cyan")
        typer.echo(response.json())
    except Exception:
        typer.secho("Failed to decode JSON response.", fg="red")

@app.command("add-entry")
def add_entry(
    title: str = typer.Argument(..., help="Title for the journal entry"),
    content: str = typer.Argument(..., help="Content for the journal entry")
) -> None:
    """Add a new journal entry."""
    url = f"{SECOND_BRAIN_API}/add_entry/"
    payload = {"title": title, "content": content}
    typer.secho(f"📡 Sending entry to {url}", fg="green")
    try:
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            typer.secho("✅ Entry added successfully!", fg="green", bold=True)
        else:
            typer.secho("❌ Failed to add entry.", fg="red", bold=True)
    except Exception as e:
        typer.secho(f"❌ Request failed: {e}", fg="red", bold=True)

@app.command("get-entries")
def get_entries() -> None:
    """Retrieve all journal entries."""
    url = f"{SECOND_BRAIN_API}/entries/"
    typer.secho(f"📡 Fetching entries from {url}", fg="green")
    try:
        response = requests.get(url)
        if response.status_code == 200:
            entries = response.json()
            if not entries:
                typer.secho("No journal entries found.", fg="yellow")
                return
            typer.secho("📖 Journal Entries:", fg="blue", bold=True)
            for entry in entries:
                typer.echo(
                    f"📝 ID: {entry.get('id', 'N/A')} | Title: {entry.get('title', 'N/A')} | "
                    f"Content: {entry.get('content', 'N/A')} | Created At: {entry.get('created_at', 'N/A')}"
                )
        else:
            typer.secho("❌ Failed to retrieve entries.", fg="red", bold=True)
    except Exception as e:
        typer.secho(f"❌ Request failed: {e}", fg="red", bold=True)

@app.command("search")
def search(query: str = typer.Argument(..., help="Search query string")) -> None:
    """
    Perform a semantic search using Weaviate and then fetch the full entry from Second Brain.
    
    This command sends a GraphQL query to Weaviate to find a JournalEntry based on the query,
    retrieves the object's _additional.id, and then calls the new endpoint `/entries/{entry_id}/`
    to fetch the detailed journal entry from Second Brain.
    """
    # Build GraphQL query without newlines
    graphql_query = (
        "{ Get { JournalEntry(nearText: { concepts: [\"" + query + "\"] }, limit: 1) { "
        "_additional { id certainty } } } }"
    )
    payload = {"query": graphql_query}
    graphql_url = f"{WEAVIATE_URL}/v1/graphql"
    typer.secho(f"🔍 Searching for '{query}' using Weaviate at {graphql_url}", fg="green")
    try:
        response = requests.post(
            graphql_url,
            json=payload,
            headers={"Content-Type": "application/json"}
        )
        if response.status_code != 200:
            typer.secho(f"❌ Weaviate search failed: {response.status_code}", fg="red", bold=True)
            typer.echo(response.text)
            raise typer.Exit()
        data = response.json()
        results = data.get("data", {}).get("Get", {}).get("JournalEntry", [])
        if not results:
            typer.secho("⚠️ No matching entries found in Weaviate.", fg="yellow")
            raise typer.Exit()
        # Use the first result from the search
        entry_id = results[0].get("_additional", {}).get("id")
        certainty = results[0].get("_additional", {}).get("certainty")
        typer.secho(f"✅ Found entry with ID: {entry_id} (certainty: {certainty})", fg="blue")
        # Fetch full entry details from Second Brain using the new endpoint
        second_brain_url = f"{SECOND_BRAIN_API}/entries/{entry_id}/"
        typer.secho(f"📡 Fetching entry details from Second Brain at {second_brain_url}", fg="green")
        entry_response = requests.get(second_brain_url)
        if entry_response.status_code == 200:
            entry_data = entry_response.json()
            typer.secho("📖 Journal Entry Details:", fg="blue", bold=True)
            typer.echo(f"📝 ID: {entry_data.get('id', 'N/A')}")
            typer.echo(f"📝 Title: {entry_data.get('title', 'N/A')}")
            typer.echo(f"📝 Content: {entry_data.get('content', 'N/A')}")
            typer.echo(f"📝 Created At: {entry_data.get('created_at', 'N/A')}")
        else:
            typer.secho("❌ Failed to fetch entry details from Second Brain.", fg="red", bold=True)
            typer.echo(entry_response.text)
    except Exception as e:
        typer.secho(f"❌ Request failed: {e}", fg="red", bold=True)

if __name__ == "__main__":
    app()