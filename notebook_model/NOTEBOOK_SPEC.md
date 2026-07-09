# Notebook Generation Spec

This is the detailed pattern future agents should follow.

## Source Of Truth

Read the root masterplan CSV row for the target date. Extract:

- `Date`
- `Focus`
- `Study (Theory / hard knowledge)`
- `Do (Practice / coding from scratch)`
- `Daily output / evidence`
- `Priority`
- `Notes`

If the user types a date that looks inconsistent with the plan, infer cautiously and state it. Example: if the user asks for `08.08` but the sequence and CSV show `08/07/2026`, create `08.07` and mention the assumption.

## Folder And File Naming

For new days, use:

```text
DD.MM/
  DD.MM.ipynb
  DD.MM_solution.ipynb
```

Only create additional data folders if the notebook needs local toy data:

```text
DD.MM/
  _dayDD_demo_data/
```

Use relative paths so notebooks run from inside their own folder.

## Practice Notebook Template

Recommended cell order:

1. Markdown title and purpose
2. Markdown theory overview
3. Code setup/imports
4. Markdown exercise A
5. Code TODO A
6. Markdown exercise B
7. Code TODO B
8. Continue for 3-6 exercises
9. Markdown `## Test Cases`
10. Code `run_dayDD_tests()`
11. Markdown checklist

Practice code cells should use clear TODO comments and `raise NotImplementedError` where the learner must fill code.

## Solution Notebook Template

Use the same markdown as the practice notebook, but replace TODO cells with complete implementations.

The solution notebook should be executable top-to-bottom. If a dependency is missing, skip optional checks gracefully; do not crash for optional visualization.

## Test Cell Requirements

Test cells should:

- Be in both practice and solution notebooks
- Define `run_dayDD_tests()`
- Check required functions/classes exist
- Check shapes, dtypes, label values, and output keys
- Use small deterministic examples
- Print exactly: `Day DD tests passed`

If PyTorch is required and missing, the test may print a clear skip message. If the notebook topic is pure math or NumPy, tests should run without PyTorch.

Example:

```python
def run_day10_tests():
    assert "my_function" in globals(), "Missing function: my_function"
    result = my_function(...)
    assert result.shape == expected_shape
    print("Day 10 tests passed")

run_day10_tests()
```

## Dependency Policy

Prefer standard library, NumPy, PIL, and PyTorch. Avoid new dependencies unless the topic requires them.

When using optional packages:

```python
try:
    import torch
    TORCH_AVAILABLE = True
except ImportError:
    torch = None
    TORCH_AVAILABLE = False
    print("PyTorch is not installed. Optional PyTorch cells will be skipped.")
```

## Content Quality Rules

- Explain enough theory for the learner to solve the exercise.
- Keep exercises scoped and testable.
- Use toy data for repeatability.
- Use deterministic seeds.
- Avoid hidden magic in tests.
- Do not add random end-of-notebook bonus exercises unless they follow the same exercise + solution + test style.

## Validation Commands

Compile notebooks:

```powershell
python -c "import json,pathlib; files=sorted(pathlib.Path('.').glob('DD.MM/*.ipynb')); [compile((c['source'] if isinstance(c['source'], str) else ''.join(c['source'])), str(p), 'exec') for p in files for c in json.loads(p.read_text(encoding='utf-8'))['cells'] if c['cell_type']=='code']; print('ok')"
```

Execute a solution notebook manually by reading each code cell in order, or open it in Jupyter and run all.

