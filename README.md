<h1>
    <img src="./README/shrek2img.jpg" />
<p>Não é o tamanho que importa, é o que você faz com isso.🐲</p>
</h1>

## 🧨 Sobre o projeto

Bem-vindo ao maravilhoso mundo de programação dos pântanos digitais com OgroScript, a linguagem de programação que mistura a robustez de códigos com a irreverência do reino de Tão Tão Distante. Projetada para ogros, burros e programadores audaciosos, **Shrek2** é a escolha ideal para aqueles que querem adicionar um toque de magia ogrosiana ao seu código.

## 🔨 Ferramentas

- [Python](https://www.python.org/downloads/)
- [VsCode](https://code.visualstudio.com)

## Como utilizar o projeto

```bash
    #Clone do projeto
    $ git clone https://github.com/Truer-Controller/Shrek2.git
```

```bash
    #Ler o arquivo de testes
    $ RUN("example.myopl")
```

## Como o Shrek2 Funciona?

Suas variaveis se encontram da seguinte forma para se utilizar:
```bash
  'Shrek',          #VAR
  'Farquaad',       #AND
  'Dragao',         #OR
  'GatoDeBotas',    #NOT       
  'SouUmOgro',      #IF
  'TalvezUmOgro',   #ELIF
  'OuNaoSouOgro',   #ELSE
  'AGenteJaChegou', #FOR
  'VaiPangare',     #TO
  'STEP',           #STEP
  'Distante',       #WHILE
  'Fada',           #FUN
  'Burrofobia',     #THEN
  'Enfezado',       #END
  'VemBurro',       #RETURN
  'AndaShrek',      #CONTINUE
  'Finalmente',     #BREAK
```
Essa é a representação das estruturas de código e o que cada um representa. Já os tokens utilizaveis são os:
```bash
TT_INT			= 'Burrinho'      #INT
TT_FLOAT    	= 'Ogro'          #FLOAT
TT_STRING		= 'Fiona'         #STRING
TT_POW			= 'Haroldo'       #POW (Potencia)
```
Nossa linguagem apresenta diversas operações matematicas podendo realizar multiplicações, divisões, somas e subtrações. O que não realizamos é o operador que é comum de se encontrar como "%" normalmente utilizado para mostrar o resto da divisão, shrek2 não utiliza desse operador. Alguns exemplos de como realizar as operações:

"BISCOITO" é o nosso famoso PRINT sendo assim mostrará para você no console o que está retornando das suas variaveis.
```bash
Shrek a = 5
BISCOITO(a)
Shrek b = 1.5
BISCOITO(b)
Shrek c = "teste string"
BISCOITO(c)
Shrek d = a + b
BISCOITO(d)
Shrek e = b - a
BISCOITO(e)
Shrek f = a / b
BISCOITO(f)
Shrek g = b * a
BISCOITO(g)
Shrek h = a ^ b
BISCOITO(h)
```
## Estrutura de repetição

Também apresentamos estruturas de repetição como o FOR que é representado da seguinte forma seguindo as orientações de declarações acima:
```bash
AGenteJaChegou i = 0 VaiPangare 5 Burrofobia
	BISCOITO("Estou no meu FOR")
Enfezado

Ou também você pode utilizar o While da seguinte forma!

Distante i < 10 Burrofobia Shrek i = i + 1
BISCOITO(i)
```
## Estrutura de compações

Shrek2 também trabalha com sistemas de comparação e alguns exemplos abaixo é como você pode estar utilizando o IF, ELIF e o ELSE:
```bash
SouUmOgro 5 == 5 Burrofobia BISCOITO("Essa condicao e verdadeira")

SouUmOgro 5 == 5 Farquaad 4 == 4 Burrofobia BISCOITO("Isso aqui nao deve ser printado se for falso")

SouUmOgro 5 == 6 Dragao 4 == 4 Burrofobia BISCOITO("Isso aqui deve ser printado mesmo se a primeira condicao e falsa")

SouUmOgro 5 >= 6 Burrofobia BISCOITO("FALSO") OuNaoSouOgro BISCOITO("Era pra eu cair no ELSE e fui certo")

Mais usualmente montamos em outras linguagens uma estrutura completa dessa forma também:

SouUmOgro a < 0 Burrofobia
	BISCOITO("positivo")
OuNaoSouOgro
	BISCOITO("negativo")
Enfezado
```
## Listas

Trabalhamos com a manipulação de listas também sendo adicionando itens em lista ou juntando seus indices conforme estrutura abaixo:
```bash
Shrek list1 = [1,2,3,4] + 4
BISCOITO(list1)
Shrek list2 = [1,2,3] * [3,4,5]
BISCOITO(list2)
```
## Funções básicas

Técnicas mais avançadas que se encontram nessa linguagem são funcionções que você pode validar o retorno no seu console como:
```bash
BISCOITO(MATH_PI)
BISCOITO(IS_NUM(123))
BISCOITO(IS_NUM("testerafa"))
BISCOITO(IS_LIST([]))
BISCOITO(IS_STR("Professor"))

Shrek list = [1,2,3,4]
APPEND(list, 5)
BISCOITO(list)

POP(list, 3)
BISCOITO(list)

EXTEND(list, [6,7,8])
BISCOITO(list)
```
## Quebra de linha(delimitador)

Caso você deseje printar mais de uma informação por linha ou simplesmente separar seu codigo é opcional a utilização do ponto e virgula:

SouUmOgro 5 == 5 Burrofobia; BISCOITO("FALSO"); BISCOITO("VERDADEIRO") OuNaoSouOgro BISCOITO("teste limitador")

## Funções!

Porem um dos maiores destaques da linguagem shrek2 é a utilização de funções complexas que nós mesmos podemos criar, como por exemplo as funções abaixo que unem strings concatenando as mesmas:

```bash
Fada oopify(prefix) -> prefix + "oop"

Fada join(elements, separador)
	Shrek resultado = ""
	Shrek len = LEN(elements)

	AGenteJaChegou i = 0 VaiPangare len Burrofobia
		Shrek resultado = resultado + elements/i
		SouUmOgro i != len - 1 Burrofobia Shrek resultado = resultado + separador
	Enfezado
	VemBurro resultado
Enfezado

Fada map(elements, func)
	Shrek new_elements = []

	AGenteJaChegou i = 0 VaiPangare LEN(elements) Burrofobia
		APPEND(new_elements, func(elements/i))
	Enfezado
	
	VemBurro new_elements
Enfezado

AGenteJaChegou i = 0 VaiPangare 5 Burrofobia
	BISCOITO(join(map(["l", "sp"], oopify), ", "))
Enfezado
```

## Geração de erros❌

Para gerar erros lexicais nessa linguagem basta inserir caracteres que não cumprimos como operadores ternarios ?? ou até mesmo como informado acima resto de divisão % segue o erro abaixo que retorna no console caso realize alguma tentativa dessa

<img src="./README/errolexicos.png" />

Já para gerar um erro sintatico basta escrever de forma errada a sintaxe do projeto seja inserindo um token errado de posição ou a forma de como escrever uma estrutura de condição

<img src="./README/errosintatico.png" />

<img src="./README/errosintatico2.png" />

Já um erro semantico não quer dizer que está faltando algo no seu código como algum simbolo ou notação até mesmo estrutura porem a logica declarada que realizou logicamente está errado por isso do erro semantico

<img src="./README/errosemantico.png" />

E por fim o erro esperado onde estamos tentando acessar a estrutura do codigo em outro bloco, por exemplo estou tentando acessar a variavel resultado que foi declarado em uma função em outra estrutura de bloco

<img src="./README/erroblocos.png" />

