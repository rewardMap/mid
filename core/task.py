import pathlib
from typing import Literal

import numpy as np

from rewardgym import check_random_state
from rewardgym.reward_classes import BaseReward
from rewardgym.tasks.yaml_tools import load_task_from_yaml
from rewardgym.runner.plugins import AddRemainder, StairCaseMid, MiscUpdateMid, TimeUpdateMid

def get_task(
    render_backend: Literal["pygame", "psychopy"] | None = None,
    random_state: int | np.random.Generator = 1000,
    key_dict=None,
    **kwargs,
):
    random_state = check_random_state(random_state)
    yaml_file = pathlib.Path(__file__).parents[1].resolve() / "task.yaml"
    info_dict, environment_graph = load_task_from_yaml(yaml_file)

    reward_structure = {
        6: BaseReward(-5),
        7: BaseReward(-1),
        8: BaseReward(0),
        9: BaseReward(1),
        10: BaseReward(5),
    }

    info_dict.update(
        {
            "position": {
                0: "large-loss",
                1: "small-loss",
                2: "neutral",
                3: "small-win",
                4: "large-win",
            }
        }
    )


    if render_backend is not None:
        from .render import get_render_info
        if key_dict is None:
            key_dict = {"left": 0, "right": 1}
        render_dict, _ = get_render_info(
            random_state=random_state, key_dict=key_dict, fullpoints=info_dict["meta"]["fullpoints"]
        )
        info_dict.update(render_dict)

    info_dict.update({"plugins":{ "pre-trial": [MiscUpdateMid(), TimeUpdateMid()],
        "post-trial": [AddRemainder(), StairCaseMid(0)]}})

    return environment_graph, reward_structure, info_dict
