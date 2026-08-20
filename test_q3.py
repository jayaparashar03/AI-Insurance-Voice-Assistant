from bot import answer

def run_case(country, text):
    print("="*60)
    print(country.upper())
    print("Customer:", text)
    print("Bot:", answer(country, text))

cases = [
    ("philippines","Magkano ang premium?"),
    ("philippines","What is a beneficiary?"),
    ("philippines","What is covered by my policy?"),
    ("indonesia","Berapa tenor pinjaman?"),
    ("indonesia","Saya belum bisa bayar cicilan."),
    ("indonesia","Berapa DP?")
]

for c in cases:
    run_case(*c)