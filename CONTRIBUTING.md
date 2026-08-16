# Contributing

Contributions that improve the Skill's decision framework, documentation,
cross-platform behavior, or evaluation coverage are welcome.

## Before opening a pull request

1. Fork the repository and create a focused branch.
2. Keep changes limited to one clear purpose.
3. Run the local checks from the repository root:

```bash
PYTHONPYCACHEPREFIX=/tmp/get-more-perspectives-pycache \
  python3 scripts/check_pipeline.py . --json
python3 scripts/run_evals.py
```
4. Update documentation and evaluation cases when behavior changes.
5. Open a pull request that explains the problem, the change, and the checks
   performed.

Do not include credentials, personal data, proprietary material, or assets
without redistribution rights. By contributing, you agree that your
contribution is licensed under the MIT License in this repository.
