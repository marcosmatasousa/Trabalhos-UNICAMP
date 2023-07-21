#include "shortest_path.hpp"

/* a lista de adjacências cresce exponencialmente -- amortizado constante */
#define TAMANHO_INICIAL 1024

using namespace std;

// Grafo: -------------------------------------------------------------------------------
void aumentaVetor(Grafo &g) {
    if (g.m >= g.n) return;
    while (g.m < g.n)
        g.m *= 2;
    g.arcos = (Arco **) realloc(g.arcos, g.m * sizeof(Arco *));
}

Grafo::Grafo() : n(0), m(TAMANHO_INICIAL) {
    this->arcos = (Arco **) calloc(this->m, sizeof(Arco *));
}

Grafo::Grafo(int _n) : n(_n), m(TAMANHO_INICIAL) {
    for (; this->m < this->n; this->m *= 2); // calcula o tamanho inicial do vetor
    this->arcos = (Arco **) calloc(this->m, sizeof(Arco *));
}

void destroiListaCPP(Arco *head) {
    if (head != nullptr) {
        destroiListaCPP(head->proximo);
        free(head);
    }
}

Grafo::~Grafo() {
    for (int i = 0; i < this->n; i++)
        destroiListaCPP(this->arcos[i]);
    free(this->arcos);
}

int Grafo::adicionaVertice() {
    this->n++;
    aumentaVetor(*this);
    this->arcos[this->n - 1] = nullptr;
    return this->n - 1;
}

int Grafo::size() {
    return this->n;
}

void Grafo::adicionaArco(int u, int v, int w) {
    Arco *e = (Arco *) malloc(sizeof(Arco));
    e->u = u;
    e->v = v;
    e->peso = w;
    e->proximo = this->arcos[u];
    this->arcos[u] = e;
}

int Grafo::numArcos() {
    int ret = 0;
    for (int i = 0; i < this->n; i++)
        for (Arco *e = this->arcos[i]; e != nullptr; e = e->proximo, ret++);
    return ret;
}

ostream &operator<<(ostream &output, const Grafo &g) {
    output << "# vértices: " << g.n << endl;
    for (int i = 0; i < g.n; i++) {
        output << i << ": ";
        for (Arco *e = g.arcos[i]; e != nullptr; e = e->proximo)
            output << "(" << e->u << ", " << e->v << ", " << e->peso << ") ";
        output << endl;
    }
    return output;
}

// Caminho Mínimo: ----------------------------------------------------------------------
void _ordTop(Grafo &g, int u, short visitado[], int pilha[], int *topo) {
    visitado[u] = 1;
    for (Arco *e = g.arcos[u]; e != nullptr; e = e->proximo)
        if (!visitado[e->v])
            _ordTop(g, e->v, visitado, pilha, topo);
    pilha[++(*topo)] = u;
}

void ordTop(Grafo &g, int pilha[]) {
    int topo = -1;
    auto *visitado = (short *) calloc(g.n, sizeof(short));
    for (int i = 0; i < g.n; i++)
        if (!visitado[i])
            _ordTop(g, i, visitado, pilha, &topo);
    free(visitado);
}

int *Grafo::caminhoMinimo(int s, int t) {
    int *pilha = (int *) malloc(this->n * sizeof(int));
    int *dist = (int *) malloc(this->n * sizeof(int));
    ordTop(*this, pilha);

    // Inicializa as distâncias:
    for (int i = 0; i < this->n; i++)
        dist[i] = INT_MAX;
    dist[s] = 0;

    // Calcula as distâncias usando programação dinâmica:
    int topo = this->n;
    while (topo > 0) {
        int u = pilha[--topo];
        if (dist[u] != INT_MAX)
            for (Arco *e = this->arcos[u]; e != nullptr; e = e->proximo)
                if (dist[u] + e->peso < dist[e->v])
                    dist[e->v] = dist[u] + e->peso;
    }

    free(pilha);
    return dist;
}
