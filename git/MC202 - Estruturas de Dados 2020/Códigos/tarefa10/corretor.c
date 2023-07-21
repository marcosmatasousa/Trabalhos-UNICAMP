#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "corretor.h"

int main(){
    int n, q;
    char palavra[50];
    p_hash dicionario = criar_hash();
    p_hash erros = criar_hash();
    scanf("%d %d", &n, &q);

    for(int i = 0; i < n; i++){
        scanf("%s", palavra);
        inserir(dicionario, palavra);
        letra_menos(erros, palavra);
        letra_mais(erros, palavra);
        letra_trocada(erros, palavra);
    }
    for(int i = 0; i < q; i++){
        scanf("%s", palavra);
        if(busca_dicionario(dicionario, palavra) == 1){
            printf("verde\n");
        }
        else if(busca_dicionario(erros, palavra) == 1){
            printf("amarelo\n");
        }
        else{
            printf("vermelho\n");
        }
    }
    destruir_hash(erros);
    destruir_hash(dicionario);
}
