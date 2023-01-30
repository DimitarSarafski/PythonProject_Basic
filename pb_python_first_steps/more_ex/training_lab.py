w = float(input())
h = float(input())
w_in_centimeters = int(w * 100)
h_in_centimeters = int(h * 100)

h_without_doorway = h_in_centimeters - 100
h_free_space = int(h_without_doorway / 70)
w_free_space = int(w_in_centimeters / 120)
total_space = (h_free_space * w_free_space) - 3

print(total_space)
