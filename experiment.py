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
from .tutorial import ModifyScreenSize, OuterProposalTutorial

def page_not_ok(participant) -> bool:
    return participant.answer != "Tutorial_Ok"

class Exp(psynet.experiment.Experiment):
    label = "Hello world"
    text = label

    timeline = Timeline(
        OuterProposalTutorial(
            avatar="me",
            time_estimate=1000,
        ),
        OuterProposalTutorial(
            avatar="partner",
            time_estimate=1000,
        ),
        ModifyScreenSize(
            zoom_in_out="out",
            zoom_count=3,
            time_estimate=10,
        ),
        conditional(
            label="check_tutorial_failed",
            condition=lambda participant: page_not_ok(participant),
            logic_if_true=UnsuccessfulEndPage(
                failure_tags=["tutorial_failed"],
            ),
            logic_if_false=None,
        ),
        ModifyScreenSize(
            zoom_in_out="in",
            zoom_count=3,
            time_estimate=10,
        ),
        conditional(
            label="check_tutorial_failed",
            condition=lambda participant: page_not_ok(participant),
            logic_if_true=UnsuccessfulEndPage(
                failure_tags=["tutorial_failed"],
            ),
            logic_if_false=None,
        ),
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
