## Benchmarking

Utlizando o caso de teste dado (2_3541687), chegamos ao seguinte resultado:


| Algoritmo      |  Nodos  Visitados  |  Tempo Médio  | Custo     |
|----------------|--------------------|---------------|-----------|
| A* Manhattan   | 289607             | 4.552s        | 23        |
| A* Hamming     | 278223             | 3.570s        | 23        | 
| BFS            | 258734             | 1.924s        | 23        |
| DFS            | Estouro de Pilha   | -             | -         |
| A* (Nossa H.)  | 253001             | 2.604s        | 23        |
| BFS MITM       |   4270             | 0.502s        | 23        |

Observamos que, em casos em que o espaço de busca é exponencial, a DFS pode continuar encontrando 
caminhos novos arbitrariamente, sem chegar a lugar algum. Experimentamos com a ideia de usar h(v)
como sendo a distância entre o espaço vazio "_" e seu lugar no estado final. Tivemos excelentes 
resultados assim.

Além disso, também empregamos a técnica chamada de Meet in the Middle, ideal para espaços exponenciais,
pois neles reduz a complexidade de 2^N para 2 * 2^(N/2), aplicando duas BFSs simultaneamente. Este foi,
de longe, nosso melhor resultado



