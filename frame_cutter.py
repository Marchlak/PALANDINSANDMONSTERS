from PIL import Image

def wytnij_klatki( liczba_klatek, wysokosc_klatki):
    # Wczytaj obraz
    original_image = Image.open('assets/animations/skeleton/Death.png')

    # Oblicz szerokość klatki
    szerokosc_obrazu = original_image.width
    szerokosc_klatki = szerokosc_obrazu // liczba_klatek

    # Lista do przechowywania wyciętych klatek
    frames = []

    for i in range(liczba_klatek):
        # Oblicz pozycję startową każdej klatki
        left = i * szerokosc_klatki
        top = 0
        right = left + szerokosc_klatki
        bottom = top + wysokosc_klatki

        # Wytnij klatkę
        frame = original_image.crop((left, top, right, bottom))
        frames.append(frame)

        # Zapisz klatkę jako nowy plik
        frame.save(f'assets/animations/skeleton/frame_death_{i}.png')

# Przykład użycia
wytnij_klatki( 4, 150)