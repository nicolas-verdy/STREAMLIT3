import streamlit as st
from streamlit_authenticator import Authenticate
from streamlit_option_menu import option_menu

# ========================
# Configuration des données utilisateurs
# ========================
lesDonneesDesComptes = {
    'usernames': {
        'NicolasVerdy': {
            'name': 'VERDY Nicolas', 
            'password': 'Jules2014',
            'email': 'utilisateur@gmail.com',
            'role': 'utilisateur'
        },
        'root': {
            'name': 'root',
            'password': 'rootMDP',
            'email': 'admin@gmail.com',
            'role': 'administrateur'
        },
        'MarieDupont': {
            'name': 'DUPONT Marie',
            'password': 'Marie123!',
            'email': 'marie.dupont@example.com',
            'role': 'utilisateur'
        },
        'utilisateur': {
            'name': 'utilisateur',
            'password': 'utilisateurMDP',
            'email': 'utilisateur@example.com',
            'role': 'utilisateur'
        },
        'JeanMartin': {
            'name': 'MARTIN Jean',
            'password': 'JeanPass2024',
            'email': 'jean.martin@example.com',
            'role': 'utilisateur'
        },
        'AliceLemoine': {
            'name': 'LEMOINE Alice',
            'password': 'AlicePwd!',
            'email': 'alice.lemoine@example.com',
            'role': 'utilisateur'
        }
    }
}

# ========================
# Authentification
# ========================
authenticator = Authenticate(
    lesDonneesDesComptes, 
    "cookie_name",  # Nom du cookie
    "cookie_key",   # Clé du cookie
    30              # Durée en jours du cookie
)

authenticator.login()

st.write("User et mdp sont : utilisateur  ")

# ========================
# Page principale
# ========================
def accueil():
    """Page d'accueil pour les utilisateurs connectés"""
    st.title("Bienvenue sur le contenu réservé aux utilisateurs connectés")
    st.image("Hello.jpg")  


def page_photos():
    st.title("Des bonnes têtes de Vainqueurs !")
    # Création des colonnes pour afficher les photos
    col1, col2, col3, col4 = st.columns(4)

    photos = [("Leslie", "image4.jpeg"), ("Nico", "image5.jpeg"), 
              ("Ludo", "image6.jpeg"), ("Daniel", "image7.jpeg")]
    
    for col, (nom, image) in zip([col1, col2, col3, col4], photos):
        with col:
            st.header(nom)
            st.image(image, width=150)


# ========================
# Barre latérale
# ========================
def barre_laterale():
    """Configuration de la barre latérale"""
    authenticator.logout("Déconnexion", "sidebar")

    st.sidebar.title("CHOIX :")
    
    # Choix de l'affichage : 
    affichage_sel  = st.sidebar.selectbox(
        "Que souhaitez-vous afficher ?",
        ["Accueil", "Photos"]
    )
    if affichage_sel == "Accueil":
        accueil()
        

    if affichage_sel == "Photos":
        page_photos()
        

  

# ========================
# Lancement du programme
# ========================
if __name__ == "__main__":
    if st.session_state.get("authentication_status"):
        barre_laterale()
        
    elif st.session_state.get("authentication_status") is False:
        st.error("L'username ou le password est incorrect")
    elif st.session_state.get("authentication_status") is None:
        st.warning("Les champs username et mot de passe doivent être remplis")


    # lancer le code    streamlit run Streamlit3.py
