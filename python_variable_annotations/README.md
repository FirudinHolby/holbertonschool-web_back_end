python_variable_annotations
===========================

Small utility functions demonstrating Python variable annotations.

Modules
-------

- `0-add.py`: `add(a: float, b: float) -> float` — Return the sum of two floats.
- `1-concat.py`: `concat(a: str, b: str) -> str` — Return the concatenation of two strings.
- `2-floor.py`: `floor(a: float) -> int` — Return the integer representation of a float by truncation.
- `3-to_str.py`: `to_str(a: float) -> str` — Convert a value to its string representation.
- `4-define_variables.py`: Demo file showing annotated variables of type `int`, `float`, `bool`, and `str`.
- `5-sum_list.py`: `sum_list(input_list: List[float]) -> float` — Return the sum of all float values in a list.
- `7-to_kv.py`: `to_kv(k: str, v: Union[int, float]) -> Tuple[str, Union[int, float]]` — Return a typed key-value tuple.

Usage
-----

Import functions and call them directly:

```python
from python_variable_annotations.0-add import add
from python_variable_annotations.1-concat import concat
from python_variable_annotations.2-floor import floor

print(add(1.2, 3.4))    # 4.6
print(concat('a', 'b'))  # 'ab'
print(floor(3.7))        # 3
```

Notes
-----

All functions include variable annotations for clarity and static type checking.
