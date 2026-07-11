# Future Agent Prompt

Copy this into a future session when asking an agent to continue the study notebooks.

```text
You are working in the BasicCVLearning repository.

Please create study notebooks for the requested OLP AI masterplan day(s).

Before creating notebooks:
- Read `[OLP AI] Masterplan - Tu's Plan.csv`.
- Read `notebook_model/README.md`.
- Read `notebook_model/NOTEBOOK_SPEC.md`.

For each requested day:
- Create a folder named `DD.MM` if it does not exist.
- Create `DD.MM/DD.MM.ipynb` as the practice notebook.
- Create `DD.MM/DD.MM_solution.ipynb` as the full solution notebook.
- Follow the existing notebook style from `08.07` and `09.07`.
- Include theory, named exercise sections, TODO code cells, solution code cells, test cases, and a final checklist.
- Keep the notebook self-contained with toy data when possible.
- When toy/custom image data is needed, include a ready-to-run data-generation cell before exercises; do not make the learner implement the data generator.
- Do not add unstructured final `## Exercises` sections.
- Add `## Test Cases` cells to both notebooks.
- Make the solution notebook pass its tests.
- Compile all new notebook code cells.
- Execute solution notebooks if dependencies are available.
- Do not touch unrelated day folders unless explicitly requested.

If the user asks to push:
- Stage only the requested new/changed day folders.
- Commit with a clear message.
- Push to `origin/main`.
```

## Short Version

```text
Use `notebook_model/README.md` and `notebook_model/NOTEBOOK_SPEC.md` as the notebook-generation contract. Continue from the masterplan CSV. Create practice + solution notebooks with test cells, validate them, and only stage requested day folders.
```
