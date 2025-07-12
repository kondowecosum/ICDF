from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt
from rich.panel import Panel

class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self._hash(key)
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index][i] = (key, value)
                return f"[yellow][INFO][/yellow] Updated key '{key}' with new value '{value}'"
        self.table[index].append((key, value))
        return f"[green][INFO][/green] Inserted key '{key}' with value '{value}'"

    def search(self, key):
        index = self._hash(key)
        for k, v in self.table[index]:
            if k == key:
                return f"[green][FOUND][/green] Key: '{key}' -> Value: '{v}'"
        return f"[red][NOT FOUND][/red] Key '{key}' does not exist."

    def delete(self, key):
        index = self._hash(key)
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                del self.table[index][i]
                return f"[blue][INFO][/blue] Key '{key}' deleted."
        return f"[red][NOT FOUND][/red] Key '{key}' not found."

    def display(self):
        table_view = Table(title="Hash Table Contents")
        table_view.add_column("Index", justify="center", style="bold cyan")
        table_view.add_column("Bucket", style="bold white")

        for i, bucket in enumerate(self.table):
            content = ", ".join(f"({k}: {v})" for k, v in bucket) or "Empty"
            table_view.add_row(str(i), content)

        console.print(table_view)


# Console setup
console = Console()

def main():
    ht = HashTable()
    console.print(Panel.fit("[bold green]Simple Hash Table Interface[/bold green]", title="💡 Hash Table"))

    while True:
        console.print("\n[bold cyan]Choose an option:[/bold cyan]")
        console.print("1. Insert a key-value pair")
        console.print("2. Search for a key")
        console.print("3. Delete a key")
        console.print("4. Display hash table")
        console.print("5. Exit")

        choice = Prompt.ask("Enter your choice (1-5)")

        if choice == "1":
            key = Prompt.ask("Enter key")
            value = Prompt.ask("Enter value")
            console.print(ht.insert(key, value))

        elif choice == "2":
            key = Prompt.ask("Enter key to search")
            console.print(ht.search(key))

        elif choice == "3":
            key = Prompt.ask("Enter key to delete")
            console.print(ht.delete(key))

        elif choice == "4":
            ht.display()

        elif choice == "5":
            console.print("[bold yellow]Goodbye![/bold yellow] 👋")
            break

        else:
            console.print("[red][ERROR][/red] Invalid option. Please try again.")

if __name__ == "__main__":
    main()
