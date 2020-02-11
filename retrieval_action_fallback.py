from rasa.nlu.components import Component
import logging


# Create a custom logger
logger = logging.getLogger(__name__)


class ResponseThreshold(Component):
    """A custom response selector component to add minimum threshold"""
    name = "response_threshold"
    defaults = {}
    language_list = ["en"]
    print('initialised the class')

    def __init__(self, component_config=None):
        super(ResponseThreshold, self).__init__(component_config)

    def train(self, training_data, cfg, **kwargs):
        """Load the sentiment polarity labels from the text
           file, retrieve training tokens and after formatting
           data train the classifier."""
        pass

    def process(self, message, **kwargs):
        """Retrieve the tokens of the new message, pass it to the classifier
            and append prediction results to the message class."""
        # get the intent to check if it is a retrieval action
        intent = message.get("intent")
        response_ranking = message.get("response_selector")

        # check the threshold for predicted responses [change here for different intent, DEFAULT='faq']
        if intent['name'] == 'faq':
            # [change here to set threshold for default message to trigger, DEFAULT=0.8]
            if response_ranking['default']['response']['confidence'] < 0.8:
                logger.info(f"In custom nlu component, confidence of response selector is {response_ranking['default']['response']['confidence']} which is less than threshold.\n Triggering fallback.")
                response_ranking['default']['response']['name'] = "Low Confidence, show default message"
                intent['confidence'] = 0.0
            message.set("intent", intent, add_to_output=True)
            message.set("response_ranking", response_ranking, add_to_output=True)
