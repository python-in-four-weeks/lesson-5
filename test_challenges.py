import pytest

import challenges


@pytest.mark.parametrize(
    "numbers, expected_numbers_over_50",
    [
        ([], []),
        ([70], [70]),
        ([-10, 50, 100, -1000], [100]),
        ([45, 67, 65, 43], [67, 65]),
    ],
)
def test_get_numbers_over_50_v1(
    numbers: list[int], expected_numbers_over_50: list[int]
) -> None:
    numbers_over_50 = challenges.get_numbers_over_50_v1(numbers)
    assert (
        numbers_over_50 == expected_numbers_over_50
    ), f"The numbers over 50 should be {expected_numbers_over_50}"


@pytest.mark.parametrize(
    "numbers, expected_numbers_over_50",
    [
        ([], []),
        ([70], [70]),
        ([-10, 50, 100, -1000], [100]),
        ([45, 67, 65, 43], [67, 65]),
    ],
)
def test_get_numbers_over_50_v2(
    numbers: list[int], expected_numbers_over_50: list[int]
) -> None:
    numbers_over_50 = challenges.get_numbers_over_50_v2(numbers)
    assert (
        numbers_over_50 == expected_numbers_over_50
    ), f"The numbers over 50 should be {expected_numbers_over_50}"


@pytest.mark.parametrize(
    "words, expected_words_under_5_characters",
    [
        ([], []),
        (["the"], ["the"]),
        (["a", "nice", "banana"], ["a", "nice"]),
        (
            ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"],
            ["the", "fox", "over", "the", "lazy", "dog"],
        ),
    ],
)
def test_get_words_under_5_characters_v1(
    words: list[str], expected_words_under_5_characters: list[str]
) -> None:
    words_under_5_characters = challenges.get_words_under_5_characters_v1(words)
    assert (
        words_under_5_characters == expected_words_under_5_characters
    ), f"The words under 5 characters should be {expected_words_under_5_characters}"


@pytest.mark.parametrize(
    "words, expected_words_under_5_characters",
    [
        ([], []),
        (["the"], ["the"]),
        (["a", "nice", "banana"], ["a", "nice"]),
        (
            ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"],
            ["the", "fox", "over", "the", "lazy", "dog"],
        ),
    ],
)
def test_get_words_under_5_characters_v2(
    words: list[str], expected_words_under_5_characters: list[str]
) -> None:
    words_under_5_characters = challenges.get_words_under_5_characters_v2(words)
    assert (
        words_under_5_characters == expected_words_under_5_characters
    ), f"The words under 5 characters should be {expected_words_under_5_characters}"


@pytest.mark.parametrize(
    "people, expected_names",
    [
        ([], []),
        ([{"name": "Sally"}], ["Sally"]),
        (
            [
                {"name": "Sally", "age": 24},
                {"name": "Susan", "age": 30},
                {"name": "Saira", "age": 28},
            ],
            ["Sally", "Susan", "Saira"],
        ),
        (
            [
                {"name": "Sally", "age": 24, "country": "UK"},
                {"name": "Susan", "age": 30, "country": "US"},
            ],
            ["Sally", "Susan"],
        ),
    ],
)
def test_get_names_v1(people: list[dict], expected_names: list[str]) -> None:
    names = challenges.get_names_v1(people)
    assert names == expected_names, f"The names should be {expected_names}"


@pytest.mark.parametrize(
    "people, expected_names",
    [
        ([], []),
        ([{"name": "Sally"}], ["Sally"]),
        (
            [
                {"name": "Sally", "age": 24},
                {"name": "Susan", "age": 30},
                {"name": "Saira", "age": 28},
            ],
            ["Sally", "Susan", "Saira"],
        ),
        (
            [
                {"name": "Sally", "age": 24, "country": "UK"},
                {"name": "Susan", "age": 30, "country": "US"},
            ],
            ["Sally", "Susan"],
        ),
    ],
)
def test_get_names_v2(people: list[dict], expected_names: list[str]) -> None:
    names = challenges.get_names_v2(people)
    assert names == expected_names, f"The names should be {expected_names}"


@pytest.mark.parametrize(
    "numbers, expected_doubled_numbers",
    [
        ([], []),
        ([25], [50]),
        ([3, 1, 6, 7], [6, 2, 12, 14]),
        ([-21, -34, 97, 0, 35, -8, 10], [-42, -68, 194, 0, 70, -16, 20]),
    ],
)
def test_double_numbers_v1(
    numbers: list[int], expected_doubled_numbers: list[int]
) -> None:
    doubled_numbers = challenges.double_numbers_v1(numbers)
    assert (
        doubled_numbers == expected_doubled_numbers
    ), f"The doubled numbers should be {expected_doubled_numbers}"


@pytest.mark.parametrize(
    "numbers, expected_doubled_numbers",
    [
        ([], []),
        ([25], [50]),
        ([3, 1, 6, 7], [6, 2, 12, 14]),
        ([-21, -34, 97, 0, 35, -8, 10], [-42, -68, 194, 0, 70, -16, 20]),
    ],
)
def test_double_numbers_v2(
    numbers: list[int], expected_doubled_numbers: list[int]
) -> None:
    doubled_numbers = challenges.double_numbers_v2(numbers)
    assert (
        doubled_numbers == expected_doubled_numbers
    ), f"The doubled numbers should be {expected_doubled_numbers}"


@pytest.mark.parametrize(
    "string_to_split",
    [
        "",
        "   ",
        "banana",
        " split ",
        "I like banana splits",
        "   I   am   very      spaced  out ",
    ],
)
def test_string_split(string_to_split: str) -> None:
    expected_split_strings = string_to_split.split()
    split_strings = challenges.string_split(string_to_split)
    assert (
        split_strings == expected_split_strings
    ), f"The list of strings after splitting should be {expected_split_strings}"


@pytest.mark.parametrize(
    "separator, strings_to_join",
    [
        (" ", []),
        (" ", ["bananas"]),
        (" and ", ["apples", "oranges"]),
        (", ", ["strawberries", "raspberries", "blackberries"]),
    ],
)
def test_string_join(separator: str, strings_to_join: list[str]) -> None:
    expected_joined_string = separator.join(strings_to_join)
    joined_string = challenges.string_join(separator, strings_to_join)
    assert (
        joined_string == expected_joined_string
    ), f"The string after joining should be {expected_joined_string}"


@pytest.mark.parametrize(
    "items",
    [
        [],
        [22.5],
        ["hello", "there"],
        [3, 1, 6, 7],
    ],
)
def test_list_reverse(items: list) -> None:
    expected_reversed_items = list(reversed(items))
    reversed_items = challenges.list_reverse(items)
    assert (
        reversed_items == expected_reversed_items
    ), f"The list after reversal should be {expected_reversed_items}"


@pytest.mark.parametrize(
    "items_1, items_2",
    [
        (set(), set()),
        ({10, 20}, {10, 20}),
        ({10, 20, 30, 40}, {30}),
        ({10, 20, 30, 40}, {50, 60}),
    ],
)
def test_set_intersection(items_1: set, items_2: set) -> None:
    expected_intersection = items_1.intersection(items_2)
    intersection = challenges.set_intersection(items_1, items_2)
    assert (
        intersection == expected_intersection
    ), f"The intersection should be {expected_intersection}"
