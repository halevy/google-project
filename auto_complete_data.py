
class AutoCompleteData:

    def __init__(self, sentence, source, offset, score = 0):
        self.completed_sentence = sentence
        self.source_text = source
        self.offset = offset
        self.score = score
