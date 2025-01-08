import mlrose
from typing import List, Dict, Tuple

class FlightScheduler:
    def __init__(self, people: List[Tuple[str, str]], destination: str, flights_file: str):
        self.people = people
        self.destination = destination
        self.flights = self._load_flights(flights_file)

    @staticmethod
    def _load_flights(flights_file: str) -> Dict[Tuple[str, str], List[Tuple[str, str, int]]]:
        flights: Dict[Tuple[str, str], List[Tuple[str, str, int]]] = {}
        with open(flights_file, "r") as file:
            for line in file:
                origin, destination, departure, arrival, price = line.strip().split(",")
                flights.setdefault((origin, destination), []).append((departure, arrival, int(price)))
        return flights

    def fitness_function(self, schedule: List[int]) -> int:
        total_price: int = 0
        flight_index: int = 0

        for i in range(len(self.people)):
            origin: str = self.people[i][1]

            outbound_flight = self.flights[(origin, self.destination)][schedule[flight_index]]
            total_price += outbound_flight[2]
            flight_index += 1

            return_flight = self.flights[(self.destination, origin)][schedule[flight_index]]
            total_price += return_flight[2]
            flight_index += 1

        return total_price

    def optimize_schedule(self, max_val: int, max_attempts: int = 100, max_iters: int = 1000) -> Tuple[List[int], int]:
        fitness = mlrose.CustomFitness(self.fitness_function)
        problem = mlrose.DiscreteOpt(
            length=len(self.people) * 2,
            fitness_fn=fitness,
            maximize=False,
            max_val=max_val
        )

        best_schedule, best_cost = mlrose.random_hill_climb(
            problem,
            max_attempts=max_attempts,
            max_iters=max_iters
        )

        return best_schedule, best_cost

def main():
    people = [
        ("Lisboa", "LIS"),
        ("Madrid", "MAD"),
        ("Paris", "CDG"),
        ("Dublin", "DUB"),
        ("Bruxelas", "BRU"),
        ("Londres", "LHR")
    ]

    destination = "FCO"
    flights_file = "flights.txt"

    scheduler = FlightScheduler(people, destination, flights_file)

    best_schedule, best_cost = scheduler.optimize_schedule(max_val=10)

    print("Best Schedule:", best_schedule)
    print("Total Cost:", best_cost)

if __name__ == "__main__":
    main()
