#!/usr/bin/env bash

python gen_metrics.py --runs 1 --metrics 5 --min-step -10 --max-step 100\
    --min-value -10 --max-value 10 --entry-dropout 0 --step-replication 0.0

python gen_metrics.py --runs 1 --metrics 3 --min-step -10 --max-step 100\
    --min-value -10 --max-value 10 --entry-dropout 0.1 --step-replication 0.0

python gen_metrics.py --runs 1 --metrics 5 --min-step -50 --max-step 200\
    --min-value -500.0 --max-value 1000.0 --entry-dropout 0.2 --step-replication 0.0

python gen_metrics.py --runs 1 --metrics 5 --min-step -10 --max-step 100\
    --min-value -10 --max-value 10 --entry-dropout 0 --shuffle --step-replication 0.0

python gen_metrics.py --runs 1 --metrics 5 --min-step -10 --max-step 100\
    --min-value -10 --max-value 10 --entry-dropout 0 --shuffle --step-replication 0.2



