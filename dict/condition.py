from collections import defaultdict
lat_eng = defaultdict(list)
for i in range(int(input())):
    eng, lat_translate_part = input().split(' - ')
    lat_translate = lat_translate_part.split(', ')
    for lat in lat_translate:
        lat_eng[lat].append(eng)

print(len(lat_eng))
for lat, eng_translate in sorted(lat_eng.items()):
    print(lat + ' - ' + ', '.join(eng_translate))
