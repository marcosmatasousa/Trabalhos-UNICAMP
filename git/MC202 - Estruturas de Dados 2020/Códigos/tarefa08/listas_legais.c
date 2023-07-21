#include <stdlib.h>
#include <stdio.h>
#include "listas_legais.h"

int main(){
    int n, k, op;
    unsigned long long int num;
    p_no esq = NULL;
    p_no dir = NULL;
    p_no raiz = NULL;
    int count; 
    int resultado = 0;
    scanf("%d %d", &n, &k);
    
    int i;
    for(i = 0; i < n; i++){
        count = 0;
        scanf("%llu", &num);
        if(i == 0){
            raiz = criar_arvore(num, esq, dir);
            raiz->ocorrencias += 1;
        }        
        else{
            if(!esta_na_arvore(raiz, num, count)){
                raiz = inserir_casca(raiz, num);
            }
            incrementar_ocorrencia(raiz, num);
        }
    }
    for(int j = 0; j < k; j++){
        scanf("%d", &op);
        
        if(op == 1){
            count = 0;
            scanf("%llu", &num);
            if(!esta_na_arvore(raiz, num, count)){
                raiz = inserir_casca(raiz, num);
            }
            incrementar_ocorrencia(raiz, num);
        }

        if(op == 2){
            scanf("%llu", &num);
            num_ocorrencias(raiz, num);
        }

        if(op == 3){
            resultado = percorre(raiz);
            printf("%d\n", resultado);
        }
    }
    destroi(raiz);
    return 0;
}