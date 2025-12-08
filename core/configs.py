from rewardgym.utils import check_random_state


def get_configs(stimulus_set: str = "1", use_abcd=True):
    random_state = check_random_state(int(stimulus_set))

    # 0 & 1 = win, 2  = neutral, 3 & 4 = lose
    condition_dict = {
        "loss-large": {0: {0: 1}},
        "loss-small": {0: {0: 2}},
        "neutral": {0: {0: 3}},
        "win-small": {0: {0: 4}},
        "win-large": {0: {0: 5}},
    }

    if not use_abcd:
        condition_template = [
            "loss-large",
            "loss-small",
            "neutral",
            "win-small",
            "win-large",
        ]
        isi_template = [1.5, 2.125, 2.75, 3.375, 4.0]

        n_blocks = 10

        conditions = random_state.permutation(condition_template * 2).tolist()
        isi = random_state.permutation(isi_template * 2).tolist()

        for _ in range(n_blocks - 1):
            reject = True
            while reject:
                condition_template = random_state.permutation(condition_template * 2).tolist()

                if conditions[-1] != condition_template[0]:
                    reject = False
                    conditions.extend(condition_template)
                    isi.extend(
                        random_state.permutation(
                            isi_template * 2, size=10, replace=False
                        ).tolist()
                    )

    if use_abcd:
        from ._mid_abcd_order import (
            citation_notice,
            stimulus_combinations,
            stimulus_sets,
        )

        print("".join(["="] * 20))
        print(citation_notice)
        print("".join(["="] * 20))
        trial_order = random_state.choice(
            list(stimulus_combinations.keys()), 1, replace=False
        ).item()
        stim_combinations = stimulus_combinations[trial_order]

        conditions = (
            stimulus_sets[stim_combinations[0]]["condition"]
            + stimulus_sets[stim_combinations[1]]["condition"]
        )
        isi = (
            stimulus_sets[stim_combinations[0]]["isi"]
            + stimulus_sets[stim_combinations[1]]["isi"]
        )

    iti = [2] * len(conditions)

    config = {
        "name": "mid",
        "stimulus_set": (stimulus_set, use_abcd),
        "isi": isi,
        "reward": iti,
        "condition": conditions,
        "condition_dict": condition_dict,
        "ntrials": len(conditions),
        "update": ["isi", "reward"],
        "add_remainder": True,
        "breakpoints": [49],
        "break_duration": 45,
    }

    return config

    return config
