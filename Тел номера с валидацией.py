import numpy as np
import re
from typing import List, Optional

def clean_phone_number(phone_number: str) -> str:
    return phone_number.replace('-', '').replace('(', '').replace(')', '')


def validate_phone_number(phone_number: str) -> bool:
    pattern = r'(\+7|8)?[\s-]*(\(?\d{3}\)?[\s-]*)?(\d[\s-]*){7,10}'
    return bool(re.fullmatch(pattern, phone_number))

def normalize_phone_numbers(phone_numbers: List[str]) -> np.ndarray:

    validated_numbers = [
        phone_number for phone_number in phone_numbers if validate_phone_number(phone_number)
    ]

    cleaned_numbers = np.array(tuple(map(clean_phone_number, validated_numbers)))

    lengths = np.array(tuple(map(len, cleaned_numbers)))

    is_7_digits = lengths == 7
    cleaned_numbers[is_7_digits] = '+7495' + cleaned_numbers[is_7_digits]

    is_11_digits = lengths == 11
    temp_11_digits = cleaned_numbers[is_11_digits]
    temp_11_digits = np.array(tuple(map(lambda x: x.replace('8', '+7', 1), temp_11_digits)))
    cleaned_numbers[is_11_digits] = temp_11_digits
    
    return cleaned_numbers


def compare_phone_numbers(normalized_numbers: np.ndarray) -> List[str]:

    if not normalized_numbers.size:
        return []

    comparison_result = tuple(
        map(lambda x: 'YES' if normalized_numbers[0] == x else 'NO', normalized_numbers[1:])
    )

    return list(comparison_result)


if __name__ == '__main__':
    phone_numbers = [
        '8(495)430-23-97',
        '+7-4-9-5-43-023-97',
        '4-3-0-2-3-9-7',
        '8-495-430',
        '8(918)5238495',
    ]

    normalized_numbers = normalize_phone_numbers(phone_numbers)
    comparison_results = compare_phone_numbers(normalized_numbers)

    print(*comparison_results, sep='\n')