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
import os
import numpy as np
import torch

SEED = 42
np.random.seed(SEED)
torch.manual_seed(SEED)
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


# Smoke check: run this after implementing the function above.
smoke_result = required_function(...)
print("smoke check:", smoke_result)
```

The solution notebook uses the same smoke-check lines with the completed function. The smoke check must execute the implementation in its own exercise cell; the final day tests provide broader verification afterward.

For a function that compares training decisions, keep a tiny call only as an explicitly labeled structural smoke check. Then run the decision experiment on the complete prepared split in the same cell and print split sizes, validation class support, the main metric, per-class metrics, and delta from the baseline. Keep compared runs aligned on initialization, epochs, and observations per epoch.

```text
## Test Cases

Run this cell after completing the TODO cells above. A correct implementation should print `Day DD tests passed`.
```

```python
def run_dayDD_tests():
    assert "required_function" in globals(), "Missing function: required_function"
    # deterministic checks here
    # For training comparisons, verify the full validation set is represented,
    # then print the already-computed full-split evidence table.
    print("Day DD tests passed")

run_dayDD_tests()
```

```text
## Day DD Checklist

Checklist items for the day.
```
