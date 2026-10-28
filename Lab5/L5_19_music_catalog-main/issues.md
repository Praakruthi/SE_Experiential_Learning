# Static Code Analysis – Issue Report

## Project: Music Catalog and Playlist Manager

### 1. Objective

The objective of this analysis is to identify and fix code quality, security, and formatting issues in `music_catalog.py` using Pylint, Bandit, and Flake8. The tools were run before modifying the source code, and their reports were examined to identify issues requiring correction.

### 2. Identified Issues and Fixes

| Issue | Type | Line(s) | Description | Fix Approach |
|---|---|---|---|---|
| SQL query construction | Security – Medium | 10 | Bandit reported B608 because the SQL INSERT query is constructed using string formatting. This can expose the application to SQL injection and cause errors when input contains special characters. | Replace string-based query construction with a parameterized SQLite query using placeholders and a tuple of values. |
| Insecure deserialization using pickle | Security – Medium | 33 | Bandit reported B301 because `pickle.loads()` can execute malicious code when processing untrusted serialized data. | Replace pickle serialization and deserialization with JSON for playlist data, and handle invalid JSON input appropriately. |
| Pickle module import | Security – Low | 1 | Bandit reported B403 because importing the pickle module may introduce security risks when it is used to deserialize untrusted data. | Remove the pickle import after replacing pickle-based serialization with a safer format such as JSON. |
| Use of random module | Security – Low | 17 | Bandit reported B311 because standard pseudo-random generators are not suitable for cryptographic or security-sensitive purposes. | Confirm that random song selection is not security-sensitive. If it is only for ordinary catalog selection, document the intended use; otherwise, use an appropriate secure random generator. |
| Mutable default argument | Code Quality / Potential Bug | 9 | Pylint reported W0102 because `playlist=[]` is used as a default argument. The same list can be reused across function calls, causing unintended shared state. | Change the default argument to `None` and initialize a new list inside the function when no playlist is supplied. |
| Missing module docstring | Code Quality | 1 | Pylint reported C0114 because the Python module does not contain a module-level docstring describing its purpose. | Add a descriptive module docstring at the beginning of the file. |
| Missing function docstrings | Code Quality | 9, 15, 20, 28, 32, 36, 43 | Pylint reported C0116 because several functions do not have docstrings explaining their purpose. | Add concise docstrings describing the purpose, parameters, and return values of the functions where appropriate. |
| Function naming conventions | Code Quality / Style | 9, 15, 28, 32, 36 | Pylint reported C0103 for function names such as `addSong`, `shufflePick`, `savePlaylist`, `loadPlaylist`, and `totalPlays`. These names do not follow Python's snake_case convention. | Rename the functions to `add_song`, `shuffle_pick`, `save_playlist`, `load_playlist`, and `total_plays`, updating all corresponding function calls. |
| Broad exception handling | Code Quality / Style | 39 | Pylint reported W0702 and Flake8 reported E722 because the code uses a bare `except` clause. This can hide unexpected errors and make debugging difficult. | Catch the specific expected exception types or handle the empty database result directly where appropriate. |
| Long lines | Formatting | 6, 10, 21, 49 | Pylint reported C0301 for a line exceeding its configured limit, while Flake8 reported E501 for lines exceeding 79 characters. | Break long statements into multiple lines and use appropriate indentation to improve readability and satisfy the configured line-length limits. |
| Unnecessary else after return | Code Quality | 22 | Pylint reported R1705 because an `else` block follows a `return` statement. The `else` is unnecessary when the preceding branch already returns. | Remove the unnecessary `else` and de-indent the statements within that branch. |
| Unnecessary string formatting | Code Quality | 10 | Pylint reported C0209 because regular string formatting is used where an f-string may be appropriate. | Use an f-string when suitable for ordinary string formatting. For SQL queries, prioritize parameterized queries instead of f-strings or string interpolation. |
| Multiple statements on one line | Formatting | 48 | Pylint reported C0321 and Flake8 reported E701 because multiple statements appear on a single line. This reduces readability. | Place each statement on a separate line with proper indentation. |
| Ambiguous variable name | Code Quality / Style | 47 | Flake8 reported E741 because the variable name `l` is ambiguous and difficult to distinguish from the digit `1`. | Replace the variable with a descriptive name that communicates its purpose. |

### 3. Summary of Initial Analysis

#### Pylint

- Initial score: 4.57/10.
- Reported missing module and function docstrings.
- Identified inconsistent function naming, a mutable default argument, long lines, unnecessary string formatting, an unnecessary `else` after `return`, broad exception handling, and multiple statements on one line.

#### Bandit

Bandit reported four potential security issues:

- B608: Possible SQL injection through string-based query construction — Medium severity.
- B301: Potentially unsafe pickle deserialization — Medium severity.
- B403: Potential security implications associated with importing pickle — Low severity.
- B311: Use of a standard pseudo-random generator — Low severity.

The initial report contained two medium-severity findings, two low-severity findings, and no high-severity findings.

#### Flake8

Flake8 reported seven formatting and style violations:

- Four E501 long-line violations at lines 6, 10, 21, and 49.
- One E722 bare-except violation at line 39.
- One E741 ambiguous-variable-name violation at line 47.
- One E701 multiple-statements-on-one-line violation at line 48.

### 4. Verification After Fixing

After implementing the fixes, all three static analysis tools must be run again against the updated `music_catalog.py`.

The final reports should be checked to verify that the addressed issues no longer appear. The final Pylint score should be above 9.5/10, all Bandit findings should be reviewed and appropriately addressed, and the Flake8 formatting violations should be resolved.

The program should also be executed after the changes to verify that its music catalog and playlist functionality continue to work correctly.

### 5. Conclusion

Static code analysis helped identify potential security vulnerabilities, code quality problems, and formatting violations in the Music Catalog and Playlist Manager. Pylint provided feedback on code quality and maintainability, Bandit highlighted potentially insecure coding patterns, and Flake8 identified style violations. Addressing these findings improves readability, maintainability, and security while helping preserve the intended functionality of the program.

**Note:** The line numbers above refer to the original source code before modifications. They may change after the fixes are applied. The final status of each issue must be confirmed using the after-fix reports.
