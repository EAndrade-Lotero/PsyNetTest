import psynet.experiment
from psynet.modular_page import ModularPage
from psynet.page import InfoPage
from psynet.timeline import Timeline, PageMaker

from .custom_pages import (
    OuterProposalPage,
    OuterAcceptancePage,
    InnerProposalPage,
    InnerAcceptancePage,
)
from .custom_front_end import CustomLikertControl


class Exp(psynet.experiment.Experiment):
    label = "Hello world"

    timeline = Timeline(
        # ModularPage(
        #     label="likert",
        #     prompt="This is a Likert scale",
        #     control=CustomLikertControl(
        #         lowest_value="Very unlikely",
        #         highest_value="Very likely",
        #         n_steps=5,
        #         timeout=5,
        #         timeout_answer="None",
        #     ),
        #     save_answer="likert",
        #     time_estimate=5,
        # ),
        # OuterProposalPage(
        #     context={
        #         "coin_url": "/static/coin.png",
        #         "generic_url": "/static/generic.png",
        #         "plate_url": "/static/plate.png",
        #     },
        # ),
        # WaitingPage(
        #     context={
        #         "coin_url": "/static/coin.png",
        #         "generic_url": "/static/generic.png",
        #         "plate_url": "/static/plate.png",
        #     },
        # ),
        # OuterAcceptancePage(
        #     context={
        #         "coin_url": "/static/coin.png",
        #         "generic_url": "/static/generic.png",
        #         "plate_url": "/static/plate.png",
        #     },
        #     proposal="RESPONDER",
        # ),
        # InnerProposalPage(
        #     game="ultimatum",
        #     context={
        #         "coin_url": "/static/coin.png",
        #         "generic_url": "/static/generic.png",
        #         "plate_url": "/static/plate.png",
        #     },
        # ),
        InnerAcceptancePage(
            context={
                "coin_url": "/static/coin.png",
                "generic_url": "/static/generic.png",
                "plate_url": "/static/plate.png",
            },
            proposal=3,
        ),
        PageMaker(
            lambda experiment, participant:
                InfoPage(
                    f"{participant.answer}",
                time_estimate=5
            ),
            time_estimate=5
        ),
    )
