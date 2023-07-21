#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define strmax 20
#define nmax 100
#define mmax 100

int verifica_rec(char **matriz, char palavra[], int n, int m, int i, int j, int pos, int count){
    char aux = '$';
    int tamanho = strlen(palavra);
    if(count == tamanho){
        return 1;
    }
    
    if((i + 1 < n)){
        if(matriz[i + 1][j] == palavra[pos + 1]){
            aux = matriz[i + 1][j];
            matriz[i + 1][j] = 'x';
            if(verifica_rec(matriz, palavra, n, m, i + 1, j, pos + 1, count + 1) == 1){
                matriz[i + 1][j] = aux;
                return 1;
            }
            matriz[i + 1][j] = aux;
        }
    }

    if((i - 1 >= 0)){
        if(matriz[i - 1][j] == palavra[pos + 1]){
            aux = matriz[i - 1][j];
            matriz[i - 1][j] = 'x';
            if(verifica_rec(matriz, palavra, n, m, i - 1, j, pos + 1, count + 1) == 1){
                matriz[i - 1][j] = aux;
                return 1;
            }
            matriz[i - 1][j] = aux;
        }
    }

    if((j + 1 < m)){
        if(matriz[i][j + 1] == palavra[pos + 1]){
            aux = matriz[i][j + 1];
            matriz[i][j + 1] = 'x';
            if(verifica_rec(matriz, palavra, n, m, i, j + 1, pos + 1, count + 1) == 1){
                matriz[i][j + 1] = aux;
                return 1; 
            }
            matriz[i][j + 1] = aux;
        }
    
    }
    if((j - 1 >= 0)){
        if(matriz[i][j - 1] == palavra[pos + 1]){
            matriz[i][j - 1] = 'x';
            if(verifica_rec(matriz, palavra, n, m, i, j - 1, pos + 1, count + 1) == 1){
                matriz[i][j - 1] = aux;
                return 1;
            }
            matriz[i][j - 1] = aux;
        }
    }
    return 0;  
}

int main() {
    int i, n, m, q, sim = 0;
    char *palavra, **matriz, aux;
    scanf("%d %d %d", &n, &m, &q);
    
    matriz = malloc(n * sizeof(char *));
    for(i = 0; i < n; i++){
        matriz[i] = malloc(m * sizeof(char));
    }

    for(i = 0; i < n; i++){
        for(int j = 0; j < m; j++){
            scanf(" %c", &matriz[i][j]);
        }
    }
    
    for (int k = 0; k < q; k++){
        sim = 0;
        palavra = malloc(strmax * sizeof(char));
        scanf("%s", palavra);
    
        for (i = 0; i < n; i++){
            for(int j = 0; j < m; j++){
                if(matriz[i][j] == palavra[0]){
                    aux = matriz[i][j];
                    matriz[i][j] = 'x';
                    if(verifica_rec(matriz, palavra, n, m, i, j, 0, 1) == 1 && sim == 0){
                        printf("sim\n");
                        sim = 1;
                        break;
                    }
                    matriz[i][j] = aux;
                } 
            }
        }
        if(sim == 0){
            printf("nao\n");
        }
    free(palavra);
    }
    for(i = 0; i < n; i++)
        free(matriz[i]);
    free(matriz);
    return 0;
}
