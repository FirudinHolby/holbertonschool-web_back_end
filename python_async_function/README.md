python_async_function

Simple asyncio exercises used in the back-end curriculum.

Files
- `0-basic_async_syntax.py`: provides `wait_random(max_delay)`.
- `1-concurrent_coroutines.py`: defines `wait_n(n, max_delay)` and a
	small CLI to run the coroutine and print results.

Usage
Run the example script from the repository root:

```bash
python python_async_function/1-concurrent_coroutines.py [n] [max_delay]
```

If no arguments are provided, the script defaults to `n=5` and `max_delay=3`.