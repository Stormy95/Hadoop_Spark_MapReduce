from mrjob.job import MRJob

class MRAnagram(MRJob):

    def mapper(self, _, line):
        # On convertit les mots en liste de lettre minuscule puis on ordonne cette liste
        letters = list(str(line).lower())
        letters.sort()

        # on utilise comme clé la liste de lettre ordonnée
        yield letters, line

    def reducer(self, _, words):
        # on renvoie les mots ayant au moins 2 anagrames en matchant par liste ordonnée
        anagrams = [w for w in words]
        if len(anagrams) > 1:
            yield len(anagrams), anagrams


if __name__ == "__main__":
    MRAnagram.run()