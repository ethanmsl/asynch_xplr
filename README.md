# Python Skeleton Repo
This is an *exploratory* skeleton repo for Python projects using both Poetry and either/both CircleCI or GitHub_Actions.
the `pyproject.toml` is pre-loaded with dev dependenceis used in the supplied pre-commit hook and CircleCI tests.


## GitHub Actions Badge
Add a GitHub Actions Passing/Failing Badge: [link to docs](https://docs.github.com/en/actions/monitoring-and-troubleshooting-workflows/adding-a-workflow-status-badge)

![hidden words](https://github.com/ethanmsl/asynch_xplr/actions/workflows/test-poet.yml/badge.svg)

## Dev-Dependencies Specified
- formatting: `isort` & `black`
- linting: `pylint`
- lsp & typechecking: `pyright`
- testing: `pytest` + `coverage` (via `pytest-cov`)
- auto-documentation: `pdoc` (*not* ~~"pdoc3"~~, which should be strongly avoided)


## Run Pre-Commit Hook Manually
from anywhere in project:
```zsh
git hook run pre-commit
```

**Note**: the `pre-commit` file needs to be placed in the `.git/hooks/` directory.
