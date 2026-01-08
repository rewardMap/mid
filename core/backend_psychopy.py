from rewardgym.psychopy_render import (
    ImageStimulus,
    FeedBackStimulus,
    ActionStimulusTooEarly,
    BaseStimulus,
)
from rewardgym.stimuli import fixation_cross, mid_stimuli


def get_psychopy_info(
    random_state=111,
    key_dict={"left": 0, "right": 1},
    external_stimuli=None,
    fullpoints=None,
    **kwargs,
):
    reward_feedback = FeedBackStimulus(
        2.0, text="{0}", target="reward", name="reward", bar_total=fullpoints, rl_label="reward"
    )

    fix_isi = ImageStimulus(
        image_paths=[fixation_cross()],
        duration=1.5,
        name="isi",
        autodraw=False,
        wait_no_keys=True,
    )

    action_stim = ActionStimulusTooEarly(
        duration=0.35, timeout_action=1, key_dict=key_dict, rl_label="action",
    )

    def first_step(img, img2):
        return [
            ImageStimulus(
                duration=2.0,
                image_paths=[img],
                positions=[(0, 0)],
                name="cue",
                rl_label="obs",
            ),
            fix_isi,
            ImageStimulus(
                duration=0.01,
                image_paths=[img2],
                positions=[(0, 0)],
                name="target",
                wait_no_keys=True,
            ),
            action_stim,
        ]

    final_step = [
        BaseStimulus(duration=None, rl_label="obs", noflip=True),
        reward_feedback,
    ]

    info_dict = {
        1: {
            "psychopy": first_step(
                mid_stimuli("-5", shape="square", probe=False),
                mid_stimuli("-5", shape="square", probe=True),
            )
        },  # big lose
        2: {
            "psychopy": first_step(
                mid_stimuli("-1", shape="square", probe=False),
                mid_stimuli("-1", shape="square", probe=True),
            )
        },  # small lose
        3: {
            "psychopy": first_step(
                mid_stimuli("0", shape="triangle_u", probe=False),
                mid_stimuli("0", shape="triangle_u", probe=True),
            )
        },  # control
        4: {
            "psychopy": first_step(
                mid_stimuli("+1", shape="circle", probe=False),
                mid_stimuli("+1", shape="circle", probe=True),
            )
        },  # small win
        5: {
            "psychopy": first_step(
                mid_stimuli("+5", shape="circle", probe=False),
                mid_stimuli("+5", shape="circle", probe=True),
            )
        },  # big win
        6: {"psychopy": final_step},
        7: {"psychopy": final_step},
        8: {"psychopy": final_step},
        9: {"psychopy": final_step},
        10: {"psychopy": final_step},
    }

    return info_dict, None
