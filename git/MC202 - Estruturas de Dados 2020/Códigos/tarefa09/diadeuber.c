#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "diadeuber.h"

int main(){
    p_fp fila_espera = criar_filaprio(500);
    int fim = 0;
    int km_buscar = 0;
    int km_corrida = 0;
    Cliente pessoa;
    char op = '#';
    char coord;
    int em_transporte = 0;
    Cliente p_transp;
    int motorista_x = 0;
    int motorista_y = 0;
    int cancelamentos = 0;

    while(fim == 0){
        scanf(" %c", &op);
        if(op == 'A'){
            int i = 0;
            scanf("%s %lf", pessoa.nome, &pessoa.avaliacao);
            do{
                int neg = 0;
                scanf("%c", &coord);
                if(coord == ' '){
                    scanf("%c", &coord);
                    if(coord == '-'){
                        scanf("%c", &coord);
                        neg = 1;
                    }
                }
                if(coord != '\n')
                    coord = coord - '0';
                
                if(i == 0){
                    pessoa.local_x = coord;
                    if(neg == 1)
                        pessoa.local_x = pessoa.local_x * -1;
                }
                else if(i == 1){
                    pessoa.local_y = coord;
                    if(neg == 1)
                        pessoa.local_y = pessoa.local_y * -1;
                }
                else if(i == 2){
                    pessoa.destino_x = coord;
                    if(neg == 1)
                        pessoa.destino_x = pessoa.destino_x * -1;
                }
                else if(i == 3){
                    pessoa.destino_y = coord;
                    if(neg == 1)
                        pessoa.destino_y = pessoa.destino_y * -1;
                }
                i++;
            } while(coord != '\n');
            insere(fila_espera, pessoa);
            printf("Cliente %s foi adicionado(a)\n", pessoa.nome);
            
        }
        else if(op == 'F'){
            printf("A corrida de %s foi finalizada\n", p_transp.nome);
            em_transporte = 0;
        }
        else if(op == 'C'){
            cancelamentos++;
            char nome[50];
            scanf("%s", nome);
            cancelamento(fila_espera, nome);
            printf("%s cancelou a corrida\n", nome);
            //cancelou a viagem, retirar o cliente da fila de espera;
        }
        else if(op == 'T')
            fim = 1;

        if(fila_espera->n > 0 && em_transporte == 0){
            p_transp = extrai_maximo(fila_espera);
            em_transporte = 1;
            int x_buscar = motorista_x - p_transp.local_x;
            if(x_buscar < 0)
                x_buscar = x_buscar * -1;
            int y_buscar = motorista_y - p_transp.local_y;
            if(y_buscar < 0)
                y_buscar = y_buscar * -1;

            int x_corrida = p_transp.local_x - p_transp.destino_x;
            if(x_corrida < 0)
                x_corrida = x_corrida * -1;
            int y_corrida = p_transp.local_y - p_transp.destino_y;
            if(y_corrida < 0)
                y_corrida = y_corrida * -1;
                
            km_buscar += x_buscar + y_buscar;
            km_corrida += x_corrida + y_corrida;
            motorista_x = p_transp.destino_x;
            motorista_y = p_transp.destino_y; 
        }
    }
    printf("\n");
    int km_total = km_buscar + km_corrida;
    printf("Jornada finalizada. Aqui esta o seu rendimento de hoje\n");
    printf("Km total: %d\n", km_total);
    double bruto = (km_corrida * 1.40) + (7 * cancelamentos);
    printf("Rendimento bruto: %.2f\n", bruto);
    double despesas = ((km_total * 0.1) * 4.104) + 57;
    printf("Despesas: %.2f\n", despesas);
    double liquido = (0.75 * bruto) - despesas;
    printf("Rendimento liquido: %.2f\n", liquido);
    
    free(fila_espera->v);
    free(fila_espera);
    return 0;
}