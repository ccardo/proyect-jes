##

def main():

    try:
        with open("artists.txt") as file_1:
            lines_1 = [i.strip().split(";") for i in file_1]
            artists = {line[1]: line[0] for line in lines_1}
    except IOError:
        quit("File not found.")

        years = {}
        for filename in artists:

            artist_id = artists[filename]
            try:
                with open(filename) as band_file:
                    songs = [i.strip().split(";") for i in band_file]
            except IOError:
                quit("File not found.")

            order_songs_by_year(songs, artist_id, years)

    for year in sorted(years):
        print(f"\n{year}:")
        for song in years[year]:
            print(f"{song[0]:<35}{song[1]}")


def order_songs_by_year(songs, artist, songs_by_year: dict):

    for song in songs:
        year, title = song

        if year not in songs_by_year:
            songs_by_year.update({year: [(title, artist)]})
        else:
            songs_by_year[year].append((title, artist))


if __name__ == '__main__':
    main()