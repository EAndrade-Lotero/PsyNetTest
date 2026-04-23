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
    ScorePage,
)
from .custom_front_end import CustomLikertControl
from .custom_timeline import CustomTimeline

from .final_survey import get_final_survey

class Exp(psynet.experiment.Experiment):
    label = "Hello world"
    text = label

    timeline = Timeline(
        ScorePage(
            outer_game_type="ultimatum",
            inner_game_type="ultimatum",
            proposer=False,
            proposal=2,
            remainder_=8,
            accumulated_score=10,
            partners_accumulated_score=11,
            outer_accepted=True,
            inner_accepted=True,
            round_failed=False,
            num_rounds_failed=1,
            round_=1,
        ),
        PageMaker(
            lambda participant: InfoPage(
                f"{participant.answer}",
                time_estimate=5
            ),
            time_estimate=5
        ),
    )
