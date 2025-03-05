import typer
import requests

app = typer.Typer()

API_URL = "http://localhost:8000"

@app.command()
def add_entry(content: str):
    """Add a new journal entry"""
    response = requests.post(f"{API_URL}/add_entry/", json=content)
    if response.status_code == 200:
        typer.echo("✅ Entry added successfully!")
    else:
        typer.echo("❌ Failed to add entry.")

@app.command()
def get_entries():
    """Retrieve all journal entries"""
    response = requests.get(f"{API_URL}/get_entries/")
    if response.status_code == 200:
        entries = response.json()
        for entry in entries:
            typer.echo(f"{entry['id']}: {entry['content']} (Created: {entry['created_at']})")
    else:
        typer.echo("❌ Failed to retrieve entries.")

if __name__ == "__main__":
    app()


