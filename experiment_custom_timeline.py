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

    timeline = CustomTimeline(
        CodeBlock(
            lambda participant: participant.var.set("round_failed", True)
        ),
        InfoPage(
            "In this page I fail the round.",
            time_estimate=5,
        ),
        InfoPage(
            "I should have skipped this page",
            time_estimate=5,
        ),
        ModularPage(
            label="end_round",
            prompt="This the end-of-round page",
            control=NullControl(),
            save_answer="reward",
            time_estimate=5,
        ),
        InfoPage(
            "This is the last page",
            time_estimate=5,
        )
    )
