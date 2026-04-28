from psynet.modular_page import ModularPage, NullControl
from .custom_front_end import TimeoutPrompt

from .game_paramters import TIMEOUT_PROPOSALS


########################################################
# Modify Screen Size Page
########################################################

class ModifyScreenSizeControl(NullControl):
    macro = "modify_screen_size"
    external_template = "modify_screen_size.html"

    def __init__(self, zoom_in_out: str = "out", zoom_count: int = 0):
        super().__init__()
        self.zoom_in_out = zoom_in_out
        self.zoom_count = zoom_count

    def get_bot_response(self, experiment, bot):
        return bot.get_response(self.zoom_in_out, self.zoom_count)


class ModifyScreenSize(ModularPage):

    def __init__(
        self,
        zoom_in_out: str = "out",
        zoom_count: int = 0,
        time_estimate: int = TIMEOUT_PROPOSALS,
    ):
        self.time_estimate = time_estimate
        assert zoom_in_out in ["in", "out"], "zoom_in_out must be either 'in' or 'out'"
        assert zoom_count >= 0, "zoom_count must be greater than 0"

        zoom_in_out_ = zoom_in_out.upper()
        bg = "#fff9e6" if zoom_in_out == "in" else "#e3f2fd"

        text = (
            f"<div style='background-color: {bg}; padding: 1rem 1.25rem; border-radius: 8px;'>"
            f"<h2>Adjusting the screen size</h2>"
            f"Some frames may be outside your screen. You can adjust the screen size to see them."
            f"<p>You can use the keyboard shortcut to zoom in and out."
            f"<p>For Mac, use the Command + Plus/Minus keys. </p>"
            f"<p>For Windows, use the Ctrl + Plus/Minus keys. </p>"
            f"<p>For Linux, use the Ctrl + Plus/Minus keys.</p>"
            f"<p>You can also use the mouse to zoom in and out. Use the scroll wheel to zoom in and out.</p>"
            "<br>"
            f"<p><span style='font-weight: bold;'>Please zoom {zoom_in_out_} at least {zoom_count} times</span></p>"
            "</div>"
        )

        prompt = TimeoutPrompt(
            text=text,
            timeout=time_estimate,
            show_rounds=False,
        )
        super().__init__(
            label="modify_screen_size",
            prompt=prompt,
            control=ModifyScreenSizeControl(
                zoom_in_out=zoom_in_out,
                zoom_count=zoom_count,
            ),
            time_estimate=self.time_estimate,
            show_next_button=False,
        )

    
########################################################
# Drag and drop coins page
########################################################

class OuterProposalTutorialControl(NullControl):
    macro = "outer_proposal_tutorial"
    external_template = "outer_proposal_tutorial.html"

    def __init__(self, avatar: str = "me"):
        super().__init__()
        self.avatar = avatar
        self.show_next_button = False


class OuterProposalTutorial(ModularPage):

    def __init__(
        self,
        avatar: str = "me",
        time_estimate: int = TIMEOUT_PROPOSALS,
    ):
        self.time_estimate = time_estimate
        assert avatar in ["me", "partner"], "avatar must be either 'me' or 'partner'"

        avatar_ = f"<span style='font-weight: bold;'>{avatar.upper()}</span>"

        super().__init__(
            label="drag_and_drop_coins",
            prompt=TimeoutPrompt(
                text=f"Drag and drop the coins onto the {avatar_} avatar: ",
                timeout=time_estimate,
                show_rounds=False,
            ),
            control=OuterProposalTutorialControl(
                avatar=avatar,
            ),
            time_estimate=time_estimate,
        )