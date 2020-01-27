from Dictionary.Word import Word
from MorphologicalAnalysis.MorphologicalParse import MorphologicalParse


class DisambiguatedWord(Word):

    __parse: MorphologicalParse

    """
    The constructor of {@link DisambiguatedWord} class which takes a str and a MorphologicalParse
    as inputs. It creates a new MorphologicalParse with given MorphologicalParse. It generates a new instance with
    given str.
     *
     * @param name  Instances that will be a DisambiguatedWord.
     * @param parse {@link MorphologicalParse} of the {@link DisambiguatedWord}.
    """
    def __init__(self, name: str, parse: MorphologicalParse):
        super().__init__(name)
        self.__parse = parse

    """
    Accessor for the MorphologicalParse.

    RETURNS
    -------
    MorphologicalParse
        MorphologicalParse.
    """
    def getParse(self) -> MorphologicalParse:
        return self.__parse
