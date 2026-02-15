import cloudscraper
from bs4 import BeautifulSoup
import time

def extraer_videos_por_paginas(pag_inicio, pag_fin):
    # Inicializamos el scraper
    scraper = cloudscraper.create_scraper(browser={'browser': 'chrome','platform': 'linux','desktop': True})
    base_url = "https://123av.com/en/dm9/uncensored-leaked"
    
    # Abrimos el archivo en modo 'w' (write) para empezar de cero
    with open("solo_videos.txt", "w") as f:
        
        for i in range(pag_inicio, pag_fin + 1):
            url = f"{base_url}?page={i}"
            print(f"Buscando videos en página {i}...")
            
            # Escribimos el separador en el archivo
            f.write(f"--- PAGINA {i} ---\n")
            
            try:
                response = scraper.get(url)
                if response.status_code == 200:
                    soup = BeautifulSoup(response.text, 'html.parser')
                    links = soup.find_all('a', href=True)
                    
                    enlaces_de_esta_pag = set() # Usamos set para evitar duplicados dentro de la misma página
                    
                    for l in links:
                        href = l['href']
                        full_url = href if href.startswith('http') else f"https://123av.com{href}"
                        
                        # Aplicamos la corrección que pediste
                        if "https://123av.com/v/" in full_url or "https://123av.comv/" in full_url:
                            url_corregida = full_url.replace(".com/v/", ".com/en/v/").replace(".comv/", ".com/en/v/")
                            enlaces_de_esta_pag.add(url_corregida)
                    
                    # Escribimos los enlaces encontrados en esta página
                    for link in sorted(enlaces_de_esta_pag):
                        f.write(link + "\n")
                    
                    # Añadimos un salto de línea extra para separar de la siguiente sección
                    f.write("\n")
                    print(f"-> Se guardaron {len(enlaces_de_esta_pag)} videos de la página {i}.")
                
                else:
                    f.write(f"Error al acceder a la página {i} (Status {response.status_code})\n\n")
                    print(f"-> Error {response.status_code} en página {i}")
                
                # Pausa de cortesía
                time.sleep(2)
                
            except Exception as e:
                print(f"Error inesperado en página {i}: {e}")
                f.write(f"Error inesperado: {e}\n\n")

# --- CONFIGURACIÓN ---
inicio = 1
fin = 15
extraer_videos_por_paginas(inicio, fin)

print(f"\nProceso finalizado. Revisa 'solo_videos.txt' para ver los resultados divididos.")
