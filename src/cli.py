import typer
import requests
import os

DEFAULT_URL = f"http://localhost:{os.getenv('PORT', '8000')}"

def main(
    topic: str = typer.Option(..., "--topic", help="Topic for the ad brief"),
    depth: int = typer.Option(1, "--depth", help="Depth of analysis"),
    user_id: str = typer.Option("local_user", "--user-id", help="User ID"),
    host: str = typer.Option(DEFAULT_URL, "--host", help="API host")
):
    """
    Generate an ad brief using the API.
    """
    payload = {"topic": topic, "depth": depth, "user_id": user_id}
    r = requests.post(f"{host}/brief", json=payload)
    typer.echo(r.json())

if __name__ == "__main__":
    typer.run(main)
