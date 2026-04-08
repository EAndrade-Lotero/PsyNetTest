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
            lambda participant: CustomTimeline.go_to_end(participant)
        ),
        CodeBlock(
            lambda participant: logger.info(
                f"==>>>>: {participant.elt_id}"
            )
        ),
        InfoPage(
            "This is the MIDDLE page",
            time_estimate=5,
        ),
        ModularPage(
            label="test1",
            prompt="This is a test",
            control=NullControl(),
            time_estimate=5,
        ),
        CodeBlock(
            lambda participant: logger.info(f"==>>>>: {participant.elt_id}")
        ),
        PageMaker(
            lambda experiment, participant:
                InfoPage(
                    f"{participant.answer}",
                time_estimate=5
            ),
            time_estimate=5
        ),
        CodeBlock(
            lambda participant: logger.info(f"==>>>>: {participant.elt_id}")
        ),
        InfoPage(
            "This is the last page",
            time_estimate=5,
        )
    )
