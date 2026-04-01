from datetime import datetime

import numpy
from dallinger.experiment import experiment_route
from dominate import tags

import psynet.experiment
from psynet.consent import MainConsent
from psynet.modular_page import (
    ModularPage,
    NumberControl,
    Prompt,
    PushButtonControl,
    TextControl,
    TimedPushButtonControl,
)
from psynet.page import InfoPage
from psynet.timeline import (
    CodeBlock,
    Module,
    PageMaker,
    Timeline,
    conditional,
    switch,
    while_loop,
)


class Exp(psynet.experiment.Experiment):
    label = "Timeline exercise"
    initial_recruitment_size = 1

    config = {
        "min_accumulated_reward_for_abort": 0.15,
        "show_abort_button": True,
    }

    @experiment_route("/custom_route", methods=["POST", "GET"])
    @classmethod
    def custom_route(cls):
        return f"A custom route for {cls.__name__}."

    timeline = Timeline(
        #----------------------------------------------
        # Variable initialization
        #----------------------------------------------
        CodeBlock(
            lambda participant: participant.set_answer("Yes")
        ),
        CodeBlock(
            lambda participant: participant.var.new(
                "price", {
                    "Bananas": 2.2,
                    "Apples": 1.0,
                    "Oranges": 1.5
                },
            )
        ),
        CodeBlock(
            lambda participant: participant.var.new(
                "virtual_basket", dict()
            )
        ),
        #----------------------------------------------
        # Main loop
        #----------------------------------------------
        while_loop(
            "main_loop",
            lambda participant: participant.answer == "Yes",
            Module(
                "color",
                PageMaker(
                    lambda participant: [
                        ModularPage(
                            "Shopping items",
                            Prompt("Please choose the item you want to purchase:"),
                            control=PushButtonControl(
                                ["Bananas", "Apples", "Oranges"], 
                                arrange_vertically=False
                            ),
                            time_estimate=5,
                            save_answer="item",
                        ),
                    ],
                    time_estimate=5,
                ),
                CodeBlock(
                    lambda participant: participant.var.set(
                        "item", participant.answer
                    )
                ),
                PageMaker(
                    lambda participant: [
                        ModularPage(
                            "Amount",
                            Prompt(f"How many {participant.var.item} do you want?\nEach one costs {participant.var.price[participant.var.item]}"),
                            NumberControl(),
                            time_estimate=5,
                            save_answer="amount",
                        ),
                    ],
                    time_estimate=5,
                ),
                CodeBlock(
                    lambda participant: participant.var.virtual_basket.update({
                        participant.var.item: participant.var.amount
                    })
                ),
                PageMaker(
                    lambda participant: [
                        InfoPage(
                            f"You have ordered {participant.var.amount} {participant.var.item}",
                            time_estimate=3,
                        ),
                    ],
                    time_estimate=5,
                ),
                ModularPage(
                    "stop_condition",
                    Prompt("Would you like to continue shopping?"),
                    control=PushButtonControl(["Yes", "No"], arrange_vertically=False),
                    save_answer="finished",
                    time_estimate=3,
                ),
            ),
            expected_repetitions=3,
        ), # End while loop
        #----------------------------------------------
        # Aggregation and final info
        #----------------------------------------------
        PageMaker(
            lambda participant: [
                InfoPage(
                    f"Your order is:\n{'\n'.join([f'{amount} {item};' for item, amount in participant.var.virtual_basket.items()])} for a total of {sum([participant.var.price[item] * float(amount) for item, amount in participant.var.virtual_basket.items()])} dollars",
                    time_estimate=3,
                ),
            ],
            time_estimate=5,
        ),

    ) # End timeline