import random

LOCATIONS = [
    'Location 1',
    'Location 2',
    'Location 3',
    'Location 4',
    'Location 5',
    'Location 6',
    'Location 7',
    'Location 8',
    'Location 9',
    'Location 10',
    'Location 11',
    'Location 12',
]

start_message = (
    "\nStarting location: \n"
    "------------------\n"
    "  {}\n\n"
)

ending_message = (
    "Ending location: \n"
    "----------------\n"
    "  {}\n"
)

stop_message = (
    "Stop location # {}: \n"
    "------------------\n"
    "  {}\n\n"
)


def get_sphero_path(start=None, ending=None):
    """
    """
    n_stops = input("\nHow many stops? ")
    n_stops = int(n_stops)

    locations = []

    # Message to build.
    message = ""

    # Starting location
    if start is None:
        start = random.choice(LOCATIONS)

    elif start not in LOCATIONS:
        raise Exception("Starting location is not known.")

    # Add to message
    message += start_message.format(start)

    # Save start
    locations.append(start)

    # Add stops.
    for i in range(n_stops):

        # Get a stop
        z = 0
        while True:
            stop = random.choice(LOCATIONS)

            # Check that stop hasn't be used yet
            if stop not in locations or z > 10:
                break
            z += 1

        # Add to message
        message += stop_message.format(i+1, stop)

        # Save start
        locations.append(stop)

    # Starting location
    if ending is None:

        # Get a stop
        z = 0
        while True:
            ending = random.choice(LOCATIONS)

            # Check that stop hasn't be used yet
            if ending not in locations or z > 10:
                break
            z += 1

    elif ending not in LOCATIONS:
        raise Exception("Ending location is not known.")

    # Add to message
    message += ending_message.format(ending)

    print(message)
