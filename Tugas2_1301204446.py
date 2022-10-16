amount = 8
service_time = 9
pick_up = "yes"

#untuk menentukan jumlah barang yang akan diservis
if amount == 1 or amount == 2:
    add = 0
    base_fee = 50
elif amount >= 3 or amount <= 10:
    add = 10 * amount
    base_fee = 100
elif amount > 10:
    add = 10 * amount
    base_fee = 500

#untuk menentukan biaya jam kerja
if service_time < 8 and service_time > 17:
    base_fee = base_fee * 2

if pick_up == "yes":
    base_fee = base_fee / 2

base_fee = base_fee + add
print("total fee yang didapat", base_fee)