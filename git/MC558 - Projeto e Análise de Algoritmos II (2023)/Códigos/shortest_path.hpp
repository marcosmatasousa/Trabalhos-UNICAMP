#ifndef PATH_HPP
#define PATH_HPP

#include <ostream>
#include <climits>
#include <iostream>

typedef struct arco { // nó da lista de adjacências
    int u, v, peso;
    struct arco *proximo;
} Arco;

using namespace std;

class Grafo {

    /* para facilitar seu debug */
    friend ostream &operator<<(ostream &output, const Grafo &p);

public:
    int n; // número de nós
    int m; // tamanho do vetor de listas de adjacências
    Arco **arcos; // vetor de lista de adjacências

    /* cria um novo grafo vazio */
    Grafo();

    /* cria um novo grafo com n vértices */
    Grafo(int n);

    /* destruidor */
    ~Grafo();

    /* retorna o número de nós do grafo */
    int size();

    /* adiciona um vértice ao grafo
     * devolve o índice do novo vértice */
    int adicionaVertice();

    /* adiciona um arco de u a v com peso w
     * 0 <= u, v <= n-1  */
    void adicionaArco(int u, int v, int w);

    /* número de arcos do grafo */
    int numArcos();

    /* calcula um caminho mínimo de s a t num grafo sem ciclos orientados
     * devolve o custo de um caminho mínimo */
    int *caminhoMinimo(int s, int t);
};

#endif // PATH_HPP
