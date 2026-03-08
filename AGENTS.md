# About Me Data

A structured personal data repository that stores and validates "about me" information using JSON files and Pydantic models.

## Project Structure

- **JSON data files** (`education.json`, `experience.json`, `open-source.json`, `personal.json`, `projects.json`) — Each file holds a specific category of personal/professional data (education history, work experience, open-source contributions, personal info, and projects).
- **`data_types.py`** — Defines Pydantic models (e.g., `EducationData`, `ExperienceItem`, `PersonalData`, `ProjectItem`) that describe and validate the shape of each JSON data file.
- **`dataTypes.ts`** — TypeScript equivalents of the Pydantic models, providing type definitions for consuming the JSON data in a TypeScript/JavaScript context.
- When defining python types, use modern type hints. Use `list` instead of `List`, `dict` instead of `Dict`, `str|None` instead of `Optional[str]`, etc.
- Always make sure files do not contain any syntax errors or linting issues.
