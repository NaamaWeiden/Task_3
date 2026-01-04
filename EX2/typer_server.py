import typer
import json
import os

app = typer.Typer()
FILE_PATH = "titanic.json"

@app.command()
def add(json_str: str):
    try:
        data = json.loads(json_str)
    except json.JSONDecodeError:
        typer.echo("Invalid JSON")
        raise typer.Exit(code=1)

    if os.path.exists(FILE_PATH):
        with open(FILE_PATH, "r") as f:
            file_data = json.load(f)
    else:
        file_data = []

    file_data.append(data)

    with open(FILE_PATH, "w") as f:
        json.dump(file_data, f, indent=2)

    typer.echo("JSON added!")

@app.command()
def last10():
    if not os.path.exists(FILE_PATH):
        typer.echo("No data yet.")
        raise typer.Exit(code=1)

    with open(FILE_PATH, "r") as f:
        file_data = json.load(f)

    for item in file_data[-10:]:
        typer.echo(item)

if __name__ == "__main__":
    app()
