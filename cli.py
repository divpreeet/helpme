import os
import sys
import traceback
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt, Confirm
from rich.table import Table
import main as main
import zoom as zoom
import random

console = Console()
responses = [
    "Miss, I am getting the answer as,",
    "I think the answer is,",
    "I am pretty sure the answer is,",
    "Miss, the answer is,",
    "The answer is,",
    "I think the answer to the question is,"
]


def title():
    console.print(
        Panel.fit(
            "[bold cyan]helpme[/bold cyan]\n"
            "[dim]an gemini powered question solver with playback in your voice, for me to be lazy[/dim]"
        )
    )

def menu():
    table = Table(title="action", show_lines=True)
    table.add_column("key", style="bold yellow", justify="center")
    table.add_column("action", style="white")
    table.add_row("1", "ss + AI answer")
    table.add_row("2", "ss + AI answer with zoom playback")
    table.add_row("q", "quit")
    console.print(table)

def full():
    console.print("\n[bold]1: capture screenshot[/bold]")
    shot = main.capture_q()

    if not shot or not os.path.exists(shot):
        console.print("[red]screenshot not found[/red]")
        return

    console.print(f"[green]captured: [/green] {shot}")
    console.print("[bold]2. ask ai[/bold]")
    encoded = main.encode(shot)
    answer_ai, error = main.ask_ai(encoded)

    if error:
        console.print(f"[red]{error}[/red]")
        return

    console.print(Panel.fit(f"[bold green]{answer_ai}[/bold green]\n"))

    console.print("[bold]3. generating and playing tts locally before zoom[/bold]")
    main.speak(f"{random.choice(responses)} {answer_ai}")

    console.print("[bold]4. sending audio to zoom now[/bold]")
    zoom.focus("result.wav")
    console.print("[green]done.[/green]")
    

def answer():
    console.print("\n[bold]1: capture screenshot[/bold]")
    shot = main.capture_q()

    if not shot or not os.path.exists(shot):
        console.print("[red]screenshot not found[/red]")
        return

    console.print(f"[green]captured: [/green] {shot}")
    console.print("[bold]2. ask ai[/bold]")
    encoded = main.encode(shot)
    answer_ai, error = main.ask_ai(encoded)

    if error:
        console.print(f"[red]{error}[/red]")
        return

    console.print(Panel.fit(f"[bold green]{answer_ai}[/bold green]\n"))

def run():
    while True:
        console.clear()
        title()
        menu()
        choice = Prompt.ask("select", default="1").strip().lower()

        try:
            if choice == "1":
                answer()
            elif choice == "2":
                full()
            elif choice == "q":
                console.print("[cyan]bye[/cyan]")
                sys.exit(0)
            else:
                console.print("[yellow]invalid choice[/yellow]")
        except KeyboardInterrupt:
            console.print("\n[yellow]interrupted[/yellow]")
        except Exception as e:
            console.print(e)

        input("\npress enter to continue")
    
if __name__ == "__main__":
    run()