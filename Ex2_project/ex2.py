import rsa
import os

def clear_terminal():
    """Xóa màn hình terminal"""
    os.system('cls' if os.name == 'nt' else 'clear')

class RSASystem:
    """Hệ thống mã hóa RSA với quản lý khóa từ file"""
    
    def __init__(self):
        self.alice_pub = None
        self.alice_priv = None
        self.bob_pub = None
        self.bob_priv = None
        
    def case_a_tao_cap_khoa(self, key_size=2048):
        """
        Case A: Tạo cặp khóa công khai – bí mật cho Alice và Bob, lưu ra file
        """
        print("\n" + "=" * 60)
        print("CASE A: TẠO CẶP KHÓA VÀ LƯU RA FILE")
        print("=" * 60)
        
        print("\n1. Tạo khóa cho Alice...")
        (self.alice_pub, self.alice_priv) = rsa.newkeys(key_size)
        
        with open("alice_public.pem", 'wb') as f:
            f.write(self.alice_pub.save_pkcs1('PEM'))
        with open("alice_private.pem", 'wb') as f:
            f.write(self.alice_priv.save_pkcs1('PEM'))
        
        print(f"   ✓ Đã tạo và lưu khóa Alice ({key_size} bits)")
        print(f"   - Khóa công khai: alice_public.pem")
        print(f"   - Khóa bí mật: alice_private.pem")
        
        print("\n2. Tạo khóa cho Bob...")
        (self.bob_pub, self.bob_priv) = rsa.newkeys(key_size)
        
        with open("bob_public.pem", 'wb') as f:
            f.write(self.bob_pub.save_pkcs1('PEM'))
        with open("bob_private.pem", 'wb') as f:
            f.write(self.bob_priv.save_pkcs1('PEM'))
        
        print(f"   ✓ Đã tạo và lưu khóa Bob ({key_size} bits)")
        print(f"   - Khóa công khai: bob_public.pem")
        print(f"   - Khóa bí mật: bob_private.pem")
        
        input("\nNhấn Enter để tiếp tục...")
        
    def case_b_ma_hoa_cho_bob(self):
        """
        Case B: Alice mã hóa văn bản chỉ Bob mới đọc được
        """
        print("\n" + "=" * 60)
        print("CASE B: MÃ HÓA VĂN BẢN CHỈ BOB ĐỌC ĐƯỢC")
        print("=" * 60)
        
        van_ban = input("\nNhập văn bản cần mã hóa: ").strip()
        if not van_ban:
            print("✗ Văn bản không được để trống!")
            input("\nNhấn Enter để tiếp tục...")
            return
        
        print("\n1. Đọc khóa công khai của Bob...")
        duong_dan_bob_pub = input("   Nhập đường dẫn file khóa công khai Bob (Enter = bob_public.pem): ").strip()
        if not duong_dan_bob_pub:
            duong_dan_bob_pub = "bob_public.pem"
        
        try:
            with open(duong_dan_bob_pub, 'rb') as f:
                self.bob_pub = rsa.PublicKey.load_pkcs1(f.read())
            print(f"   ✓ Đã đọc khóa từ: {duong_dan_bob_pub}")
        except Exception as e:
            print(f"   ✗ Lỗi: {e}")
            input("\nNhấn Enter để tiếp tục...")
            return
        
        print("\n2. Mã hóa văn bản...")
        message_bytes = van_ban.encode('utf-8')
        encrypted = rsa.encrypt(message_bytes, self.bob_pub)
        
        with open("encrypted_message.bin", 'wb') as f:
            f.write(encrypted)
        
        print(f"   ✓ Đã mã hóa thành công!")
        print(f"   ✓ Đã lưu bản mã vào: encrypted_message.bin")
        print(f"   - Độ dài bản mã: {len(encrypted)} bytes")
        
        print("\n3. Bob giải mã...")
        duong_dan_bob_priv = input("   Nhập đường dẫn file khóa bí mật Bob (Enter = bob_private.pem): ").strip()
        if not duong_dan_bob_priv:
            duong_dan_bob_priv = "bob_private.pem"
        
        try:
            with open(duong_dan_bob_priv, 'rb') as f:
                self.bob_priv = rsa.PrivateKey.load_pkcs1(f.read())
            
            decrypted = rsa.decrypt(encrypted, self.bob_priv).decode('utf-8')
            print(f"   ✓ Văn bản sau khi giải mã: {decrypted}")
        except Exception as e:
            print(f"   ✗ Lỗi khi giải mã: {e}")
        
        input("\nNhấn Enter để tiếp tục...")
        
    def case_c_xac_nhan_ban_quyen(self):
        """
        Case C: Alice ký văn bản, bất kỳ ai có public key Alice đều xác nhận được
        """
        print("\n" + "=" * 60)
        print("CASE C: XÁC NHẬN BẢN QUYỀN")
        print("=" * 60)
        
        print("\n--- BƯỚC 1: ALICE KÝ VĂN BẢN ---")
        
        van_ban = input("\nNhập văn bản cần ký: ").strip()
        if not van_ban:
            print("✗ Văn bản không được để trống!")
            input("\nNhấn Enter để tiếp tục...")
            return
        
        print("\n1. Đọc khóa bí mật của Alice...")
        duong_dan_alice_priv = input("   Nhập đường dẫn file khóa bí mật Alice (Enter = alice_private.pem): ").strip()
        if not duong_dan_alice_priv:
            duong_dan_alice_priv = "alice_private.pem"
        
        try:
            with open(duong_dan_alice_priv, 'rb') as f:
                self.alice_priv = rsa.PrivateKey.load_pkcs1(f.read())
            print(f"   ✓ Đã đọc khóa từ: {duong_dan_alice_priv}")
        except Exception as e:
            print(f"   ✗ Lỗi: {e}")
            input("\nNhấn Enter để tiếp tục...")
            return
        
        print("\n2. Alice ký văn bản bằng private key...")
        message_bytes = van_ban.encode('utf-8')
        signature = rsa.sign(message_bytes, self.alice_priv, 'SHA-256')
        
        with open("signature.sig", 'wb') as f:
            f.write(signature)
        with open("original_text.txt", 'w', encoding='utf-8') as f:
            f.write(van_ban)
        
        print(f"   Đã tạo chữ ký thành công!")
        print(f"   Đã lưu chữ ký vào: signature.sig")
        print(f"   Đã lưu văn bản gốc vào: original_text.txt")
        print(f"   Độ dài chữ ký: {len(signature)} bytes")
        
        print("\n--- BƯỚC 2: BẤT KỲ AI XÁC NHẬN BẰNG PUBLIC KEY ALICE ---")
        
        duong_dan_alice_pub = input("\nNhập đường dẫn khóa công khai Alice (Enter = alice_public.pem): ").strip()
        if not duong_dan_alice_pub:
            duong_dan_alice_pub = "alice_public.pem"
        
        try:
            with open(duong_dan_alice_pub, 'rb') as f:
                alice_pub = rsa.PublicKey.load_pkcs1(f.read())
            print(f"✓ Đã đọc khóa công khai từ: {duong_dan_alice_pub}")
        except Exception as e:
            print(f"✗ Lỗi đọc khóa: {e}")
            input("\nNhấn Enter để tiếp tục...")
            return
        
        print("\n3. Xác minh chữ ký bằng public key Alice...")
        try:
            hash_method = rsa.verify(message_bytes, signature, alice_pub)
            print(f"\n   ✓✓✓ XÁC NHẬN THÀNH CÔNG! ✓✓✓")
            print(f"   - Văn bản này DO ALICE VIẾT")
            print(f"   - Văn bản KHÔNG BỊ THAY ĐỔI sau khi ký")
            print(f"   - Phương thức hash: {hash_method}")
        except rsa.VerificationError:
            print(f"\n   ✗✗✗ XÁC NHẬN THẤT BẠI! ✗✗✗")
            print(f"   - Văn bản KHÔNG PHẢI của Alice")
            print(f"   - HOẶC văn bản đã bị THAY ĐỔI")
        
        input("\nNhấn Enter để tiếp tục...")


def main():
    system = RSASystem()
    
    while True:
        clear_terminal()
        
        print("\n" + "=" * 60)
        print("HỆ THỐNG MÃ HÓA RSA")
        print("=" * 60)
        print("\nMENU CHÍNH")
        print("=" * 60)
        print("a. Tạo cặp khóa công khai – bí mật cho Alice và Bob")
        print("b. Mã hóa văn bản chỉ Bob mới đọc được")
        print("c. Xác nhận bản quyền văn bản của Alice")
        print("0. Thoát")
        print("=" * 60)
        
        lua_chon = input("\nNhập lựa chọn (a/b/c/0): ").strip().lower()
        
        if lua_chon == 'a':
            system.case_a_tao_cap_khoa()
        
        elif lua_chon == 'b':
            system.case_b_ma_hoa_cho_bob()
        
        elif lua_chon == 'c':
            system.case_c_xac_nhan_ban_quyen()
        
        elif lua_chon == '0':
            clear_terminal()
            print("\nĐã thoát!")
            break
        
        else:
            print("✗ Lựa chọn không hợp lệ!")
            input("\nNhấn Enter để tiếp tục...")


if __name__ == "__main__":
    main()
