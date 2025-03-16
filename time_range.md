# Working `--range` arguments

The `--range` arguments should not exceed 7 days. Here are some working examples:

- `--range "last 6 days"`
- `--range "last 0 days"`
- `--range "last 23 hours"`

# Working `--start` and `--end` examples

- `--end "2025-03-16T07:00:00.000Z"`
- `--start "2025-03-16T07:00:00.000Z"`
- `--start "-7d"`
- `--start "-1w"`

# Python Code for Time Format

```python
from datetime import datetime, timezone

# Get the current UTC time in the required format
timestamp = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + 'Z'

print(timestamp)
```



# Giving guidance
```
Today is 16Mar2025 09:00 AM GMT+2
timestamp = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + 'Z'`
```