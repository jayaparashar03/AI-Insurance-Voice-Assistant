from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

def read_market_notes(country):
    file_path = BASE_DIR / country / "knowledge.md"
    return file_path.read_text(encoding="utf-8")

def detect_market_language(text):
    msg = text.lower()

    tagalog_words = {
        "magkano","salamat","opo","po","ako","ko",
        "bahay","insurance","premium","beneficiary"
    }

    indonesia_words = {
        "berapa","terima","kasih","saya","anda",
        "cicilan","tenor","dp","pinjaman"
    }

    if any(word in msg for word in tagalog_words):
        return "philippines"

    if any(word in msg for word in indonesia_words):
        return "indonesia"

    return "english"

def answer(country, customer_text):

    lang = detect_market_language(customer_text)

    customer_text = customer_text.lower()

    if country == "philippines":

        if "premium" in customer_text or "magkano" in customer_text:
            return ("Ang premium ay depende sa plan at eligibility. "
                    "Maaaring tulungan ka ng representative sa quote.")

        if "beneficiary" in customer_text:
            return ("Ang beneficiary ay ang taong makakatanggap ng insurance benefits.")

        if "coverage" in customer_text:
            return ("Ang coverage ay depende sa napiling policy. "
                    "Maaaring ipaliwanag ito ng representative.")

        return ("Salamat sa iyong tanong. "
                "Tutulungan ka naming makipag-ugnayan sa representative.")

    if country == "indonesia":

        if "tenor" in customer_text:
            return ("Tenor tergantung produk pembiayaan yang dipilih.")

        if "dp" in customer_text:
            return ("DP tergantung jenis pembiayaan dan proses verifikasi.")

        if "cicilan" in customer_text:
            return ("Kami dapat membantu menjelaskan opsi cicilan dan menghubungkan Anda dengan petugas.")

        return ("Terima kasih. Kami akan membantu menghubungkan Anda dengan petugas.")

    return "Market not supported."