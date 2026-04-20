import psynet.experiment
from psynet.modular_page import ModularPage, NullControl
from psynet.page import InfoPage
from psynet.timeline import Timeline, PageMaker, CodeBlock
from psynet.utils import get_logger

logger = get_logger()

from .custom_pages import (
    OuterProposalPage,
    OuterAcceptancePage,
    InnerProposalPage,
    InnerAcceptancePage,
)
from .custom_front_end import CustomLikertControl
from .custom_timeline import CustomTimeline


class Exp(psynet.experiment.Experiment):
    label = "Hello world"
    text = label

    timeline = CustomTimeline(
        InfoPage(
            "Here we go",
            time_estimate=5,
        ),
        ModularPage(
            label=label,
            prompt=TimeoutPrompt(
                text=Markup(text),
                timeout=10,
            ),
            control=CustomLikertControl(
                lowest_value="Very inaccurate",
                highest_value="Very accurate",
                n_steps=5,
            ),
            time_estimate=10,
        )
    )
