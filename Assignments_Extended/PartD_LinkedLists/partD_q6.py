# Part D - Q6: Favorites List ADT


class FavoritesList:
    class _Record:
        def __init__(self, key):
            self.key = key
            self.hits = 0

    def __init__(self):
        self._records = []

    def access(self, key):
        for rec in self._records:
            if rec.key == key:
                rec.hits += 1
                return
        new_rec = self._Record(key)
        new_rec.hits = 1
        self._records.append(new_rec)

    def remove(self, key):
        for i, rec in enumerate(self._records):
            if rec.key == key:
                self._records.pop(i)
                return True
        return False

    def top(self, k):
        sorted_recs = sorted(self._records, key=lambda r: r.hits, reverse=True)
        return [(r.key, r.hits) for r in sorted_recs[:k]]


if __name__ == "__main__":
    favs = FavoritesList()
    for site in ["python.org", "github.com", "python.org", "docs.python.org", "python.org", "github.com"]:
        favs.access(site)

    print("Top 2 entries:")
    for url, visits in favs.top(2):
        print(f"  {url}: {visits} visits")

    favs.remove("python.org")
    print("\nTop after removing python.org:")
    for url, visits in favs.top(2):
        print(f"  {url}: {visits} visits")
