#include <stdlib.h>
#include <stdio.h>
#include "listas_legais.h"

p_no criar_arvore(unsigned long long int dado, p_no esq, p_no dir){
    p_no r = calloc(1, sizeof(No));
    r->dado = dado;
    r->esq = esq;
    r->dir = dir;
    return r;
}

int esta_na_arvore(p_no raiz, unsigned long long int dado, int count){
    if(raiz == NULL)
        return count;
    if(raiz->dado == dado)
         count += 1;
    if(dado < raiz->dado && raiz->esq != NULL)
        return(esta_na_arvore(raiz->esq, dado, count));
    if(dado > raiz->dado && raiz->dir != NULL)
        return(esta_na_arvore(raiz->dir, dado, count));
    return count;
}

void incrementar_ocorrencia(p_no raiz, unsigned long long int dado){
    if(raiz == NULL)
        return;
    else if(raiz->dado == dado)
        raiz->ocorrencias += 1;
    else if(dado < raiz->dado && raiz->esq != NULL)
        incrementar_ocorrencia(raiz->esq, dado);
    else if(dado > raiz->dado && raiz->dir != NULL)
        incrementar_ocorrencia(raiz->dir, dado);
}

void num_ocorrencias(p_no raiz, unsigned long long int dado){
    if (raiz == NULL)
        printf("0\n");
    else if(raiz->dado == dado)
        printf("%d\n", raiz->ocorrencias);
    else if(dado < raiz->dado)
        num_ocorrencias(raiz->esq, dado);
    else if(dado > raiz->dado)
        num_ocorrencias(raiz->dir, dado);
}

int percorre(p_no raiz){
    int count = 0;
    if(raiz != NULL){
        if(raiz->dado > raiz->ocorrencias)
            count += (raiz->ocorrencias);
        if(raiz->dado < raiz->ocorrencias)
            count += (raiz->ocorrencias - raiz->dado);
            
        count += percorre(raiz->esq);
        count += percorre(raiz->dir);
    }
    return count;
}

void destroi(p_no raiz){
    if(raiz != NULL){
        destroi(raiz->esq);
        destroi(raiz->dir);
        free(raiz);
    }
}

int eh_vermelho(p_no x){
    if(x == NULL)
        return 0;
    return x->cor == RED;
}

int eh_preto(p_no x){
    if(x == NULL)
        return 1;
    return x->cor == BLACK;
}

p_no rotaciona_esq(p_no raiz){
    p_no x = raiz->dir;
    raiz->dir = x->esq;
    x->esq = raiz;
    x->cor = raiz->cor;
    raiz->cor = RED;
    return x;
}

p_no rotaciona_dir(p_no raiz){
    p_no x = raiz->esq;
    raiz->esq = x->dir;
    x->dir = raiz;
    x->cor = raiz->cor;
    raiz->cor = RED;
    return x;
}

void sobe_vermelho(p_no raiz){
    raiz->cor = RED;
    raiz->esq->cor = BLACK;
    raiz->dir->cor = BLACK;
}

p_no inserir_rec(p_no raiz, unsigned long long int dado){
    p_no novo;
    if(raiz == NULL){
        novo = malloc(sizeof(No));
        novo->ocorrencias = 0;
        novo->esq = novo->dir = NULL;
        novo->dado = dado;
        novo->cor = RED;
        return novo;
    }
    if(dado < raiz->dado)
        raiz->esq = inserir_rec(raiz->esq, dado);
    else
        raiz->dir = inserir_rec(raiz->dir, dado);
    if(eh_vermelho(raiz->dir) && eh_preto(raiz->esq))
        raiz = rotaciona_esq(raiz);
    
    if(eh_vermelho(raiz->esq) && eh_vermelho(raiz->esq->esq))
        raiz = rotaciona_dir(raiz);
    
    if(eh_vermelho(raiz->esq) && eh_vermelho(raiz->dir))
        sobe_vermelho(raiz);
    
    return raiz; 
}

p_no inserir_casca(p_no raiz, unsigned long long int dado){
    raiz = inserir_rec(raiz, dado);
    raiz->cor = BLACK;
    return raiz;
}