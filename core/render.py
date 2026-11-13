from rewardgym.render import ImageDefinition
from rewardgym.render.routines import FeedBackRoutine, PresentationRoutine
from rewardgym.render.routines import ActionRoutine
from rewardgym.stimuli import fixation_cross, mid_stimuli


def get_render_info(
    random_state=111,
    key_dict=None,
    external_stimuli=None,
    fullpoints=None,
    **kwargs,
):

    if key_dict is None:
        key_dict = {"left": 0, "right": 1, "space": 0}
    reward_feedback = FeedBackRoutine(
        duration=2.0, name="reward", bar_total=fullpoints, rl_label="reward"
    )


    fix_isi = PresentationRoutine(
        stimulus_definitions=[ImageDefinition(name='fixation', autoDraw=False, image=fixation_cross())],
        duration=1.5,
        name="isi",
        poll_keys=False,
    )

    action_stim = ActionRoutine(
        name="action",
        duration=0.35, timeout_action=1, too_early_action=1, key_dict=key_dict, rl_label="action", detect_too_early=True
    )

    def first_step(img, img2):
        return [
            PresentationRoutine(
                duration=2.0,
                stimulus_definitions=[
                    ImageDefinition(
                        pos=(0, 0),
                        name="cue",
                        image=img
                    )
                ],
                name="cue",
                rl_label="obs",
            ),
            fix_isi,
            PresentationRoutine(
                duration=0.01,
                stimulus_definitions=[
                    ImageDefinition(
                        pos=(0, 0),
                        name="cue",
                        image=img2
                    )
                ],
                name="target",
                poll_keys=False,
            ),
            action_stim,
        ]

    final_step = [
        PresentationRoutine(duration=None, rl_label="obs", flip=False),
        reward_feedback,
    ]

    info_dict = {
        1: {
            "render": first_step(
                mid_stimuli("-5", shape="square", probe=False),
                mid_stimuli("-5", shape="square", probe=True),
            )
        },  # big lose
        2: {
            "render": first_step(
                mid_stimuli("-1", shape="square", probe=False),
                mid_stimuli("-1", shape="square", probe=True),
            )
        },  # small lose
        3: {
            "render": first_step(
                mid_stimuli("0", shape="triangle_u", probe=False),
                mid_stimuli("0", shape="triangle_u", probe=True),
            )
        },  # control
        4: {
            "render": first_step(
                mid_stimuli("+1", shape="circle", probe=False),
                mid_stimuli("+1", shape="circle", probe=True),
            )
        },  # small win
        5: {
            "render": first_step(
                mid_stimuli("+5", shape="circle", probe=False),
                mid_stimuli("+5", shape="circle", probe=True),
            )
        },  # big win
        6: {"render": final_step},
        7: {"render": final_step},
        8: {"render": final_step},
        9: {"render": final_step},
        10: {"render": final_step},
    }

    return info_dict, None
