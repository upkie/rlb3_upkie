# RLB3 environment for Upkie wheeled bipeds

Software to train neural-network policies for Upkie wheeled bipeds using [RL Baselines3 Zoo](https://github.com/DLR-RM/rl-baselines3-zoo).

<img alt="image" src="https://github.com/user-attachments/assets/2d0313b2-ed96-4acd-b3e4-03db68437097" />

## Installation

This project uses [pixi](https://pixi.sh/latest/#installation) to run tasks and manage Python dependencies automatically.

## Usage

To train a new policy:

```console
pixi run train
```

This will train using 8 parallel environments by default. To customize the number of environments or show the PyBullet GUI during training:

```console
pixi run train <n_envs> [gui]
```

Examples:

```console
# Train with 4 parallel environments (no GUI)
pixi run train 4

# Train with 2 environments and display the PyBullet GUI
pixi run train 2 gui
```

To test the latest trained policy:

```console
pixi run enjoy
```

## Development

- Linting: `pixi run lint`
- Testing: `pixi run test`
