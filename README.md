# RLB3 environment for Upkie wheeled bipeds

Software to train neural-network policies for Upkie wheeled bipeds using [RL Baselines3 Zoo](https://github.com/DLR-RM/rl-baselines3-zoo).

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

Project tasks such as linting and testing are managed with [pixi](https://pixi.sh/latest/#installation).

- Linting: `pixi run lint`
- Testing: `pixi run test`
