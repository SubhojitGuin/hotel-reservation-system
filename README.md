# Hotel Reservation System

This project is a simple hotel reservation system implemented in Python. It allows users to book hotels based on availability and manage customer reservations. The system utilizes CSV files for storing hotel information, credit card details, and card security.

## Features

- Hotel Class: Represents a hotel and provides methods to check availability and book a hotel.
- ReservationTicket Class: Generates a reservation ticket with customer details and the name of the booked hotel.
- CreditCard Class: Represents a credit card and validates card details.
- SecureCreditCard Class: Inherits from CreditCard and adds authentication using a password.

## Usage

1. Prepare CSV files:
   - Create a `hotels.csv` file with hotel information, including ID, name, city, capacity, and availability.
   - Create a `cards.csv` file with credit card information, including number, expiration date, CVV, and holder name.
   - Create a `card_security.csv` file with credit card number and corresponding password.

2. Update file paths:
   - Modify the file paths in the script (`main.py`) to match the locations of the CSV files.

3. Run the script:
   - Execute the script and follow the prompts.
   - Enter the ID of the hotel you want to book.
   - Provide credit card details for validation and authentication.
   - If the hotel is available, it will be booked, and a reservation ticket will be generated.

## Requirements

The project requires the following dependencies:

- numpy==1.25.0
- pandas==2.0.2
- python-dateutil==2.8.2
- pytz==2023.3
- six==1.16.0
- tzdata==2023.3

Install the dependencies using `pip install -r requirements.txt` before running the script.

## Acknowledgements

We would like to acknowledge the contributions of the developers and contributors to the open-source libraries used in this project. Their dedication and hard work have made this project possible.

Special thanks to:

- [Pandas](https://pandas.pydata.org/) - for providing powerful data manipulation and analysis tools.
- [NumPy](https://numpy.org/) - for providing efficient numerical computations and array operations.
- [Python-Dateutil](https://dateutil.readthedocs.io/) - for providing helpful date and time utilities.
- [Pytz](https://pythonhosted.org/pytz/) - for providing timezone support for Python.
- [Six](https://pypi.org/project/six/) - for providing compatibility utilities for Python 2 and 3.
- [Tzdata](https://www.iana.org/time-zones) - for providing timezone data.

Without the contributions of these amazing open-source projects and the developers behind them, this project would not have been possible. We express our gratitude and appreciation for their work.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.