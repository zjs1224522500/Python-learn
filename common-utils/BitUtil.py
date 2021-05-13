version_lock = 0
UNLOCKED_BIT = 0b11111110
CLIENT_BIT = 0b10000000

version_lock &= UNLOCKED_BIT
print("version_lock &= UNLOCKED_BIT : " + bin(version_lock))
version_lock += 1
print("version_lock += 1 : " + bin(version_lock))
current_version = version_lock
current_version += 1
print("current_version: " + bin(current_version))
print("version_lock & CLIENT_BIT : " + bin(version_lock & CLIENT_BIT))
print(bin(current_version | (version_lock & CLIENT_BIT)))

