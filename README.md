# python-studies

## NumPy

- Criando array
- Operações com array
- Indexação e fatiamento

## Pandas


### Data Frame

Um DataFrame é uma estrutura de dados tabular bidimensional com rótulos (labels) nas colunas e nas linhas. Em Python, a biblioteca Pandas fornece a estrutura de DataFrame, que é amplamente utilizada para manipulação e análise de dados.

Principais características de um DataFrame:

Bidimensional: Os dados são organizados em linhas e colunas, formando uma tabela.

Rótulos de Linhas e Colunas: Cada linha e coluna em um DataFrame tem rótulos que podem ser usados para acessar os dados.

Flexibilidade nas Colunas: As colunas podem conter diferentes tipos de dados (números, strings, datas, etc.).

Operações Eficientes: Oferece operações eficientes para manipulação, limpeza e análise de dados.

Integração com NumPy: Baseado na biblioteca NumPy, o que permite a integração fácil com outras ferramentas de análise de dados e aprendizado de máquina.

Ler e Escrever em Diferentes Formatos: Pode ser facilmente lido e escrito em diferentes formatos, como CSV, Excel, SQL, etc.



### Describe


Essas estatísticas são resultado da função describe() aplicada a uma coluna específica de um DataFrame, neste caso, à coluna "Idade". Vamos entender o significado de cada uma dessas estatísticas:

count: Número total de observações não nulas na coluna. No exemplo, count é 3, o que significa que há três valores não nulos na coluna "Idade".

mean: A média dos valores na coluna. Neste caso, mean é 30.0, indicando que a média das idades é 30.0.

std (desvio padrão): Mede a dispersão dos valores em relação à média. Quanto maior o desvio padrão, mais dispersos estão os valores. No exemplo, std é 5.0.

min: O valor mínimo na coluna. min é 25.0, indicando que a menor idade na coluna é 25.0.

25% (primeiro quartil): Indica o valor abaixo do qual 25% dos dados na coluna estão. Neste caso, 25% é 27.5, ou seja, 25% das idades são menores ou iguais a 27.5.

50% (segundo quartil ou mediana): O valor abaixo do qual 50% dos dados estão. 50% é 30.0, indicando que a mediana das idades é 30.0.

75% (terceiro quartil): O valor abaixo do qual 75% dos dados estão. 75% é 32.5, ou seja, 75% das idades são menores ou iguais a 32.5.

max: O valor máximo na coluna. max é 35.0, indicando que a maior idade na coluna é 35.0.



## Biography

- "Introduction to Machine Learning with Python" por Andreas C. Müller e Sarah Guido