##
# this function prints the given country name with the appropriate French article
#

def main():
    country = input("S'il vous plaît, écrivez un pays: ")

    exceptions = ['Belize', 'Cambodge', 'Mexique', 'Mozambique', 'Zimbabwe']
    pluralCountries = ['Etats-Unis', 'Pays-Bas']
    articles = ['le', 'la', "l'", 'les']
    vowels = 'aeiou'

    article = articles[0]
    if country[len(country) - 1] == 'e':
        article = articles[1]
        if country in exceptions:
            article = articles[0]
    if country[0].lower() in vowels:
        article = articles[2]
    if country in pluralCountries:
        article = articles[3]

    print(f"{article} {country}")


if __name__ == '__main__':
    main()
