import hashlib
import getpass
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Confirm

console = Console()


def hash_password(password):
    """Hash a password using SHA-256"""
    return hashlib.sha256(password.encode()).hexdigest()


def main():
    console.print(Panel.fit("[bold cyan]🔐 Password Hashing System (SHA-256)[/bold cyan]"))

    # Secure password input
    password = getpass.getpass("Enter password: ")

    # Confirm hashing
    if not Confirm.ask("Do you want to hash this password?"):
        console.print("[bold yellow]Operation cancelled.[/bold yellow]")
        return

    # Hash the password
    hashed_password = hash_password(password)

    # Display result
    console.print("\n[bold green]✅ Password hashed successfully![/bold green]")
    console.print(f"[blue]SHA-256 Hash:[/blue] [bold magenta]{hashed_password}[/bold magenta]")
    console.print("\n[dim]Note: The original password is never displayed or stored.[/dim]")


if __name__ == "__main__":
    main()
