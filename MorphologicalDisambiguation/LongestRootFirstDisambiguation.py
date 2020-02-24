from MorphologicalDisambiguation.DisambiguationCorpus import DisambiguationCorpus
from MorphologicalDisambiguation.MorphologicalDisambiguator import MorphologicalDisambiguator


class LongestRootFirstDisambiguation(MorphologicalDisambiguator):

    def train(self, corpus: DisambiguationCorpus):
        """
        Train method implements method in MorphologicalDisambiguator.

        PARAMETERS
        ----------
        corpus : DisambiguationCorpus
            DisambiguationCorpus to train.
        """
        pass

    def disambiguate(self, fsmParses: list) -> list:
        """
        The disambiguate method gets an array of fsmParses. Then loops through that parses and finds the longest root
        word. At the end, gets the parse with longest word among the fsmParses and adds it to the correctFsmParses
        list.

        PARAMETERS
        ----------
        fsmParses : list
            FsmParseList to disambiguate.

        RETURNS
        -------
        list
            CorrectFsmParses list.
        """
        correctFsmParses = []
        for fsmParseList in fsmParses:
            maxLength = -1
            bestParse = None
            for i in range(fsmParseList.size()):
                if len(fsmParseList.getFsmParse(i).getWord().getName()) > maxLength:
                    maxLength = len(fsmParseList.getFsmParse(i).getWord().getName())
                    bestParse = fsmParseList.getFsmParse(i)
            if bestParse is not None:
                correctFsmParses.append(bestParse)
        return correctFsmParses

    def saveModel(self):
        pass

    def loadModel(self):
        pass