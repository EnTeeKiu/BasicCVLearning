# Example Day Outline

Use this outline when drafting a new day.

```text
# DD.MM - Topic

**Notebook type:** Practice notebook with theory, exercises, TODO cells, and test cases.

**Daily output:** ...

Short topic intro.
```

```text
## Core Ideas

Explain the essential concepts from the masterplan row.
```

```python
# setup/imports
import random
import numpy as np

SEED = 42
random.seed(SEED)
np.random.seed(SEED)
```

```text
## Prepared Image Data

Generate deterministic toy data here when the day needs custom data.
```

```python
def make_demo_images(...):
    # Complete provided helper, not a TODO.
    ...

X, y = make_demo_images(...)
```

```text
## Exercise DD-A: Name

Clear task description.
```

```python
# TODO DD-A
def required_function(...):
    raise NotImplementedError
```

```text
## Test Cases

Run this cell after completing the TODO cells above. A correct implementation should print `Day DD tests passed`.
```

```python
def run_dayDD_tests():
    assert "required_function" in globals(), "Missing function: required_function"
    # deterministic checks here
    print("Day DD tests passed")

run_dayDD_tests()
```

```text
## Day DD Checklist

Checklist items for the day.
```
