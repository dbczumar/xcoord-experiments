import argparse
import time
import random

import numpy as np

import mlflow
from mlflow.tracking.client import MlflowClient


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='PyTorch MNIST Example')
    parser.add_argument('--runs', type=int, default=1, help='The number of runs to generate')
    parser.add_argument('--metrics', type=int, default=5, help='The number of metrics to generate for each run')
    parser.add_argument('--min-step', type=int, default=-10, help='The minimum step to record for each metric')
    parser.add_argument('--max-step', type=int, default=100, help='The maximum step to record for each metric')
    parser.add_argument('--min-value', type=float, default=-10, help='The maximum value to record for each metric')
    parser.add_argument('--max-value', type=float, default=10, help='The maximum value to record for each metric')
    parser.add_argument('--entry-dropout', type=float, default=0.1, help='The fraction of entries to randomly omit')
    parser.add_argument('--step-replication', type=float, default=0.1, help='The fraction of entries that should be given the same step')
    parser.add_argument('--shuffle', action="store_true", help='If specified, shuffles timestamps')

    args = parser.parse_args()

    mlflow_client = MlflowClient()

    for i in range(args.runs):
        with mlflow.start_run():
            run_id = mlflow.active_run().info.run_uuid
            for j in range(args.metrics):
                metric_name = "metric_{idx}".format(idx=j)

                steps = range(args.min_step, args.max_step)
                replicated_steps = np.random.choice(steps, size=int(len(steps) * args.step_replication))
                steps = np.concatenate([steps, replicated_steps])

                curr_time = int(time.time())
                timestamps = [1000 * item for item in xrange(curr_time, curr_time + len(steps))]
                if args.shuffle:
                    np.random.shuffle(timestamps)

                steps_timestamps = zip(steps, timestamps)
                sample_indices = random.sample(
                    range(len(steps_timestamps)),
                    int((1 - args.entry_dropout) * len(steps_timestamps)))
                steps_timestamps = [steps_timestamps[i] for i in sorted(sample_indices)]

                values = (args.max_value - args.min_value) * np.random.random(len(steps_timestamps)) + args.min_value

                for k in range(len(steps_timestamps)):
                    step, timestamp = steps_timestamps[k]
                    value = values[k]
                    print(step, timestamp, value)
                    mlflow_client.log_metric(
                        run_id=run_id,
                        key=metric_name,
                        value=value,
                        timestamp=timestamp,
                        step=step)

