import psynet.experiment
from psynet.page import InfoPage
from psynet.timeline import Timeline, PageMaker

from .custom_pages import (
    OuterProposalPage,
    OuterAcceptancePage,
    InnerProposalPage,
    OuterProposalWaitingPage,
    InnerProposalWaitingPage,
    InnerAcceptancePage,
)


class Exp(psynet.experiment.Experiment):
    label = "Hello world"

    timeline = Timeline(
        OuterProposalPage(
            context={
                "coin_url": "/static/coin.png",
                "generic_url": "/static/generic.png",
                "plate_url": "/static/plate.png",
            },
        ),
        OuterProposalWaitingPage(
            context={
                "coin_url": "/static/coin.png",
                "generic_url": "/static/generic.png",
                "plate_url": "/static/plate.png",
            },
        ),
        OuterAcceptancePage(
            context={
                "coin_url": "/static/coin.png",
                "generic_url": "/static/generic.png",
                "plate_url": "/static/plate.png",
            },
            proposal="RESPONDER",
        ),
        InnerProposalPage(
            game="ultimatum",
            context={
                "coin_url": "/static/coin.png",
                "generic_url": "/static/generic.png",
                "plate_url": "/static/plate.png",
            },
        ),
        InnerProposalWaitingPage(
            context={
                "coin_url": "/static/coin.png",
                "generic_url": "/static/generic.png",
                "plate_url": "/static/plate.png",
            },
        ),
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
