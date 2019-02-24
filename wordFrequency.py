wordstring = '''Lorem ipsum dolor sit amet, veri repudiandae signiferumque id est, 
id ius populo sententiae. Per ei nemore invenire disputando, corpora blandit eum no. 
Vix purto primis at, legimus vivendo adversarium sed eu, everti postulant qui ea. Summo 
aeterno deterruisset ius in, duo sonet pertinax intellegat ei, at dolorum urbanitas 
duo. No eam numquam postulant, cum consul latine dignissim et, ea maiestatis philosophia 
nec. Duo aliquid suscipiantur ea, mollis probatus duo ei.

Possim splendide democritum ei est, ad viris sapientem usu. Etiam incorrupte concludaturque 
an has, ei nonumy timeam nostrud sit. Pro te erat saepe inimicus. Per saepe nusquam no, 
at alterum praesent vis.

Pri at esse inimicus, sumo dolorum id sit. Et sea case adipisci similique, doming impedit 
concludaturque ex usu. Eam nulla oratio an, per perfecto consectetuer voluptatibus no, 
alii labitur consequat an eum. Putent vidisse mei an, ipsum labores molestiae cum in. 
Hinc elitr per cu, discere euismod erroribus quo ei, reque tation facete sea an. Eligendi 
adipiscing scriptorem eos ex.

Cum et duis persius delicatissimi. Sed elit scaevola mandamus id. Facete laboramus an duo, 
ad pri purto nemore timeam. Ut qui debitis eligendi intellegebat, ad vim dicta adversarium 
ullamcorper. Quo labitur gubergren eu, periculis comprehensam cu vel.

Id duis ocurreret pro. Dolore constituto no per. Ludus ocurreret usu ea. Omnesque offendit 
atomorum id mei. Wisi quaerendum eos at, dicit dolor utinam ad nam. Dicam feugiat noluisse 
vix in, at eirmod reprehendunt per, nec sonet propriae tacimates ea. Eum modo esse dicunt 
ei, ea malis diceret posidonium eum, vis ut aeque torquatos.'''

wordlist = wordstring.split()

wordfreq = [wordlist.count(w) for w in wordlist]

print("String\n {} \n".format(wordstring))
print("List\n {} \n".format(str(wordlist)))
print("Frequencies\n {} \n".format(str(wordfreq)))
print("Pairs\n {}".format(str(dict(zip(wordlist, wordfreq)))))