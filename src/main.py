from datetime import date
from typing import Dict
from .models import Habit
from .storage import load_habits, save_habits, delete_habit

def prompt_non_empty(prompt: str) -> str:
    """Prompt the user until they provide a non-empty input."""
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Input cannot be empty. Please try again.")

def prompt_integer(prompt: str) -> int:
    """Prompt the user until they provide a valid integer."""
    while True:
        try:
            value = int(input(prompt).strip())
            return value
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def prompt_frequency(prompt: str) -> str:
    """Prompt the user until they provide a valid frequency."""
    valid_frequencies = {"daily", "weekly"}
    while True:
        value = input(prompt).strip().lower()
        if value in valid_frequencies:
            return value
        print(f"Invalid frequency. Please enter one of: {', '.join(valid_frequencies)}.")

def show_habits(habits: Dict[str, Habit]) -> None:
    """Display the list of habits."""
    if not habits:
        print("No habits found.")
        return
    for hid, habit in habits.items():
        rate = habit.get_completion_rate() * 100
        print(f"ID: {hid}, Name: {habit.name}, Frequency: {habit.frequency}, Target: {habit.target}, Completion Rate: {rate:.2f}%")

def add_habit() -> None:
    """Add a new habit."""
    habits = load_habits()
    hid = prompt_non_empty("Enter habit ID: ")
    if hid in habits:
        print("Habit ID already exists. Please choose a different ID.")
        return
    name = prompt_non_empty("Enter habit name: ")
    frequency = prompt_frequency("Enter habit frequency (daily/weekly): ")
    target = prompt_integer("Enter habit target (number of times to complete): ")
    habit = Habit(id=hid, name=name, frequency=frequency, target=target)
    habits[hid] = habit
    save_habits(habits)
    print("Habit added successfully.")

def check_in_habit() -> None:
    """Check in a habit for today."""
    habits = load_habits()
    hid = prompt_non_empty("Enter habit ID to check in: ")
    if hid not in habits:
        print("Habit ID not found.")
        return
    habit = habits[hid]
    today = date.today()
    habit.check_in(today)
    save_habits(habits)
    print(f"Habit '{habit.name}' checked in for {today}.")

def delete_habit_by_id() -> None:
    """Delete a habit by its ID."""
    hid = prompt_non_empty("Enter habit ID to delete: ")
    habits = load_habits()
    if hid not in habits:
        print("Habit ID not found.")
        return
    delete_habit(hid)
    print("Habit deleted successfully.")

def main() -> None:
    """Main function to run the habit tracker CLI."""
    while True:
        print("\nHabit Tracker Menu:")
        print("1. Show Habits")
        print("2. Add Habit")
        print("3. Check In Habit")
        print("4. Delete Habit")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ").strip()
        if choice == "1":
            habits = load_habits()
            show_habits(habits)
        elif choice == "2":
            add_habit()
        elif choice == "3":
            check_in_habit()
        elif choice == "4":
            delete_habit_by_id()
        elif choice == "5":
            print("Exiting Habit Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")