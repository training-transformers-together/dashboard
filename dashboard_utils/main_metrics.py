import wandb

WANDB_REPO = "learning-at-home/Main_metrics"

def get_main_metrics():
    api = wandb.Api()
    runs = api.runs(WANDB_REPO)
    run = runs[0]
    history = run.scan_history(keys=["step", "loss", "alive peers"])

    steps = []
    losses = []
    alive_peers = []
    for row in history:
        steps.append(row["step"])
        losses.append(row["loss"])
        alive_peers.append(row["alive peers"])

    return steps, losses, alive_peers