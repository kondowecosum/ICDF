import hashlib
import sys
import tty
import termios
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Confirm

console = Console()

def get_password_with_stars(prompt="Enter password: "):
    console.print(f"[bold]{prompt}[/bold]", end="", style="cyan")
    password = ""
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)

    try:
        tty.setraw(fd)
        while True:
            ch = sys.stdin.read(1)
            if ch == "\r" or ch == "\n":
                print()  # Move to next line
                break
            elif ch == "\x7f":  # Backspace
                if len(password) > 0:
                    password = password[:-1]
                    sys.stdout.write("\b \b")
                    sys.stdout.flush()
            else:
                password += ch
                sys.stdout.write("*")
                sys.stdout.flush()
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

    return password

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def main():
    console.print(Panel.fit("[bold cyan]🔐 Password Hashing System (SHA-256)[/bold cyan]"))

    # Get password with visible *
    password = get_password_with_stars("Enter password: ")

    if not Confirm.ask("Do you want to hash this password?"):
        console.print("[bold yellow]Operation cancelled.[/bold yellow]")
        return

    hashed_password = hash_password(password)

    console.print("\n[bold green]✅ Password hashed successfully![/bold green]")
    console.print(f"[blue]SHA-256 Hash:[/blue] [bold magenta]{hashed_password}[/bold magenta]")
    console.print("\n[dim]Note: Your original password was hidden during hashing.[/dim]")

if __name__ == "__main__":
    main()
