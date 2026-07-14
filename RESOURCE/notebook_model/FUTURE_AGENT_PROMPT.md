# Future Agent Prompt

Copy this into a future session when asking an agent to continue the study notebooks.

```text
You are working in the BasicCVLearning repository.

Please create study notebooks for the requested OLP AI masterplan day(s).

Before creating notebooks:
- Read `[OLP AI] Masterplan - Tu's Plan.csv`.
- Read `RESOURCE/library.png` and use it as the import allowlist for notebook code.
- Read `notebook_model/README.md`.
- Read `notebook_model/NOTEBOOK_SPEC.md`.

For each requested day:
- Create a folder named with a two-digit study-order prefix plus the notebook topic title, not just the date. Use the title text after `DD.MM - ` and sanitize invalid Windows path characters, e.g. `Image I/O for CV` becomes `03 - Image IO for CV`.
- Create `NN - Topic Title/DD.MM.ipynb` as the practice notebook.
- Create `NN - Topic Title/DD.MM_solution.ipynb` as the full solution notebook.
- Follow the existing notebook style from `06 - CNN Fundamentals` and `07 - Small CNN Coding`.
- Include theory, named exercise sections, TODO code cells, solution code cells, test cases, and a final checklist.
- Use only libraries listed in `RESOURCE/library.png`; do not import unlisted helpers such as `pathlib`, `random`, or `math` in notebook code.
- For CV transforms/models, use allowed `torchvision` APIs directly when they fit the task.
- Keep the notebook self-contained with toy data when possible.
- When toy/custom image data is needed, include a ready-to-run data-generation cell before exercises; do not make the learner implement the data generator.
- If the toy data is file-based, write the generated files into the day folder, for example `_dayDD_image_data/images/*.png` plus `_dayDD_image_data/labels.csv`, and keep paths relative to the notebook folder.
- Do not add unstructured final `## Exercises` sections.
- Add `## Test Cases` cells to both notebooks.
- Make the solution notebook pass its tests.
- Compile all new notebook code cells.
- Execute solution notebooks if the allowed dependencies are available; if an allowed dependency is missing locally, report that instead of adding unapproved fallback code.
- Do not touch unrelated day folders unless explicitly requested.

If the user asks to push:
- Stage only the requested new/changed day folders.
- Commit with a clear message.
- Push to `origin/main`.
```

## Short Version

```text
Use `RESOURCE/library.png`, `notebook_model/README.md`, and `notebook_model/NOTEBOOK_SPEC.md` as the notebook-generation contract. Continue from the masterplan CSV. Create practice + solution notebooks with test cells, validate them, and only stage requested day folders.
```
