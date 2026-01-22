from dataclasses import dataclass, field
from typing import Dict
from datetime import date

@dataclass
class Habit:
    id: str
    name: str
    frequency: str  # e.g., "daily", "weekly"
    target: int  # e.g., number of times to complete the habit in the frequency period
    history: Dict[date, bool] = field(default_factory=dict)  # date -> completed or not 

    def check_in(self, check_date: date, completed: bool = True) -> None:
        """Mark the habit as completed for the given date."""
        self.history[check_date.isoformat()] = completed

    def get_completion_rate(self) -> float:
        """Calculate the completion rate of the habit."""
        if not self.history:
            return 0.0
        completed_days = sum(1 for completed in self.history.values() if completed)
        return completed_days / len(self.history)