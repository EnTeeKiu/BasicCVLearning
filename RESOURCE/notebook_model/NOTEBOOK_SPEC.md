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
  _dayDD_image_data/
```

Use relative paths so notebooks run from inside their own folder.
For synthetic image/video/audio fixtures, the prepared-data cell should write the actual files into that local day folder, plus any CSV/metadata needed to reload them. For image classification, mirror the Day 07 pattern: `_dayDD_image_data/images/*.png` and `_dayDD_image_data/labels.csv` with relative `image_path,label` rows.

## Practice Notebook Template

Recommended cell order:

1. Markdown title and purpose
2. Markdown theory overview
3. Code setup/imports
4. Markdown `## Prepared Data` or `## Prepared Image Data` when toy/custom data is needed
5. Code cell that generates deterministic toy/custom data
6. Markdown exercise A
7. Code TODO A
8. Markdown exercise B
9. Code TODO B
10. Continue for 3-6 exercises
11. Markdown `## Test Cases`
12. Code `run_dayDD_tests()`
13. Markdown checklist

Practice code cells should use clear TODO comments and `raise NotImplementedError` where the learner must fill code.

Do not make the learner implement custom data generation. If the notebook needs synthetic images, videos, text, or labels, provide that generator in a normal runnable cell before the exercises. Exercises may ask the learner to inspect, batch, transform, model, train on, or evaluate that data.
When the generator represents file-based data, it must materialize the files on disk before the exercises, not only return tensors in memory.

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
- Use toy data for repeatability, and provide its generation code outside TODO cells.
- If toy data is file-based, save the generated artifacts under the day folder and include tests that check the expected folder/metadata files exist.
- Use deterministic seeds.
- Avoid hidden magic in tests.
- Do not add random end-of-notebook bonus exercises unless they follow the same exercise + solution + test style.

## Validation Commands

Compile notebooks:

```powershell
python -c "import json,pathlib; files=sorted(pathlib.Path('.').glob('DD.MM/*.ipynb')); [compile((c['source'] if isinstance(c['source'], str) else ''.join(c['source'])), str(p), 'exec') for p in files for c in json.loads(p.read_text(encoding='utf-8'))['cells'] if c['cell_type']=='code']; print('ok')"
```

Execute a solution notebook manually by reading each code cell in order, or open it in Jupyter and run all.
