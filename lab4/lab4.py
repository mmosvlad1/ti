import random
from decimal import Decimal, getcontext


def build_arithmetic_code(sequence, numb, prob):
    getcontext().prec = 100
    cumulative_probabilities = [sum(prob[:i]) for i in range(len(prob) + 1)]

    low = Decimal(0)
    high = Decimal(1)

    for symbol in sequence:
        index = numb.index(symbol)
        range_size = high - low
        high = low + range_size * cumulative_probabilities[index + 1]
        low = low + range_size * cumulative_probabilities[index]

    return (high + low) / 2


def decode_arithmetic_code(encoded_value, numb, prob, k):
    getcontext().prec = 100
    cumulative_probabilities = [sum(prob[:i]) for i in range(len(prob) + 1)]

    value = Decimal(encoded_value)
    result = []
    for _ in range(k):
        for i in range(len(prob)):
            if cumulative_probabilities[i] <= value < cumulative_probabilities[i + 1]:
                result.append(numb[i])
                range_size = cumulative_probabilities[i + 1] - cumulative_probabilities[i]
                value = (value - cumulative_probabilities[i]) / range_size
                break

    return result


if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    probabilities = [Decimal('0.11'), Decimal('0.10'), Decimal('0.11'), Decimal('0.12'), Decimal('0.07'),
                     Decimal('0.08'),
                     Decimal('0.09'), Decimal('0.11'), Decimal('0.12'), Decimal('0.09')]

    letters = ['m', 'o', 's', 'k', 'a', 'l', ' ', 'v', 'd', 'y', 'n', 'r', 'i', 'c', 'h']
    letters_probabilities = [Decimal('0.03571428571428571230317317031222046352922916412353515625'),
                             Decimal('0.0714285714285714246063463406244409270584583282470703125'),
                             Decimal('0.0714285714285714246063463406244409270584583282470703125'),
                             Decimal('0.03571428571428571230317317031222046352922916412353515625'),
                             Decimal('0.142857142857142849212692681248881854116916656494140625'),
                             Decimal('0.10714285714285713690951951093666139058768749237060546875'),
                             Decimal('0.0714285714285714246063463406244409270584583282470703125'),
                             Decimal('0.10714285714285713690951951093666139058768749237060546875'),
                             Decimal('0.0714285714285714246063463406244409270584583282470703125'),
                             Decimal('0.10714285714285713690951951093666139058768749237060546875'),
                             Decimal('0.03571428571428571230317317031222046352922916412353515625'),
                             Decimal('0.03571428571428571230317317031222046352922916412353515625'),
                             Decimal('0.03571428571428571230317317031222046352922916412353515625'),
                             Decimal('0.03571428571428571230317317031222046352922916412353515625'),
                             Decimal('0.03571428571428571230317317031222046352922916412353515625')]

    sequence_1 = random.choices(numbers, list(map(float, probabilities)), k=5)
    sequence_2 = random.choices(numbers, list(map(float, probabilities)), k=10)
    sequence_3 = 'moskal vladyslav andriyovych'

    arithmetic_code_1 = build_arithmetic_code(sequence_1, numbers, probabilities)
    arithmetic_code_2 = build_arithmetic_code(sequence_2, numbers, probabilities)
    arithmetic_code_3 = build_arithmetic_code(sequence_3, letters, letters_probabilities)

    decoded_sequence_1 = decode_arithmetic_code(arithmetic_code_1, numbers, probabilities, k=5)
    decoded_sequence_2 = decode_arithmetic_code(arithmetic_code_2, numbers, probabilities, k=10)
    decoded_sequence_3 = decode_arithmetic_code(arithmetic_code_3, letters, letters_probabilities, k=len(sequence_3))

    print(f"Sequence 1: {sequence_1}")
    print(f"Sequence 2: {sequence_2}")
    print(f"Sequence 3: {sequence_3}")

    print(f"Arithmetic code for the sequence 1 is: {arithmetic_code_1}")
    print(f"Arithmetic code for the sequence 2 is: {arithmetic_code_2}")
    print(f"Arithmetic code for the sequence 3 is: {arithmetic_code_3}")

    print(f"Decoded sequence 1 is: {decoded_sequence_1}")
    print(f"Decoded sequence 2 is: {decoded_sequence_2}")
    print(f"Decoded sequence 3 is: {decoded_sequence_3}")
