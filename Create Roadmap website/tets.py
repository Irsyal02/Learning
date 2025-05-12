def nyalakan_lampu(ruangan, kecerahan):
  """Menyalakan lampu di ruangan tertentu dengan tingkat kecerahan tertentu.

  Args:
    ruangan: Nomor ruangan (1, 2, 3, dst.).
    kecerahan: Tingkat kecerahan (0-7).
  """
  global status_lampu
  mask = (1 << (ruangan - 1)) * kecerahan
  status_lampu |= mask

def matikan_lampu(ruangan):
  """Mematikan lampu di ruangan tertentu."""
  mask = ~(1 << (ruangan - 1))
  status_lampu &= mask

def cek_kerusakan(ruangan):
  """Mengecek apakah lampu di ruangan tertentu rusak."""
  mask = 1 << (ruangan - 1)
  return bool(status_lampu & mask) and (status_lampu & (mask << 3)) == 0

# Inisialisasi status lampu semua ruangan (misalnya, hanya ruangan 1 dan 3 yang menyala dengan kecerahan maksimal)
status_lampu = 255  # Biner: 11111111

# Menyalakan lampu di ruangan 2 dengan kecerahan sedang
nyalakan_lampu(2, 4)

# Mematikan lampu di ruangan 1
matikan_lampu(1)

# Mengecek kerusakan lampu di ruangan 2
print("Lampu di ruangan 2 rusak:", cek_kerusakan(2))

# Menampilkan status semua lampu (untuk debugging)
print(bin(status_lampu))