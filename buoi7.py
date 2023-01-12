"""
Cho hai tập hợp (set)
art_students = {"John", "Max", "Anna", "Bob", "Obito"}
math_students = {"Max", "Mery", "David", "Anna", "Naruto", "John"}
a.Tìm những người bạn học cả vẽ lẫn toán
b.Tìm những người bạn học vẽ nhưng không học toán
c.Tìm những người bạn học toán nhưng không học vẽ
d..Tìm những người bạn học vẽ hay toán không phải cả hai
e.Tìm tất cả những người
"""
art_students = {"John", "Max", "Anna", "Bob", "Obito"}
math_students = {"Max", "Mery", "David", "Anna", "Naruto", "John"}
#a
math_art = art_students.intersection(math_students)
print(math_art)
#b
art_no_math = art_students.difference(math_students)
print(art_no_math)
#c
math_no_art = math_students.difference(art_students)
print(math_no_art)
#d
art_or_math = art_students.symmetric_difference(math_students)
print(art_or_math)
#e
all = art_students.union(math_students)
print(all)

"""
2
Yêu cầu:
a.Lấy ra giá trị của các key sau: album_name, release_year bằng hai cách
b.Thay đổi giá trị của key: release_year từ 1973 thành 1971
c.Xóa phần tử với key là track_list
d.Thêm một key mới là amount = 2000 bằng hai cách
e.Làm trống dict: album_info
"""
album_info = {
    "album_name": "The Dark Side of the Moon",
    "band": "Pink Floyd",
    "release_year": 1973,
    "track_list": [
        "Speak to Me",
        "Breathe",
        "On the Run",
        "Time",
        "The Great Gig in the Sky",
        "Money",
        "Us and Them",
        "Any Colour You Like",
        "Brain Damage",
        "Eclipse"
    ]
}
#a
print(album_info["album_name"])
print(album_info.get("album_name"))

print(album_info["release_year"])
print(album_info.get("release_year"))
#b
import json

album_info["release_year"] = 1971
print(json.dumps(album_info, indent=4))
#c
del album_info["track_list"]
print(json.dumps(album_info, indent=4))
#d
album_info["amount"] = 2000
album_info.update(amount=2000)

print(json.dumps(album_info, indent=4))
#e
album_info.clear()
print(album_info)