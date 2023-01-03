##
#

def main():

    # opening the "artists.txt" file
    filepath = "proyect-jes/Exam exercises/Discography/artists.txt"
    with open(filepath, "r") as artists_file:
        lines = [i.strip().split(";") for i in artists_file]
        bands  = {line[0]: line[1] for line in lines}
    
    # saving the songs by the year of their release
    songs_by_year = dict()
    for band_code in bands:

        band_songs = save_discography(f"proyect-jes/Exam exercises/Discography/{bands[band_code]}")
        releases_of_that_year = set()
        bands[band_code] = releases_of_that_year

        for song in band_songs:

            releases_of_that_year.add(song)
            year = band_songs[song]

            if year not in songs_by_year:
                songs_by_year.update({year: {song}})
            else:
                songs_by_year[year].add(song)
    
    # iterating over songs_by_year and printing all the songs with their band code
    for year in songs_by_year:

        print(f"\n{year}:")
        for song in songs_by_year[year]:
            
            band_code = [code for code in bands if song in bands[code]][0]
            print(f"{song:<40}{band_code}")


def save_discography(file_path: str) -> dict:

    """reads the file and returns a dict with format {song: year}"""

    try:
        with open(file_path, "r") as band:
            lines = [i.strip().split(";") for i in band]

    except IOError or OSError:
        exit("No file with this name has been found. Try again.")

    return {line[1]: int(line[0]) for line in lines}


if __name__ == "__main__":
    main()