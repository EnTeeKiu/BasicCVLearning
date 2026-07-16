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

If the user types a date that looks inconsistent with the plan, infer cautiously and state it. Example: if the user asks for `08.08` but the sequence and CSV show `08/07/2026`, use the `08/07/2026` row and mention the assumption.

Also read `RESOURCE/library.png` before writing notebook code. It is the allowlist for imports inside generated notebooks.

## Folder And File Naming

For new days, name the top-level folder with a two-digit study-order prefix plus the topic title from the notebook H1, using the title text after `DD.MM - `. Sanitize characters that are invalid in Windows paths, such as `/`, `\`, `:`, `*`, `?`, `"`, `<`, `>`, and `|`.

Use date-based notebook filenames inside that numbered topic folder:

```text
NN - Topic Title/
  DD.MM.ipynb
  DD.MM_solution.ipynb
```

Example: `10.07 - Optimization for CV` lives in `08 - Optimization for CV/10.07.ipynb`.
Example sanitization: `05.07 - Image I/O for CV` lives in `03 - Image IO for CV/05.07.ipynb`.

Only create additional data folders if the notebook needs local toy data:

```text
NN - Topic Title/
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

Every learner-implementation cell must end with a clearly labeled `# Smoke check` block. That block must call every newly implemented function/class, or use one representative end-to-end call when the functions are intentionally interdependent, and print, display, or assert a result that proves the implementation body executed. Definition-only exercise cells are not allowed. In practice notebooks, running the unfinished cell may raise `NotImplementedError`; once the TODO is completed, rerunning that same cell must execute the smoke check successfully. A final day test cell complements these checks but does not replace them.

Do not make the learner implement custom data generation. If the notebook needs synthetic images, videos, text, or labels, provide that generator in a normal runnable cell before the exercises. Exercises may ask the learner to inspect, batch, transform, model, train on, or evaluate that data.
When the generator represents file-based data, it must materialize the files on disk before the exercises, not only return tensors in memory.

## Solution Notebook Template

Use the same markdown as the practice notebook, but replace TODO cells with complete implementations.

The solution notebook should be executable top-to-bottom in an environment with the allowed libraries installed. If a locally missing dependency prevents validation, report it clearly; do not add unapproved fallback imports or custom compatibility layers.

## Test Cell Requirements

Test cells should:

- Be in both practice and solution notebooks
- Define `run_dayDD_tests()`
- Check required functions/classes exist
- Check shapes, dtypes, label values, and output keys
- Use small deterministic examples
- Print exactly: `Day DD tests passed`

If a required allowed dependency is missing in the local validation environment, report that validation could not execute. If the notebook topic is pure NumPy/data processing, tests should run without PyTorch.

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

Use only the libraries allowed by `RESOURCE/library.png`.

Current allowed libraries:

- Machine learning / NLP: `torch`, `tensorflow`, `scikit-learn`, `xgboost`, `catboost`, `transformers`, `spacy`, `nltk`, `gensim`, `fasttext`
- Data processing: `pandas`, `numpy`, `scipy`, `csv`, `json`, `pickle`
- Image processing: `opencv-python`, `Pillow`, `torchvision`, `scikit-image`
- Visualization: `matplotlib`, `seaborn`, `plotly`, `autoviz`
- Utilities: `joblib`, `datasets`, `evaluate`, `os`, `sys`, `re`, `itertools`, `collections`, `time`, `pdb`, `pytorch-lightning`, `tensorboard`, `tqdm`

Avoid unlisted notebook imports such as `pathlib`, `random`, `math`, `typing`, or `dataclasses`. Use allowed equivalents: `os` for paths, `numpy.random` and `torch.manual_seed` for randomness, and basic arithmetic or `numpy` for simple numeric helpers.

For CV notebooks, `torchvision` is allowed. Use `torchvision.transforms` for standard image augmentation and `torchvision.models` for transfer-learning skeletons instead of creating local fallback transform/model systems.

## Content Quality Rules

- Explain enough theory for the learner to solve the exercise.
- Keep exercises scoped and testable.
- Use toy data for repeatability, and provide its generation code outside TODO cells.
- If toy data is file-based, save the generated artifacts under the day folder and include tests that check the expected folder/metadata files exist.
- Use deterministic seeds.
- Avoid hidden magic in tests.
- Exercise cells must demonstrate their code immediately with prepared inputs; do not defer the first function call to the final test cell or a later exercise.
- Do not add random end-of-notebook bonus exercises unless they follow the same exercise + solution + test style.

## Validation Commands

Compile notebooks:

```powershell
python -c "import json,os; folder='NN - Topic Title'; files=sorted(os.path.join(folder,f) for f in os.listdir(folder) if f.endswith('.ipynb')); [compile((c['source'] if isinstance(c['source'], str) else ''.join(c['source'])), p, 'exec') for p in files for c in json.loads(open(p, encoding='utf-8').read())['cells'] if c['cell_type']=='code']; print('ok')"
```

Execute a solution notebook manually by reading each code cell in order, or open it in Jupyter and run all.
