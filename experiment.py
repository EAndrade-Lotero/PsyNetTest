import psynet.experiment
from psynet.page import InfoPage
from psynet.timeline import Timeline

from .custom_pages import OuterProposalPage
from .custom_front_end import OuterGameControl

class Exp(psynet.experiment.Experiment):
    label = "Hello world"

    timeline = Timeline(
        InfoPage("Hello world!", time_estimate=5),
        OuterProposalPage(
            context={
                "coin_url": "/static/coin.png",
                "generic_url": "/static/generic.png",
                "plate_url": "/static/plate.png",
            },
        )
    )
