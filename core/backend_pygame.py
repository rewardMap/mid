from rewardgym.pygame_render import (
    BaseDisplay,
    BaseText,
    TimedAction,
    feedback_block,
)

def get_pygame_info(action_map, window_size=256):
    base_position = (window_size // 2, window_size // 2)

    reward_disp, earnings_text = feedback_block(base_position)

    def first_step(stim1, stim2):
        return [
            BaseDisplay(None, 500),
            BaseText(stim1, 2000, textposition=base_position),
            BaseDisplay(None, 500),
            BaseText(stim2, 200, textposition=base_position),
            TimedAction(500),
        ]

    final_display = [
        BaseDisplay(None, 500),
        reward_disp,
        earnings_text,
    ]

    pygame_dict = {
        1: {"pygame": first_step("LL", "x")},
        2: {"pygame": first_step("LL", "x")},
        3: {"pygame": first_step("O", "o")},
        4: {"pygame": first_step("W", "+")},
        5: {"pygame": first_step("WW", "+")},
        6: {"pygame": final_display},
        7: {"pygame": final_display},
        8: {"pygame": final_display},
        9: {"pygame": final_display},
        10: {"pygame": final_display},
    }

    return pygame_dict
