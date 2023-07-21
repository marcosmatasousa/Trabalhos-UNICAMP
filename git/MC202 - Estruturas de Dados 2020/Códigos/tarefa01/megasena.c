#include <stdio.h>
#define MAX 15
#define MAXM 1000
// adicionar o maximo array, testar
void imprime_premio(int n, int matriz_jogadas[][MAX], double premio, int lista_numeros[]){
    
    double faixa1 = 0;
    double faixa2 = 0;
    double faixa3 = 0;
    int apostadores[MAXM];
    // substituir o n pelo maximo
    for (int i = 0; i < n; i++){
        int acertos = 0;
        for (int j = 0; j < 6; j++){
            for(int k = 0; k < MAX; k++){
                if (lista_numeros[j] == matriz_jogadas[i][k]){
                    acertos++;
                }
            }
             
        }
        if (acertos == 4){
            faixa3++;
            apostadores[i] = 3;
        
        } else if (acertos == 5){
            faixa2++;
            apostadores[i] = 2;
        
        } else if (acertos == 6){
            faixa1++;
            apostadores[i] = 1;
        
        } else{
            apostadores[i] = 0;
        }
    }


    for (int i = 0; i < n; i++){
        if (apostadores[i] == 1){
            printf("%.2f\n", (0.62 * premio)/faixa1);
        
        }else if (apostadores[i] == 2){
            printf("%.2lf\n", (0.19 * premio)/ faixa2);
        
        }else if (apostadores[i] == 3){
            printf("%.2lf\n", (0.19 * premio)/ faixa3);
        
        }else if (apostadores[i] == 0){
            printf("%.2f\n", 0.00);
        }

    }
}


int main(){
    int n;
    double premio;
    int l[10];
    scanf("%d %lf", &n, &premio);
    int matriz_apostas[MAXM][MAX];
    int lista_numeros[6];

    for (int j = 0; j < n; j++){
        int contagem = 0;
        int coluna = 0;

        for (int i = 0; i < 6; i++){
            for (int k = 0; k < 10; k++){
                scanf("%d",&l[k]);
            }
        
        for(int y = 0; y < 10; y ++){
            if (l[y] == 1){
                matriz_apostas[j][coluna] = contagem + 1;
                coluna++;
            }
            contagem++;
            }
        }
        for (; coluna < MAX; coluna ++){
            matriz_apostas[j][coluna] = 0;
        } 

    }
    for (int i = 0; i < 6; i ++){
        scanf("%d", &lista_numeros[i]);
    }
    imprime_premio(n, matriz_apostas, premio, lista_numeros);
    // teste
}