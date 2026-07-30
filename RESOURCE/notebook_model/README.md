# Notebook Model

This folder is the handoff guide for future agents that create OLP AI study notebooks.

Use it when a new session needs to continue the study plan without reading old chat history. The source of truth for topics is still the root CSV:

`[OLP AI] Masterplan - Tu's Plan.csv`

The source of truth for allowed notebook libraries is:

`RESOURCE/library.png`

Future notebooks must use only the libraries listed there. Current allowed libraries are:

- Machine learning / NLP: `torch`, `tensorflow`, `scikit-learn`, `xgboost`, `catboost`, `transformers`, `spacy`, `nltk`, `gensim`, `fasttext`
- Data processing: `pandas`, `numpy`, `scipy`, `csv`, `json`, `pickle`
- Image processing: `opencv-python`, `Pillow`, `torchvision`, `scikit-image`
- Visualization: `matplotlib`, `seaborn`, `plotly`, `autoviz`
- Utilities: `joblib`, `datasets`, `evaluate`, `os`, `sys`, `re`, `itertools`, `collections`, `time`, `pdb`, `pytorch-lightning`, `tensorboard`, `tqdm`

Do not import unlisted helpers such as `pathlib`, `random`, or `math` in generated notebooks unless `RESOURCE/library.png` is updated.

## Goal

For each study day, create a folder named with a two-digit study-order prefix plus that day's notebook topic title, not just by date. Use the title text after the `DD.MM - ` prefix and sanitize characters that are invalid in Windows paths. For example:

`08 - Optimization for CV/`

Keep notebook filenames date-based inside the topic folder:

- `08 - Optimization for CV/10.07.ipynb` - practice notebook with theory, TODO exercises, and test cases
- `08 - Optimization for CV/10.07_solution.ipynb` - full working solution notebook with the same test cases

Example sanitization: the topic `Image I/O for CV` should use the folder `03 - Image IO for CV/`.

Do not rename older notebook files unless the user asks. Some earlier topic folders have extra files such as `*_practicing.ipynb` or `*_clean_exercises.ipynb`; preserve them.

## Required Notebook Shape

Every new practice notebook should include:

1. Title cell: `# DD.MM - Topic`
2. Notebook type line: practice notebook with theory, exercises, TODO cells, and test cases
3. Daily output copied or adapted from the masterplan
4. Theory cells explaining the core ideas
5. Setup/import cell using only libraries allowed by `RESOURCE/library.png`
6. Prepared data-generation cell when custom/toy data is needed
7. Numbered exercise sections like `## Exercise 10-A: ...`
8. TODO code cells for the learner to complete
9. `## Test Cases` markdown cell
10. Runnable test code cell with assertions and a clear pass message
11. `## Day DD Checklist`

Every solution notebook should:

- Mirror the practice notebook structure
- Replace TODO code with complete working code
- Include the same test cases
- Pass its test cases when executed in order

## Style Rules

- Keep notebooks self-contained. Generate toy data locally when possible.
- Follow a library-first teaching policy. When an allowed library already provides the production-standard operation, teach the learner to select, configure, apply, and interpret that API. Do not make the learner reimplement standard splitters, metrics, transforms, samplers, or similar utilities unless understanding that algorithm's internals is the explicit topic for the day.
- Explain important API semantics and tradeoffs alongside usage. For example, distinguish a stratified split, which preserves class proportions, from exact class balancing, which may require under/oversampling and changes the sampled distribution.
- For ordinary imbalanced classification, default to a stratified original-data split, keep validation untouched, and address training imbalance with an allowed sampler or class-weighted loss. Do not duplicate validation observations to make its class counts equal.
- If custom image/data fixtures are needed, provide a ready-to-run generation cell before the exercises. The learner should not be responsible for coding synthetic data generators.
- For file-based toy data, the generation cell must write the artifacts into the day folder. For image datasets, use a local pattern like `_dayDD_image_data/images/*.png` plus `_dayDD_image_data/labels.csv`, and keep paths relative to the notebook folder.
- Avoid required internet downloads.
- Use allowed libraries directly when they fit the topic. For CV transforms and models, `torchvision` is allowed; do not replace it with custom fallback transform/model helpers just because a local environment might be missing it.
- If an allowed dependency is missing during validation, report that clearly instead of adding unapproved fallback libraries or broad compatibility layers.
- Avoid final unstructured `## Exercises` sections. Exercises should appear as named sections with matching TODO or solution cells.
- Do not leave learner-implemented functions or classes as definition-only cells. At the bottom of each exercise code cell, add a clearly labeled smoke check that calls the newly implemented API with prepared data and prints, displays, or asserts a meaningful result. In a practice notebook, the smoke check may fail with `NotImplementedError` until the TODO is completed; after completion, the same cell must exercise the learner's code immediately.
- Use assertion-based tests so the learner can verify their work.
- Prefer small, fast examples over big datasets.
- For CV notebooks, always check shape, dtype, device, and label mapping where relevant.

## Validation Checklist

Before committing new notebooks:

- Compile every code cell as Python.
- Execute the solution notebook if dependencies are available.
- Confirm the test cell prints `Day DD tests passed`.
- Confirm generated file-based fixtures exist on disk when the notebook relies on them.
- Confirm practice notebooks contain TODOs and solution notebooks contain full code.
- Confirm every learner-implementation cell includes and runs an immediate smoke check; final test cells are additional verification and do not replace per-cell calls.
- Confirm no unrelated files are staged.

## Git Workflow

When committing generated notebooks:

1. Run `git status --short --branch`.
2. Stage only the requested day folders.
3. Commit with a message like `Add study notebooks for day 10`.
4. Push to `origin/main` if the user asks or the session is already following the push workflow.
