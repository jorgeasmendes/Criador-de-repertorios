# Criador de repertórios musicais

Um projeto de estudo em Python para auxiliar músicos profissionais e amadores a terem seus repertórios organizados e criarem setlists de forma rápida e direcionada para cada ocasião.


## ⚙️ Funcionalidades
1- No programa é possível armazenar as músicas em um banco de dados, de forma simples e organizada por meio de categorias (compositor, artista de referência, tonalidade, gênero, subgênero, andamento, clima e tema da letra) para posterior consulta.\n
2-Além disso, é possível associar as músicas a cifras ou letras, que podem ser baixadas instantaneamente dos sites cifraclub.com.br e letras.com.\n
(Obs: esse é um projeto de estudo, sem pretensões comerciais ou de uso amplo. Realizei webscrap nos referidos sites, mas em uma possível implementação futura procurarei o uso de APIs oficiais.)\n
3-Por fim, será possível criar setlists escolhendo o número de músicas e definindo parâmetros, como por exemplo: 
Setlist com 20 músicas; sendo 10 sambas e 10 forrós; 5 lentas, 5 rápidas e 10 muito rápidas; 10 com o tema brasilidades e 10 com o tema amor; etc.
O programa crirá automaticamente o repertório com os parâmetros indicados e ainda incluirá as letras/cifras na ordem correspondente, salvando tudo em um arquivo doc.\n
(Esta funcionalidade 3 está em fase de desenvolvimento).

## 🛠️ Construído com
* [Python] Linguagem de programação
* [Tkinter] Para criar a Interface Gráfica
* [Pandas] Para manipular os dados da tabela armazenada em csv
* [Beautiful Soup] Para fazer webscraping nos sites de cifras e letras
