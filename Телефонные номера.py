import numpy as np
from typing import List

def clean_phone_number(phone_number: str) -> str:
    cleaned_number = phone_number.replace('-', '').replace('(', '').replace(')', '')
    return cleaned_number

def normalize_phone_numbers(phone_numbers: List[str]) -> np.ndarray:

    cleaned_numbers = []
    for phone_number in phone_numbers:
      cleaned_numbers.append(clean_phone_number(phone_number))
    cleaned_numbers_arr = np.array(cleaned_numbers)


    lengths = []
    for number in cleaned_numbers_arr:
      lengths.append(len(number))
    lengths_arr = np.array(lengths)
    
    for i, length in enumerate(lengths_arr):
        if length == 7:
            cleaned_numbers_arr[i] = '+7495' + cleaned_numbers_arr[i]
        elif length == 11 and cleaned_numbers_arr[i].startswith('8'):
           cleaned_numbers_arr[i] = cleaned_numbers_arr[i].replace('8', '+7', 1)


    return cleaned_numbers_arr

def compare_phone_numbers(normalized_numbers: np.ndarray) -> List[str]:
    comparison_result = []
    if not normalized_numbers.size:
        return comparison_result
    first_number = normalized_numbers[0]
    for number in normalized_numbers[1:]:
        if number == first_number:
            comparison_result.append('YES')
        else:
            comparison_result.append('NO')
    return comparison_result
    


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