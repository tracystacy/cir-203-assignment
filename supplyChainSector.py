# 1. Create list of routes
routes = [
    "Nairobi-Mombasa", "Kisumu-Nairobi", "Nakuru-Eldoret",
    "Nairobi-Embu", "Nyeri-Nairobi", "Machakos-Kitui",
    "Nairobi-Kitengela", "Thika-Nairobi", "Garissa-Nairobi",
    "Narok-Nairobi"
]

# 2. Append and remove
routes.append("Mombasa-Kwale")        # add
routes.remove("Machakos-Kitui")       # remove

# 3. Sort alphabetically then reverse
routes.sort()
routes.reverse()
print("Sorted & reversed:", routes)

# 4. Count routes starting with 'N'
count_N = sum(r.startswith("N") for r in routes)
print("Routes starting with N:", count_N)

# 5. New list of routes longer than 10 chars
long_routes = [r for r in routes if len(r) > 10]
print("Routes longer than 10 chars:",long_routes)
