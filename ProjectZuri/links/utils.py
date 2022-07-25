from uuid import uuid4


def generate_random_id():
    """
    A function to generate a random 8 character string.
    Useful for creating ranom Ids for URLs and objects
    """
    id = str(uuid4())
    # slicing to give first 8 Characters
    id = id[:8]
    return id
