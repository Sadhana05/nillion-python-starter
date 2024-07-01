from nada_dsl import *


def nada_main():
    party1 = Party(name="Party1")
    my_int1 = SecretInteger(Input(name="my_int1", party=party1))
    my_int2 = SecretInteger(Input(name="my_int2", party=party1))

    # Perform a computation using my_int1 and my_int2, e.g., multiplication
    result = my_int1 * my_int2

    # Return the result as output
    return [Output(result, "product_output", party1)]


create_new_nada_program_by_reference(nada_main)
