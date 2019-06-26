print('hello')

languages = ['Green', 'Blue', 'Orange']

for language in languages:
    print(language)

class Variant:

    def __init__(this, position, gene, reference, alternative):
        this.position = position
        this.gene = gene
        this.reference = reference
        this.alternative = alternative

variant = Variant(12, 14, 15, 18)
