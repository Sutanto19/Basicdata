def nearest_to_zero(arr):
    # Jika array kosong
    if not arr:
        return 0
    
    #Inisialisasi nilai terdekat dengan elemen pertama array
    nearest = arr[0]
    
    for num in arr:
        # Cek angka yang paling dekat dengan 0
        if abs(num) < abs(nearest):
            nearest = num
        # Angka yang paling dekat, prefer positive value
        elif abs(num) == abs(nearest) and num > nearest:
            nearest = num
    
    return nearest

#Array
array = [-10, 5, 12, 32, -5]
print(nearest_to_zero(array))
