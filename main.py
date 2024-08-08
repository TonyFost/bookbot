def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        words = file_contents.split()

        characters = {}

        for w in words:
            
            for c in w.lower():
                if c in characters:
                    characters[c] += 1
                else:
                    characters[c] = 1

        print(f"Words = {len(words)}")
        print(f"Characters = {characters}")

        keyed_characters = [{"character": k, "count": characters[k]} for k in characters.keys() if k.isalpha()]

        keyed_characters.sort(reverse=True, key=sort_on)

        print("--- Begin report of books/frankenstein.txt ---")
        print(f"{len(words)} words found in the document")
        print("")
        for character in keyed_characters:
            c = character["character"]
            x = character["count"]
            print(f"The {c} character was found {x} times")
        print("--- End report ---")


def sort_on(dict):
    return dict["count"]



main()