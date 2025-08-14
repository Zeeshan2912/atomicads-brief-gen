import typer
import requests
import os

app = typer.Typer()
DEFAULT_URL = f"http://localhost:{os.getenv('PORT', '8000')}"

@app.command()
def brief(topic: str, depth: int = 1, user_id: str = "local_user", host: str = DEFAULT_URL):
    payload = {"topic": topic, "depth": depth, "user_id": user_id}
    r = requests.post(f"{host}/brief", json=payload)
    typer.echo(r.json())

if __name__ == "__main__":
    app()