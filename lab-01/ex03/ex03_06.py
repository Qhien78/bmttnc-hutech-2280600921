def xoa_phan_tu(dictionary, key):
    if(key in dictionary):
        return True
    else:
        return False
my_dict ={'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4}
key_to_del = 'b'
result = xoa_phan_tu(my_dict, key_to_del)
if result:
    print("Phan tu da duoc xoa tu dictionary", my_dict)
else:
    print("Khong tim thay phan tu can xoa trong dictionary")