#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "corretor.h"

p_no criar_lista(){
    return NULL;
}

p_no inserir_lista(p_no lista, char *palavra){
    p_no novo;
    novo = malloc(sizeof(No));
    novo->palavra[0] = '\0';
    strcpy(novo->palavra, palavra);
    novo->prox = lista;
    return novo;
}

void destruir_lista(p_no lista){       
    if (lista != NULL){
        destruir_lista(lista->prox);
        free(lista);
    }
}

p_hash criar_hash(){
    p_hash lista_hash = malloc(sizeof(Hash));
    for(int i = 0; i < MAX; i++)
        lista_hash->vetor[i] = criar_lista();
    return lista_hash;
}

void destruir_hash(p_hash t){
    for(int i = 0; i < MAX; i++)
        destruir_lista(t->vetor[i]);
    free(t);
}

int hash(char *palavra){
    int i, n = 0;
    for(i = 0; i < strlen(palavra); i++)
        n = (256 * n + palavra[i]) % MAX;
    return n;
}

void inserir(p_hash t, char *palavra){
    int n = hash(palavra);
    t->vetor[n] = inserir_lista(t->vetor[n], palavra);
}

int busca_dicionario(p_hash t, char *palavra){
    int n = hash(palavra);
    p_no aux = t->vetor[n];
    while(aux != NULL){
        if(strcmp(aux->palavra, palavra) == 0)
            return 1;
        else
            aux = aux->prox;
    }
    return 0;
}

void letra_menos(p_hash t, char *palavra){
    int o = strlen(palavra);
    char copia[50];
    for(int i = 0; i < o; i++){
        strcpy(copia, palavra);
        for(int j = i; copia[j] != '\0'; j++){
            copia[j] = copia[j + 1];
        }
        inserir(t, copia);
    }
}

void letra_mais(p_hash t, char *palavra){
    char copia[50];
    for(int i = 0; i < 50; i++){
        copia[i] = '\0';
    }
    int o = strlen(palavra);
    for(int k = 97; k <= 122; k++){
        for(int i = 0; i < o; i++){
            strcpy(copia, palavra);
            for(int j = o - 1; j >= i; j--){
                copia[j + 1] = copia[j];
            }
            copia[i] = k;
            inserir(t, copia);
        }
    }
}

void letra_trocada(p_hash t, char *palavra){
    char copia[50];
    int o = strlen(palavra);
    for(int i = 97; i <= 122; i++){
        for(int j = 0; j < o; j++){
            strcpy(copia, palavra);
            copia[j] = i;
            inserir(t, copia);
        }
    }
}