# oi Meu amorzinho, se tu estiver isso, para aqui, não lê, é pra ser uma surpresa, te amo muito, tomara que tu goste
# URL do compilador deste codigo https://www.programiz.com/python-programming/online-compiler/


def ler_inteiro(mensagem, minimo=None, maximo=None):
  while True:
    try:
      valor = int(input(mensagem))
      if minimo is not None and valor < minimo:
        print(f"Por favor, digite um número maior ou igual a {minimo}.")
        continue
      if maximo is not None and valor > maximo:
        print(f"Por favor, digite um número menor ou igual a {maximo}.")
        continue
      return valor
    except ValueError:
      print("Entrada inválida. Digite apenas números.")


print("Meu amor, antes de começarmos, quero te fazer algumas perguntas :)")
str(input("Sabe quando tempo a gente ta junto meu amorzinho?  "))
str(input("Sabe mesmo? quanto tempo?  "))
print(
  "Pois é, todo esse tempo, e sabe de uma coisa? Esse ano e dois meses tem sido "
  "Os melhores 14 meses da minha vida \n TU É O MELHOR MOMENTO DESSA MINHA EXISTÊNCIA"
  "Adoro cada segundo que eu passo com você, cada risada, cada conversa, beijo, trapalhada, tudo"
  "Mas eu preciso saber também, então me diz:"
)

nivel_de_amor = ler_inteiro("De 1 a 10 qual teu nível de amor por mim hoje em dia? ", 1, 10)

if nivel_de_amor == 10:
  print(
    "HIIHHIHIIHIHIHIHIHHIIHHIHI EU TAMBÉM TE AMO ESSE TANTÃO\n"
    "Sinto muito tua falta sempre que estamos longe um dos outros"
  )
  print(
    "E faz 1 ano e 2 meses que nós nos conhecemos, que tempo maravilhoso"
    "por isso, para comemorar eu estava pensando em hoje te surpreender: "
    "hoje às 18:30 eu vou passar pra te buscar na sua casa e nós vamos ter "
    "um ótimo jantar. Prepare-se"
  )
  str(input("O que me diz? Aceita meu convite?"))
  print(
    "Eu poderia fazer um código pra saber sua resposta, mas eu sei que foi um sim, "
    "hihihiihhihihi\n Te vejo daqui a pouco meu amor"
  )
elif nivel_de_amor >= 7:
  print("Eu te amo mais, hihiihi, mas tudo bem, eu sempre vou te amar com todo meu coração")
  print(
    "E faz 1 ano e 2 meses que nós nos conhecemos, que tempo maravilhoso"
    "Por mais que tu não esteja tão ~in love~ comigo, acho que posso fazer algo pra melhorar um pouco a nossa situação"
    "por isso, para comemorar eu estava pensando em te surpreender, tu achava que eu tinha esquecido né?"
    "hoje às 18:30 eu vou passar pra te buscar na sua casa e nós vamos ter um ótimo jantar, e nosso date surpresa. Prepare-se"
  )
  str(input("O que me diz? Aceita meu convite? "))
  print(
    "Eu poderia fazer um código pra saber sua resposta, mas eu sei que foi um sim, "
    "hihihiihhihihi\n Te vejo daqui a pouco meu amor"
  )
else:
  print("QUE? Para aqui e me liga então, vamos conversar, o que aconteceu?"
        "tinha toda uma surpresa fofa feita e tudo mais, mas isso nao importa mais"
        "Vamos conversar, me diz o que houve?")