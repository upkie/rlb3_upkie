# RLB3 environment for Upkie wheeled bipeds

Software to train neural-network policies for Upkie wheeled bipeds using [RL Baselines3 Zoo](https://github.com/DLR-RM/rl-baselines3-zoo).

## Installation

This project uses [pixi](https://pixi.sh/latest/#installation) to manage Python dependencies.

## Usage

To train a new policy:

```console
pixi run train
```

To test the latest trained policy:

```console
pixi run enjoy
```

## Development

- Linting: `pixi run lint`
- Testing: `pixi run test`
