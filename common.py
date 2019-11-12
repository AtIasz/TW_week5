import random

def generate_random(table):
    """
    Generates random and unique string. Used for id/key generation:
         - at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letter
         - it must be unique in the table (first value in every row is the id)

    Args:
        table (list): Data table to work on. First columns containing the keys.

    Returns:
        string: Random and unique string
    """

    generated = []

    SPECIAL_CHARACTERS = "!@#$%^&*()-+={[]}:./,<>"
    LOWERCASE = "qwertyuiopasdfghjklzxcvbnm"
    UPPERCASE = "QWERTYUIOPASDFGHJKLZXCVBNM"
    NUMBERS = "1234567890"

    random_special_characters = random.choice(SPECIAL_CHARACTERS)
    random_lowercase = random.choice(LOWERCASE)
    random_uppercase = random.choice(UPPERCASE)
    random_numbers = random.choice(NUMBERS)
    random_special_characters2 = random.choice(SPECIAL_CHARACTERS)
    random_lowercase2 = random.choice(LOWERCASE)
    random_uppercase2 = random.choice(UPPERCASE)
    random_numbers2 = random.choice(NUMBERS)

    generated.append(random_lowercase)
    generated.append(random_numbers)
    generated.append(random_special_characters)
    generated.append(random_uppercase)
    generated.append(random_lowercase2)
    generated.append(random_numbers2)
    generated.append(random_special_characters2)
    generated.append(random_uppercase2)

    final_result = ''.join(generated)

    return final_result