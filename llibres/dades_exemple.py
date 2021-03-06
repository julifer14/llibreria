# -*- coding: utf8 -*-
from llibres.models import Genere
from llibres.models import Titol
from llibres.models import Llibre
from django.contrib.auth.models import User
from usuaris.models import Perfil

def crea():
    #--------------------USUARIS---------------------------------
    pepe_usr = User.objects.create_user( 'pepe', 'pepe@bookshare.cat', 'pepe1' )
    jose_usr = User.objects.create_user( 'jose', 'jose@bookshare.cat', 'jose1' )
    pepa_usr = User.objects.create_user( 'pepa', 'pepa@bookshare.cat', 'pepa1' )
    oriol_usr = User.objects.create_user('oriol', 'oriol@bookshare.cat', 'oriol1')
    

    #------------------------GENERES------------------------------------
    fantasia = Genere()
    fantasia.nom = "Fantasia"
    fantasia.save()
    
    aventura = Genere()
    aventura.nom = "Aventura"
    aventura.save()

    terror = Genere()
    terror.nom = "Terror"
    terror.save()

    romantico = Genere()
    romantico.nom = "Romantico"
    romantico.save()
    
    historica = Genere()
    historica.nom = "Historica"
    historica.save()
    
    manuals = Genere()
    manuals.nom = "Manuals"
    manuals.save()
    #---------------------Titols---------------------------
    harrypotter = Titol()
    harrypotter.titol = "Harry Potter i la pedra filosofal"
    harrypotter.sinopsis = "Primer de Harry Potter"
    harrypotter.genere = fantasia
    harrypotter.idioma = "Català"
    harrypotter.save()

    amor = Titol(titol = "Amor Amor", sinopsis = "Llibre d'amor",idioma = "Català", genere = romantico)
    amor.save()

    grito = Titol(titol ="Grito", idioma = "Castellà", sinopsis ="Terror el grito",genere =terror)
    grito.save()
    
    hp2 = Titol(titol = "Harry Potter i la camara secreta", idioma = "Català",sinopsis="Segon any d'en Harry a Hogwarts", genere = fantasia)
    hp2.save()
    
    #-----------------------------Llibres-----------------
    harry2 = Llibre()
    harry2.isbn = "0000000000002"
    harry2.edicio = "Cinquena"
    harry2.editorial = "Empuries"
    harry2.titol = hp2
    harry2.propietari = Perfil.objects.get(usuari__username = 'oriol')
    harry2.estat = "disponible"
    harry2.save()
    
    harry1 = Llibre()
    harry1.isbn = "0000000000001"
    harry1.edicio = "Primera"
    harry1.editorial = "La Castellana"
    harry1.titol = harrypotter
    harry1.propietari = Perfil.objects.get(usuari__username = 'pepe')
    harry1.estat = "disponible"
    harry1.save()
    
    amor1 = Llibre(isbn = "0000000000002",edicio = "Segona",editorial = "La Catalana", titol = amor, propietari = pepa_usr.perfil, estat = "disponible")
    amor1.save()
    
    grito1 = Llibre(isbn = "0000000000003", edicio = "Tercera", editorial = "Maya", titol = grito, propietari = jose_usr.perfil,estat = "disponible" )
    grito1.save()
    
    