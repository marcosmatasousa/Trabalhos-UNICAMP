#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <math.h>
#include "caminho.h"

p_no criar_lista(){
    return NULL;
}

void destruir_lista(p_no lista){
    if(lista != NULL){
        destruir_lista(lista->prox);
        free(lista);
    }
}

p_no adicionar_ponto(p_no lista, double coord_x, double coord_y){
    p_no novo;
    novo = malloc(sizeof(No));
    novo->coord_x = coord_x;
    novo->coord_y = coord_y;
    novo->visitado = 0;
    novo->prox = lista;
    return novo;
}

p_grafo criar_grafo(){
    p_grafo g = malloc(sizeof(Grafo));
    g->pokestops = criar_lista();
    g->lugias = criar_lista();
    return g;
}

void destruir_grafo(p_grafo g){
    destruir_lista(g->pokestops);
    destruir_lista(g->lugias);
    free(g);
}

void desvisitar(p_no pokestops){
    while(pokestops != NULL){
        pokestops->visitado = 0;
        pokestops = pokestops->prox;
    }
}

double distancia(double origem_x, double origem_y, double destino_x, double destino_y){
    double retorno;
    retorno = sqrt(pow((destino_x - origem_x), 2) + pow((destino_y - origem_y), 2));
    return retorno;
}

int caminhos(double atual_x, double atual_y, p_no pokestops, p_no poke_aux, p_no lugias, p_no lugias_aux, int teto){
    while(lugias != NULL){
        double dist = distancia(atual_x, atual_y, lugias->coord_x, lugias->coord_y);
        if(dist <= teto){
            return 1;
        }
        lugias = lugias->prox;
    }
    lugias = lugias_aux;
    while(pokestops != NULL){
        double dist = distancia(atual_x, atual_y, pokestops->coord_x, pokestops->coord_y);
        if(!pokestops->visitado && dist <= teto){
            pokestops->visitado = 1;
            if(caminhos(pokestops->coord_x, pokestops->coord_y, poke_aux, poke_aux, lugias, lugias_aux, teto) == 1){
                return 1;
            }
        }
        pokestops = pokestops->prox;
    }
    pokestops = poke_aux;
    return 0;
}