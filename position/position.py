









def start_module():

    ui.print_menu(title, options)


def create_position():
    """
    Create “Position”
    Users can create new positions. A position has an ID, description, number of seats and a “Company ID”.
    Position IDs are unique amongst other positions.
    Descriptions cannot be empty.
    The number of seats must be greater than 0.
    Company ID must exist.
    """
    pass
def read_position():
    pass
    """
    Read “Position”
    Users can show the details of existing positions by entering their ID.
    “Students” already applied are shown here.
    """
    pass
def read_positions():
    """
    Read “Positions”
    Users can list existing positions. All attributes of a position are visible plus it’s displayed how many seats are already taken (e.g 2/1, one out of two seats are taken).
    """
    pass
def update_position():
    """
    Update “Position”
    Users can update the details of existing positions by first entering their ID and then the information needs to be updated.
    Only the description can be updated, nothing else.
    """
    pass
def delete_position():
    """
    Delete “Position”
    Users can delete existing positions by entering their ID.
    Positions cannot be deleted if they have an existing “Application”.
    """
    pass