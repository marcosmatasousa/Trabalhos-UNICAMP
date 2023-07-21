#include "shortest_path.hpp"

using namespace std;

int main(void) {
    int n, Q;
    scanf("%d %d", &n, &Q);
    int *p = new int[n];
    int *v = new int[n];
    int *q = new int[n];

    int a, b, c;
    int niveis = 0;
    for(int i = 0; i < n; i++){
        scanf("%d %d %d", &a, &b, &c);
        v[i] = a;
        p[i] = b;
        q[i] = c;
        niveis += q[i];
    }

    int** vertices = new int*[Q+1];
    for(int i = 0; i < Q+1; ++i)
        vertices[i] = new int[niveis];
    
    Grafo g = Grafo();
    int s = g.adicionaVertice();
    for(int j = 0; j < niveis; j++){
        for(int i = 0; i <= Q; i++){
           vertices[i][j] = g.adicionaVertice();
        }
    }

    g.adicionaArco(s, 1, 0);
    g.adicionaArco(s, vertices[v[0]][0], p[0]);

    int count = 1;
    int select = 0;
    for(int j = 0; j < niveis - 1; j++){
        for(int i = 0; i <= Q; i++){
            
            if(count == q[select]){
                select++;
                count = 0;
            }
            
            g.adicionaArco(vertices[i][j], vertices[i][j + 1], 0);

            if((i + v[select] <= (Q))){
                g.adicionaArco(vertices[i][j], vertices[i + v[select]][j + 1], p[select]);
           }
        }
        count++;
    }


    int *dist = g.caminhoMinimo(0, vertices[Q][niveis - 1]);
    if(dist[vertices[Q][niveis - 1]] == 2147483647){
        int j = niveis - 1;
        for(int i = Q - 1; i > 0; i--){
            if(i < Q && dist[vertices[i][j]] != 2147483647){
                printf("%d %d\n", i, dist[vertices[i][j]]);
                break;
            }
        }
    }
    else{
        cout << dist[vertices[Q][niveis - 1]] << endl;
    }

    free(dist);
    return 0;
}