
class PhotoAlbum:
    current_page = 1
    snapshots = 0

    def __init__(self, pages: int) -> None:
        self.pages = pages
        self.photos = []
        for i in range(self.pages):
            self.photos.append([])

    @classmethod
    def from_photos_count(cls, photos_count: int):
        if photos_count > 4:
            photos_count = 4
        return cls(photos_count)

    def add_photo(self, label: str):
        if PhotoAlbum.current_page <= self.pages:
            if len(self.photos[PhotoAlbum.current_page - 1]) == 4:
                PhotoAlbum.current_page += 1
            current_slot = len(self.photos[PhotoAlbum.current_page - 1]) + 1
            self.photos[PhotoAlbum.current_page - 1].append(label)
            PhotoAlbum.snapshots += 1
            return f"{label} photo added successfully on page {PhotoAlbum.current_page} slot {current_slot}"
        return "No more free slots"

    def display(self) -> str:
        number_of_photos = PhotoAlbum.snapshots
        res = f"-----------\n"
        while number_of_photos:
            for sch in range(4):
                number_of_photos -= 1
                res += f"[] "
                if not number_of_photos:
                    break
            res.rstrip()
            res += "\n"
            res += f"-----------\n"

        return res


album = PhotoAlbum(2)
print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))
print(album.display())