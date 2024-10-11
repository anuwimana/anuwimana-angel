
# Stack for undoing team entries
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, team ):
        self.stack.append(team )

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return None

    def is_empty(self):
        return len(self.stack) == 0

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        return None

# Queue for scheduling matches
from collections import deque
class Queue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self,team):
        self.queue.append(team)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.popleft()
        return None

    def is_empty(self):
        return len(self.queue) == 0

# List for managing team rankings
class Rankings:
    def __init__(self):
        self.rankings = []

    def add_team(self, team):
        self.rankings.append(team)

    def update_ranking(self, team, new_rank):
        for i, (t, rank) in enumerate(self.rankings):
            if t == team:
                self.rankings[i] = (team, new_rank)
                break

    def sort_rankings(self):
        self.rankings.sort(key=lambda x: x[1])  # Sort by rank

    def display(self):
        for team, rank in self.rankings:
            print(f"Team: {team}, Rank: {rank}")

# Putting it all together
class TournamentScheduler:
    def __init__(self):
        self.teams_stack = Stack()  # Stack for team entries
        self.match_queue = Queue()  # Queue for matches
        self.rankings = Rankings()  # List for rankings

    # Add team to the stack and rankings list
    def add_team(self, team, rank):
        self.teams_stack.push(team)
        self.rankings.add_team((team, rank))

    # Undo team entry (remove last added team)
    def undo_team_entry(self):
        removed_team = self.teams_stack.pop()
        if removed_team:
            print(f"Undo team entry: {removed_team}")
        else:
            print("No teams to undo.")

    # Schedule match between two teams
    def schedule_match(self, team1, team2):
        self.match_queue.enqueue((team1, team2))

    # Get next scheduled match
    def next_match(self):
        match = self.match_queue.dequeue()
        if match:
            print(f"Next match: {match[0]} vs {match[1]}")
        else:
            print("No matches scheduled.")

    # Display current team rankings
    def display_rankings(self):
        self.rankings.sort_rankings()
        self.rankings.display()

# Example usage
if __name__ == "__main__":
    scheduler = TournamentScheduler()

    # Add teams
    scheduler.add_team("Team A", 1)
    scheduler.add_team("Team B", 2)
    scheduler.add_team("Team C", 3)

    # Schedule matches
    scheduler.schedule_match("Team A", "Team B")
    scheduler.schedule_match("Team B", "Team C")

    # Show rankings
    print("\nCurrent rankings:")
    scheduler.display_rankings()

    # Undo last team entry
    scheduler.undo_team_entry()

    # Show next match
    print("\nNext match:")
    scheduler.next_match()

    # Show rankings after undo
    print("\nRankings after undo:")
    scheduler.display_rankings()

