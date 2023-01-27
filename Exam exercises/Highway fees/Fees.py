##
from colorama import Fore, init
init()

def main():

    with open("fees.txt") as file_fees, open("Tracks.txt") as file_tracks:
        fees_raw = [i.strip().rsplit(";", 1) for i in file_fees]
        tracks = [i.strip().split(";") for i in file_tracks]

    fees = {i[0]: float(i[1]) for i in fees_raw}
    total_stops = {i.split(";")[0] for i in fees}.union({i.split(";")[1] for i in fees})

    results = {}
    for track in tracks:

        start_fee, end = track
        total_track = "-".join(track)
        # start_fee = start
        results[total_track] = [0.0, 0]
        for _ in fees:

            if start_fee not in total_stops or end not in total_stops:
                results[total_track]: list | str = "path not available"
                break

            next_stop = list(filter(lambda x: start_fee == x.split(";")[0], list(fees.keys())))[0]

            start_fee = next_stop.split(";")[1]

            cost = fees[next_stop]
            results[total_track][0] += cost
            results[total_track][1] += 1
            if start_fee == end: break

        if results[total_track] != "path not available":
            print(f"Track {total_track}: {results[total_track][1]} posts, total cost of {round(results[total_track][0], 2)}$")

        else:
            print(f"Track {total_track}:", Fore.RED, results[total_track], Fore.RESET)
            results.pop(total_track)

    cheapest_track = min(results, key=lambda x: results[x][0])
    print(f"\nCheapest track: {cheapest_track}, with a cost of {results[cheapest_track][0]}$")


if __name__ == '__main__':
    main()