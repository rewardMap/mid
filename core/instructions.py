import json
import pathlib

from rewardgym.render.routines.passive_routines import InstructionRoutine
from rewardgym.render.stimuli import mid_stimuli
from rewardgym.render.stimulus_definitions import ImageDefinition, TextDefinition
from rewardgym.utils import NameCounter

instructions_path = (
    pathlib.Path(__file__).parent.resolve() / "assets" / "instructions_en.json"
)
instructions = json.loads(instructions_path.read_text())



def get_instructions(instructions=instructions):

    stim_name = NameCounter()

    size = (125, 125)

    left_pos = [-265, -135, 0, 135, 265]

    part_0_0 = TextDefinition(
        name=stim_name.name,
        text=instructions["0.0"],
        height=28,
        pos=(0, 200),
    )

    stims = [
        mid_stimuli(am, shap)
        for am, shap in zip(
            ["-5", "-1", "0", "+1", "+5"],
            ["square", "square", "triangle_u", "circle", "circle"],
        )
    ]

    stims = [
        ImageDefinition(image=i, pos=(lp, 75), size=size, name=stim_name.name)
        for i, lp in zip(stims, left_pos)
    ]
    part_0_1 = TextDefinition(
        name=stim_name.name,
        text=instructions["0.1"],
        height=28,
        pos=(0, -150),
    )

    part_0 = InstructionRoutine(name="part_0",
    stimulus_definitions=stims + [part_0_0, part_0_1])

    part_1_0 = TextDefinition(
        name=stim_name.name,
        text=instructions["1.0"],
        height=28,
        pos=(0, 275),
    )
    size = (125, 125)

    img1 = ImageDefinition(
        name=stim_name.name,
            image=mid_stimuli("+5", "circle"), size=size, pos=(0, 170)
    )

    img2 = ImageDefinition(
                    name=stim_name.name,
            image=mid_stimuli("-5", "square"), size=size, pos=(0, -125)
    )

    part_1_1 = TextDefinition(
        name=stim_name.name,
        text=instructions["1.1"],
        height=28,
        pos=(0, 20),
    )

    part_1_2 = TextDefinition(
        name=stim_name.name,
        text=instructions["1.2"],
        height=28,
        pos=(0, -225),
    )

    part_1 = InstructionRoutine(
        name="part_1",
        stimulus_definitions=[part_1_0, part_1_1, part_1_2, img1, img2]
    )

    left_pos = [-130, 0, 130]

    stims = [
        mid_stimuli(am, shap, probe=True)
        for am, shap in zip(["", "", ""], ["square", "triangle_u", "circle"])
    ]

    stims = [
        ImageDefinition( image=i, pos=(lp, 0), size=size, name=stim_name.name)
        for i, lp in zip(stims, left_pos)
    ]
    part_2_0 = TextDefinition(
        name=stim_name.name,
        text=instructions["2.0"],
        height=28,
        pos=(0, 200),
    )

    part_2_1 = TextDefinition(
        name=stim_name.name,
        text=instructions["2.1"],
        height=28,
        pos=(0, -200),
    )

    part_2 = InstructionRoutine(
        name="part_2",
        stimulus_definitions=stims + [part_2_0, part_2_1]
    )

    part_3_0 = TextDefinition(
        name=stim_name.name,
        text=instructions["3.0"],
        height=28,
        alignText="center",
    )

    part_3 = InstructionRoutine(
        stimulus_definitions=[part_3_0], name="part_3"
    )

    return [part_0, part_1, part_2, part_3], instructions
