# Notebook Model

This folder is the handoff guide for future agents that create OLP AI study notebooks.

Use it when a new session needs to continue the study plan without reading old chat history. The source of truth for topics is still the root CSV:

`[OLP AI] Masterplan - Tu's Plan.csv`

## Goal

For each study day, create a folder named by date, for example:

`10.07/`

Preferred notebook pair for new days:

- `10.07/10.07.ipynb` - practice notebook with theory, TODO exercises, and test cases
- `10.07/10.07_solution.ipynb` - full working solution notebook with the same test cases

Do not rename older day files unless the user asks. Some earlier folders have extra files such as `*_practicing.ipynb` or `*_clean_exercises.ipynb`; preserve them.

## Required Notebook Shape

Every new practice notebook should include:

1. Title cell: `# DD.MM - Topic`
2. Notebook type line: practice notebook with theory, exercises, TODO cells, and test cases
3. Daily output copied or adapted from the masterplan
4. Theory cells explaining the core ideas
5. Setup/import cell with graceful dependency handling
6. Numbered exercise sections like `## Exercise 10-A: ...`
7. TODO code cells for the learner to complete
8. `## Test Cases` markdown cell
9. Runnable test code cell with assertions and a clear pass message
10. `## Day DD Checklist`

Every solution notebook should:

- Mirror the practice notebook structure
- Replace TODO code with complete working code
- Include the same test cases
- Pass its test cases when executed in order

## Style Rules

- Keep notebooks self-contained. Generate toy data locally when possible.
- Avoid required internet downloads.
- If PyTorch, OpenCV, matplotlib, or another package may be missing, handle that gracefully.
- Avoid final unstructured `## Exercises` sections. Exercises should appear as named sections with matching TODO or solution cells.
- Use assertion-based tests so the learner can verify their work.
- Prefer small, fast examples over big datasets.
- For CV notebooks, always check shape, dtype, device, and label mapping where relevant.

## Validation Checklist

Before committing new notebooks:

- Compile every code cell as Python.
- Execute the solution notebook if dependencies are available.
- Confirm the test cell prints `Day DD tests passed`.
- Confirm practice notebooks contain TODOs and solution notebooks contain full code.
- Confirm no unrelated files are staged.

## Git Workflow

When committing generated notebooks:

1. Run `git status --short --branch`.
2. Stage only the requested day folders.
3. Commit with a message like `Add study notebooks for day 10`.
4. Push to `origin/main` if the user asks or the session is already following the push workflow.

