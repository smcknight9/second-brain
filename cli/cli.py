import typer
import requests

app = typer.Typer()

API_URL = "http://localhost:8000"

## command for writing journal entires
@app.command()
def add_entry(content: str = typer.Argument(..., help="Journal entry content")):
    """Add a new journal entry"""
    typer.echo(f"📡 Sending request to {API_URL}/add_entry/ with content: {content}")

    try:
        response = requests.post(f"{API_URL}/add_entry/?content={content}")

        typer.echo(f"🔍 Response Status Code: {response.status_code}")
        typer.echo(f"📝 Response JSON: {response.json()}")

        if response.status_code == 200:
            typer.echo("✅ Entry added successfully!")
        else:
            typer.echo("❌ Failed to add entry.")

    except Exception as e:
        typer.echo(f"❌ Request failed: {e}")

## command for retrieving journal entries
@app.command()
def get_entries():
    """Retrieve all journal entries"""
    typer.echo(f"📡 Fetching journal entries from {API_URL}/entries/")

    try:
        response = requests.get(f"{API_URL}/entries/")

        typer.echo(f"🔍 Response Status Code: {response.status_code}")

        if response.status_code == 200:
            entries = response.json()
            typer.echo("📖 Journal Entries:")
            for entry in entries:
                typer.echo(f"📝 ID: {entry['id']} | Content: {entry['content']} | Created At: {entry['created_at']}")
        else:
            typer.echo("❌ Failed to retrieve entries.")

    except Exception as e:
        typer.echo(f"❌ Request failed: {e}")

if __name__ == "__main__":
    app()

