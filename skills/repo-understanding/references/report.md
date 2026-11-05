# Repository Understanding Report

Use the following headings for a full onboarding report. Translate the headings to the user's language when appropriate. Keep each section as short as the evidence allows. The three status labels apply to findings, including individual cells or clauses that have different levels of certainty.

## 1. Project Overview
Give the project name, purpose and scope of inspection. Identify any packages or areas omitted.

## 2. Technology Stack
Identify languages, frameworks, package manager, runtime and build system from specific files.

## 3. Directory Structure
List the few source, config, test, docs and resource locations that explain how to navigate. Describe purposes you checked against file contents.

## 4. Architecture Overview
Trace one operation through concrete symbols and files. Explain what crosses each boundary and what the caller receives.

## 5. Important Modules
For each main module give its responsibility and a caller or consumer.

## 6. Main Entry Points
Connect each confirmed command, route or export to its target. Flag broken or unresolved links.

## 7. Dependencies
Separate runtime and development dependencies from internal ones. Explain the role of an important dependency where a call site supports it.

## 8. Development Commands
Cover install, run, build, test, lint and type-check. Group missing commands. Include working directory, available prerequisites and evidence. Distinguish a command found on disk from one actually executed.

## 9. Testing Strategy
Identify the test runner, how it discovers tests and one behavior actually asserted. Scope any coverage gap to the inspected tests.

## 10. Coding Conventions
Distinguish configured rules from patterns sampled in source and tests. Note relevant unknowns instead of generalizing from one example.

## 11. Potential Risks
Give evidence and a plausible consequence for each material risk.

## 12. Unknowns and Limitations
Name unresolved questions, sources omitted for safety and the limits of static inspection.

## 13. Recommended Next Steps
Suggest the next file, maintainer question or check tied to a finding. List any operation requiring separate permission without executing it.
