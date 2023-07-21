#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <math.h>
#include "caminho.h"

int main(){
    double inicio_x, inicio_y;
    char tipo[50]; //pokestop ou lugia
    scanf("%lf %lf", &inicio_x, &inicio_y);
    int teste = 1;
    double coord_x, coord_y;
    p_grafo unicamp = criar_grafo();
    double maior_distancia = 0;

    do{
        teste = scanf("%lf %lf", &coord_x, &coord_y);
        if(teste >= 1){
            scanf("%s", tipo);
            if(tipo[0] == 'p'){
                unicamp->pokestops = adicionar_ponto(unicamp->pokestops, coord_x, coord_y);
            }
            else{
                unicamp->lugias = adicionar_ponto(unicamp->lugias, coord_x, coord_y);
            }
            double dist = (distancia(inicio_x, inicio_y, coord_x, coord_y));
            if (dist > maior_distancia){
                maior_distancia = dist;
            }
        }
    } while(teste >= 1);

    maior_distancia = floor(maior_distancia);
    int teto;
    int achar_caminho = 1;
    for(teto = maior_distancia; achar_caminho == 1; teto--){
        achar_caminho = caminhos(inicio_x, inicio_y, unicamp->pokestops, unicamp->pokestops, 
        unicamp->lugias, unicamp->lugias, teto);
        if(achar_caminho == 0){
            break;
        }
        desvisitar(unicamp->pokestops);
    }
    printf("%d", teto + 1);
    destruir_grafo(unicamp);
    return 0;
}