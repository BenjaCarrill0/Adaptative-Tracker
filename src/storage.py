import json
from pathlib import Path
from typing import Dict
from .models import Habit

DATA_FILE = Path("data.json")

def load_habits() -> Dict[str, Habit]:
    """Load habits from the JSON data file."""
    if not DATA_FILE.exists():
        return {}
    with open(DATA_FILE, "r") as f:
        data = json.load(f)
    habits = {hid: Habit(**habit_data) for hid, habit_data in data.items()}
    return habits

def save_habits(habits: Dict[str, Habit]) -> None:
    """Save habits to the JSON data file."""
    data = {hid: habit.__dict__ for hid, habit in habits.items()}
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

def delete_habit(habit_id: str) -> None:
    """Delete a habit by its ID."""
    habits = load_habits()
    if habit_id in habits:
        del habits[habit_id]
        save_habits(habits)