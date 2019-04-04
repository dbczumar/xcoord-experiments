import wandb

def multiple_values_same_step():
    for i in range(3):
        val = {
            "cat": i,
        }
        wandb.log(val, step=0)


def same_value_multiple_steps():
    val = {
        "cat": 1,
    }
    for i in range(3):
        wandb.log(val, step=i)

def diff_value_multiple_steps():
    for i in range(3):
        val = {
            "cat": i,
        }
        wandb.log(val, step=i)

def same_value_no_step():
    for i in range(3):
        val = {
            "cat": 1
        }
        wandb.log(val)

def diff_value_no_step():
    for i in range(3):
        val = {
            "cat": 1
        }
        wandb.log(val)

def large_step_numbers():
    for i in range(3):
        val = {
            "cat": 1
        }
        wandb.log(val, step=i + 50)

def update_previous_step():
    for i in range(10):
        val = {
            "cat": i
        }
        wandb.log(val, step=i % 3)

def negative_step():
    val = {
        "cat": 1,
    }
    wandb.log(val, step=-5)

def multiple_values_different_steps_large_step_first():
    val1 = {
        "cat": 1,
    }
    wandb.log(val1, step=7)

    val2 = {
        "dog": 1,
    }
    wandb.log(val2, step=5)


def multiple_values_different_steps_small_step_first():
    val1 = {
        "cat": 1,
    }
    wandb.log(val1, step=5)

    val2 = {
        "dog": 1,
    }
    wandb.log(val2, step=7)

if __name__ == "__main__":
    import wandb
    wandb.init(project="test")

    # multiple_values_same_step()
    # same_value_multiple_steps()
    # diff_value_multiple_steps()
    # same_value_no_step()
    # diff_value_no_step()
    # large_step_numbers()
    # update_previous_step()
    # negative_step()
    # multiple_values_different_steps()
    # multiple_values_different_steps_large_step_first()
    multiple_values_different_steps_small_step_first()
