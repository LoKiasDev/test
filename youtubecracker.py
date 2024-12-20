from pytube import YouTube

# Fonction pour télécharger une vidéo YouTube
def telecharger_video(url):
    try:
        # Créer un objet YouTube
        video = YouTube(url)
        
        # Obtenir le flux vidéo avec la meilleure résolution
        stream = video.streams.get_highest_resolution()
        
        # Télécharger la vidéo
        stream.download()
        print("Téléchargement terminé !")
    except Exception as e:
        print(f"Erreur : {e}")

# Exemple d'utilisation
url = input("Entrez l'URL de la vidéo YouTube : ")
telecharger_video(url)