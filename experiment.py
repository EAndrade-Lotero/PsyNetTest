import psynet.experiment
from psynet.modular_page import ModularPage, NullControl
from psynet.page import InfoPage, UnsuccessfulEndPage
from psynet.timeline import Timeline, PageMaker, CodeBlock, conditional
from psynet.utils import get_logger

logger = get_logger()

from .custom_pages import (
    OuterProposalPage,
    OuterAcceptancePage,
    InnerProposalPage,
    InnerAcceptancePage,
    ScorePage,
)
from .custom_front_end import CustomLikertControl
from .custom_front_end import TimeoutPrompt
from .custom_timeline import CustomTimeline, EndRoundPage

from .final_survey import get_final_survey
from .tutorial import get_tutorial_pages

class Exp(psynet.experiment.Experiment):
    label = "Hello world"
    text = label

    timeline = Timeline(
        *get_tutorial_pages(),
        ModularPage(
            label="end_of_tutorial",
            prompt=TimeoutPrompt(
                text="End of Tutorial.",
                timeout=5,
            ),
            control=NullControl(),
            time_estimate=5,
        )
    )
