# Forza Horizon 6 - AFK Script
# @author: pwnedroot

import pyautogui
import time
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn, TimeElapsedColumn
from rich.table import Table
from rich.align import Align
from rich import box
from datetime import datetime

console = Console()

# ─── Banner ───────────────────────────────────────────────────────────────────

def print_banner():
    banner = Text()
    banner.append("███████╗ ██████╗ ██████╗ ███████╗ █████╗ \n", style="bold bright_cyan")
    banner.append("██╔════╝██╔═══██╗██╔══██╗╚══███╔╝██╔══██╗\n", style="bold cyan")
    banner.append("█████╗  ██║   ██║██████╔╝  ███╔╝ ███████║\n", style="bold bright_blue")
    banner.append("██╔══╝  ██║   ██║██╔══██╗ ███╔╝  ██╔══██║\n", style="bold blue")
    banner.append("██║     ╚██████╔╝██║  ██║███████╗██║  ██║\n", style="bold bright_magenta")
    banner.append("╚═╝      ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝\n", style="bold magenta")

    subtitle = Text("  HORIZON 6  ──  AFK RACE SCRIPT  ──  by pwnedroot", style="bold bright_white on dark_blue")

    console.print(Panel(
        Align(banner, align="center"),
        border_style="bright_cyan",
        padding=(0, 2),
    ))
    console.print(Align(subtitle, align="center"))
    console.print()

# ─── Status Table ─────────────────────────────────────────────────────────────

def build_status_table(lap: int, action: str, status_color: str = "green"):
    table = Table(box=box.DOUBLE_EDGE, border_style="bright_blue", show_header=False, padding=(0, 2))
    table.add_column(justify="right", style="bold bright_black", min_width=18)
    table.add_column(justify="left", style="bold white", min_width=24)

    table.add_row("🏁  Races Completed", f"[bold bright_yellow]{lap}[/]")
    table.add_row("⚡  Current Action", f"[{status_color}]{action}[/]")
    table.add_row("🕒  Time", f"[bright_cyan]{datetime.now().strftime('%I:%M:%S %p')}[/]")

    return Panel(Align(table, align="center"), title="[bold bright_cyan]RACE STATUS[/]", border_style="cyan")

# ─── Countdown ────────────────────────────────────────────────────────────────

def countdown(message: str, seconds: int, style: str = "yellow"):
    for i in range(seconds, 0, -1):
        console.print(
            f"  [bold {style}]{message}[/] [bold white]in[/] [bold bright_white]{i}s[/]...",
            end="\r"
        )
        time.sleep(1)
    console.print(" " * 60, end="\r")

# ─── Sleep with live bar ──────────────────────────────────────────────────────

def sleep_with_bar(seconds: int, label: str = "Waiting"):
    with Progress(
        SpinnerColumn(style="bright_cyan"),
        TextColumn(f"[bold bright_white]{label}[/]"),
        BarColumn(bar_width=36, style="bright_blue", complete_style="bright_cyan"),
        TextColumn("[bold bright_yellow]{task.percentage:>3.0f}%[/]"),
        TimeElapsedColumn(),
        console=console,
        transient=True,
    ) as progress:
        task = progress.add_task("", total=seconds)
        for _ in range(seconds):
            time.sleep(1)
            progress.advance(task)

# ─── Main ─────────────────────────────────────────────────────────────────────

def main():
    print_banner()

    console.print(Panel(
        "[bold yellow]⚠  Make sure you are on the page to start the race![/]\n"
        "[bright_black]   Script will begin automatically after countdown.[/]",
        border_style="yellow",
        title="[bold yellow]ATTENTION[/]",
    ))
    console.print()

    countdown("Switching to Forza window", 5, style="yellow")

    console.print(Panel(
        "[bold bright_green]✔  Click inside the Forza Horizon 6 window now![/]",
        border_style="bright_green",
    ))
    console.print()

    countdown("Launching script", 5, style="bright_cyan")

    # Press Enter once to start the very first race
    console.print(f"\n  [bold bright_green]▶  Pressing ENTER to start race...[/]\n")
    pyautogui.press('enter')
    sleep_with_bar(10, "Waiting for race to load")

    race_count = 0

    # Every race: drive → X → Enter (confirms and auto-loads next race)
    while True:
        race_count += 1
        console.rule(f"[bold bright_cyan]  RACE #{race_count}  ", style="bright_blue")
        console.print()

        console.print(build_status_table(race_count - 1, "🚗  Driving (W held)...", "bright_green"))
        pyautogui.keyDown('w')
        time.sleep(30)  # plain sleep — no terminal updates while key is held
        pyautogui.keyUp('w')

        sleep_with_bar(5, "Waiting for end screen to load")

        console.print(build_status_table(race_count - 1, "⏭   Restarting (X)...", "bright_yellow"))
        pyautogui.press('x')
        sleep_with_bar(5, "Waiting for restart prompt")

        console.print(build_status_table(race_count - 1, "✅  Confirming restart (Enter)...", "bright_cyan"))
        pyautogui.press('enter')
        sleep_with_bar(8, "Waiting...")

        console.print(build_status_table(race_count - 1, "🚀  Starting race (Enter)...", "bright_magenta"))
        pyautogui.press('enter')
        sleep_with_bar(8, "Waiting...")

        console.print(build_status_table(race_count - 1, "🚀  Confirming start (Enter)...", "bright_magenta"))
        pyautogui.press('enter')
        sleep_with_bar(10, "Waiting for race to load")

        console.print(f"\n  [bold bright_green]✔  Race #{race_count} complete![/] [bright_black]Looping...[/]\n")

if __name__ == "__main__":
    main()
