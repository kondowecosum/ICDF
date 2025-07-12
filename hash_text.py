import hashlib
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Confirm

console = Console()

def compute_file_hash(filename):
    with open(filename, "rb") as file:
        content = file.read()
        return hashlib.sha256(content).hexdigest()

def create_file(filename, content):
    with open(filename, "w") as file:
        file.write(content)

# Display heading
console.print(Panel.fit("[bold cyan]🔐 Hash Function Avalanche Effect Demo[/bold cyan]"))

# Step 1: Create original file
original_content = """Lab 2: Exploring Hash Functions

Learning outcomes: Understand the importance of hash functions in cryptography."""
original_filename = "hash_test_file.txt"

create_file(original_filename, original_content)
console.print(f"[green]✔ Created original file:[/green] [bold]{original_filename}[/bold]")

# Step 2: Compute and display original hash
original_hash = compute_file_hash(original_filename)
console.print(f"[yellow]Original File SHA-256 Hash:[/yellow] [bold magenta]{original_hash}[/bold magenta]")

# Step 3: Ask user to proceed with modification
proceed = Confirm.ask("\nDo you want to simulate a small change (1 character) to see the avalanche effect?")

if proceed:
    # Modify one character
    modified_content = """Lab 2: Exploring Hash Functions

Learning outcomes: understand the importance of hash functions in cryptography."""
    modified_filename = "hash_test_file_modified.txt"

    create_file(modified_filename, modified_content)
    console.print(f"\n[green]✔ Created modified file:[/green] [bold]{modified_filename}[/bold]")

    # Step 4: Compute and display modified hash
    modified_hash = compute_file_hash(modified_filename)
    console.print(f"[yellow]Modified File SHA-256 Hash:[/yellow] [bold red]{modified_hash}[/bold red]")

    # Step 5: Compare and explain
    console.print("\n[bold underline cyan]Hash Comparison Result[/bold underline cyan]")
    if original_hash != modified_hash:
        console.print("[bold red] Hashes are completely different![/bold red] Even a single character change causes a drastic difference.")
    else:
        console.print("[bold green]No change detected.[/bold green] (Unexpected — check your input)")
else:
    console.print("[bold yellow]Operation cancelled by user.[/bold yellow]")
