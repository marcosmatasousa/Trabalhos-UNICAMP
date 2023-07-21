#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "diadeuber.h"

p_fp criar_filaprio(int tam){
    p_fp fprio = malloc(sizeof(FP));
    fprio->v = malloc(tam * sizeof(Cliente));
    fprio->n = 0;
    fprio->tamanho = tam;
    return fprio;
}

void troca(Cliente *a, Cliente *b){
    Cliente t = *a;
    *a = *b;
    *b = t;
}

void sobe_no_heap(p_fp fprio, int k){
    if(k > 0 && fprio->v[(k-1)/2].avaliacao < fprio->v[k].avaliacao){
        troca(&fprio->v[k], &fprio->v[(k-1)/2]);
        sobe_no_heap(fprio, (k-1)/2);
    }
}

void desce_no_heap(p_fp fprio, int k){
    int maior_filho;
    if((2*k+1) < fprio->n){
        maior_filho = (2*k+1);
        if((2*k+2) < fprio->n && fprio->v[(2*k+1)].avaliacao < fprio->v[2*k+2].avaliacao)
            maior_filho = (2*k+2);
        if(fprio->v[k].avaliacao < fprio->v[maior_filho].avaliacao){
            troca(&fprio->v[k], &fprio->v[maior_filho]);
            desce_no_heap(fprio, maior_filho);
        }
    }
}

void insere(p_fp fprio, Cliente pessoa){
    fprio->v[fprio->n] = pessoa;
    fprio->n += 1;
    sobe_no_heap(fprio, fprio->n - 1);
}

Cliente extrai_maximo(p_fp fprio){
    Cliente pessoa = fprio->v[0];
    troca(&fprio->v[0], &fprio->v[fprio->n - 1]);
    fprio->n--;
    desce_no_heap(fprio, 0);
    return pessoa;
}

void cancelamento(p_fp fprio, char nome[50]){
    int i;
    for(i = 0; i < fprio->n - 1; i++){
        if(strcmp(fprio->v[i].nome, nome) == 0)
            break;
    }
    troca(&fprio->v[i], &fprio->v[fprio->n - 1]);
    fprio->n--;
    desce_no_heap(fprio, 0);
}