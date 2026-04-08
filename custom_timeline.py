from psynet.timeline import Timeline, PageMakerFinishedError
from psynet.utils import get_logger, log_time_taken
from psynet.timeline import Page, PageMaker

logger = get_logger()


class CustomTimeline(Timeline):

    def __init__(self, *args):
        super().__init__(*args)
        logger.info(f"CustomTimeline: {vars(self)}")

    @staticmethod
    def go_to_end(participant):
        logger.info(
            f"==>>>>: Participant {participant.id} failed the round"
        )
        participant.var.round_failed = True
        logger.info(f"{participant.var}")

    @staticmethod
    def get_round_failed(participant):
        logger.info(f"{participant.var}")
        if participant.var.has("round_failed"):
            logger.info("OOOOOOOKKKKKKK")
            return getattr(participant.var, "round_failed")
        else:
            return False

    @log_time_taken
    def advance_page(self, experiment, participant):
        round_failed = CustomTimeline.get_round_failed(participant)

        logger.info(
            f"==>>>>: Round failed is {round_failed} for participant {participant.id}"
        )

        if round_failed:
            last_page_id = len(self.elts['main']) - 1
            logger.info(
                f"=====>: Last page id: {last_page_id}"
            )
            participant.elt_id[-1] = last_page_id

        else:
            finished = False
            while not finished:
                participant.elt_id[-1] += 1

                try:
                    new_elt = self.get_current_elt(experiment, participant)
                except PageMakerFinishedError:
                    participant.elt_id = participant.elt_id[:-1]
                    participant.elt_id_max = participant.elt_id_max[:-1]
                    continue
                if isinstance(new_elt, PageMaker):
                    participant.elt_id.append(-1)
                    continue

                new_elt.consume(experiment, participant)

                if isinstance(new_elt, Page):
                    finished = True

