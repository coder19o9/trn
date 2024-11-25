from googletrans import Translator

# Tarjimon obyekti yaratish
translator = Translator()

def translate(text, src_lang, dest_lang):
    """Matnni manba va maqsad tilga tarjima qilish"""
    try:
        translation = translator.translate(text, src=src_lang, dest=dest_lang)
        return translation.text
    except Exception as e:
        return f"Xato yuz berdi: {e}"

def main():
    print("Tarjima dasturiga xush kelibsiz!")
    while True:
        print("\nTanlang:")
        print("1. Uzb → En")
        print("2. En → Uzb")
        print("3. Ru → En")
        print("4. Ru → Uzb")
        print("5. En → Ru")
        print("6. Chiqish")
        
        choice = input("Tanlovingizni kiriting (1-6): ")

        if choice == '1':
            text = input("Tarjima qilinadigan matnni kiriting (Uzb → En): ")
            result = translate(text, 'uz', 'en')
            print(f"Tarjima: {result}")
        elif choice == '2':
            text = input("Tarjima qilinadigan matnni kiriting (En → Uzb): ")
            result = translate(text, 'en', 'uz')
            print(f"Tarjima: {result}")
        elif choice == '3':
            text = input("Tarjima qilinadigan matnni kiriting (Ru → En): ")
            result = translate(text, 'ru', 'en')
            print(f"Tarjima: {result}")
        elif choice == '4':
            text = input("Tarjima qilinadigan matnni kiriting (Ru → Uzb): ")
            result = translate(text, 'ru', 'uz')
            print(f"Tarjima: {result}")
        elif choice == '5':
            text = input("Tarjima qilinadigan matnni kiriting (En → Ru): ")
            result = translate(text, 'en', 'ru')
            print(f"Tarjima: {result}")
        elif choice == '6':
            print("Dasturdan chiqyapsiz...")
            break
        else:
            print("Noto'g'ri tanlov, iltimos, yana urinib ko'ring.")

if __name__ == "__main__":
    main()
