total_minutes = int(input("Entrez le nombre de minutes écoulées depuis le début du mois : "))
minutes_par_jour = 24 * 60
jours_ecoules = total_minutes // minutes_par_jour
reste_minutes = total_minutes % minutes_par_jour
jour_du_mois = jours_ecoules + 1

heure = reste_minutes // 60
minute = reste_minutes % 60

print(f"La date associée est : Jour {jour_du_mois}, à {heure:02d}h{minute:02d}")
