# Flight Scheduler Optimizer

This project uses optimization algorithms to find the most cost-effective flight combinations for a group of people traveling to a common destination. It is a Python-based intelligent solution leveraging the `mlrose` library to solve discrete optimization problems.

## Features

- **Data Loading**: Imports flight information from a CSV file (departure times, arrival times, and prices).
- **Group Customization**: Allows defining the group of people and their departure airports.
- **Cost Optimization**: Calculates the flight combination with the lowest total cost for round trips to the chosen destination.
- **Flexible Configuration**: Enables adjusting optimization parameters, such as the maximum number of attempts and iterations.

## Technologies Used

- **Python**: The main programming language of the project.
- **mlrose**: Library for solving discrete optimization problems.
- **Type Hints**: For better code readability and maintainability.

## Project Structure

- `flight_scheduler.py`: Main file containing the project implementation.
- `flights.txt`: Input file with flight data (origin, destination, departure, arrival, and price).

## How to Use

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/flight-scheduler-optimizer.git
   ```

2. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Replace the `flights.txt` file with the flight data you want to use.

4. Run the script:
   ```bash
   python flight_scheduler.py
   ```

## Example Data in `flights.txt`

The file should contain lines in the following format:
```
Origin,Destination,Departure,Arrival,Price
LIS,FCO,6:00,8:30,250
MAD,FCO,7:00,9:30,200
```

