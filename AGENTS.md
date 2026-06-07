# Repository Guidelines

## Project Structure & Module Organization
Core code lives in `scripts/`:

- `grid_env.py`: Gym-style grid world environment and transition/reward tables
- `solver.py`: value iteration, policy iteration, Monte Carlo, TD, DQN, and REINFORCE experiments
- `model.py`: PyTorch policy/value/Q networks
- `render.py`: Matplotlib-based grid and trajectory rendering

`README.md` provides project background. `.idea/` is editor-local and should not carry project logic.

## Build, Test, and Development Commands
This repository does not currently ship a `requirements.txt` or Makefile, so run modules directly from the repo root.

```bash
python scripts/grid_env.py
python scripts/solver.py
python -m tensorboard.main --logdir logs
```

- `python scripts/grid_env.py` opens a minimal environment render.
- `python scripts/solver.py` runs the default RL experiment and visualization.
- TensorBoard reads training logs written by `SummaryWriter("logs")`.

Install dependencies explicitly if needed: `pip install numpy matplotlib gymnasium gym torch tensorboard`.

## Coding Style & Naming Conventions
Use 4-space indentation and follow existing Python style. Prefer `snake_case` for functions, methods, variables, and module names; use `PascalCase` for classes like `GridEnv` and `PolicyNet`.

Keep new logic modular: environment behavior in `grid_env.py`, learning algorithms in `solver.py`, and networks in `model.py`. Add short comments only where the math or control flow is not obvious.

## Testing Guidelines
There is no automated test suite yet. For changes, add focused checks by running the affected module directly and verifying:

- environment reset/step behavior
- solver convergence or loss trends
- rendering still opens without errors

If you add tests, prefer `pytest` under a new `tests/` directory with names like `test_grid_env.py`.

## Commit & Pull Request Guidelines
Recent history uses short subjects such as `update`, but contributors should be more specific. Use concise imperative messages, for example `solver: fix value iteration stopping condition`.

Pull requests should include:

- a brief summary of the algorithm or rendering change
- the command(s) used for manual verification
- screenshots or plots when visuals or training curves change
- linked issues or experiment context when relevant

## Configuration Tips
`solver.py` writes logs to `logs/` and some render paths reference `image/`. Create those directories locally when using TensorBoard or video export if they do not already exist.
