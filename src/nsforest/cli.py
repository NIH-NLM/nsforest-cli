# src/nsforest/cli.py
import typer
app = typer.Typer()

@app.command()
def hello(name: str):
    """Say hello."""
    typer.echo(f"Hello {name} 👋")

if __name__ == "__main__":
    app()

# src/nsforest/core.py
def do_work():
    return "work done"

# src/nsforest/utils.py
def add(x, y):
    return x + y

# tests/test_cli.py
def test_add():
    from nsforest.utils import add
    assert add(2, 2) == 4

