#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Lista ligada de atendimentos
typedef struct NoInt{
    int dado;
    struct NoInt *prox;
} NoInt;
typedef NoInt * p_noint;

// Criar lista de atendimentos do paciente
p_noint criar_lista_atendimentos(){
    return NULL;
}

p_noint copia_lista_atendimentos(p_noint lista){
    p_noint novo;
    if(lista == NULL){
        return NULL;
    }
    novo = malloc(sizeof(NoInt));
    novo->dado = lista->dado;
    novo->prox = copia_lista_atendimentos(lista->prox);
    return novo; 
}

// Adicionar elemento a lista de atendimentos do paciente
p_noint adicionar_elemento_atendimentos(p_noint lista, int x){
    p_noint novo;
    novo = malloc(sizeof(NoInt));
    novo->dado = x; 
    novo->prox = lista;
    return novo;
}

p_noint remover_no(p_noint lista){
    p_noint r = lista->prox;
    free(lista);
    lista = r;
    return lista;
}

// Destruir lista de atendimentos do paciente
void destruir_lista_atendimentos(p_noint lista){       
    if (lista != NULL){
        destruir_lista_atendimentos(lista->prox);
        free(lista);
    }
}

// Inverter lista de atendimentos
p_noint inverter_lista_atendimentos(p_noint lista) {
    p_noint atual, ant, invertida = NULL;
    atual = lista;
    while(atual != NULL){
        ant = atual;
        atual = ant->prox;
        ant->prox = invertida;
        invertida = ant;
    }
    return invertida;
}

// Estrutura de um paciente, tipo 1 é normal, 2 é preferencial
typedef struct Paciente{
    char nome[50];
    int tipo;
    p_noint atendimentos, aux;
    int ordem;
} Paciente;

// Lista ligada de pacientes
typedef struct No {
    Paciente pessoa;
    struct No *prox, *ant;
} No;
typedef No *p_no;

// Fila deque
typedef struct Deque{
    p_no ini, fim;
} Deque;
typedef Deque *p_deque;

// Inicializador da fila
p_deque inicializa(){
    p_deque d = malloc(sizeof(Deque));
    d->ini = d->fim = NULL;
    return d;
}

void destruir_lista(p_no lista){
    if(lista != NULL){
        destruir_lista(lista->prox);
        free(lista);
    }
}

void destruir_fila(p_deque f){
    destruir_lista(f->ini);
    free(f);
}

// Inserir paciente no inicio
void insere_inicio(p_deque d, Paciente x){
    p_no novo = malloc(sizeof(No));
    novo->pessoa = x;
    novo->prox = d->ini;
    novo->ant = NULL;
    if(d->ini == NULL){
        d->fim = novo;
    }
    else{
        d->ini->ant = novo;
    }
    d->ini = novo;
}

// Inserir paciente no fim
void insere_fim(p_deque d, Paciente x){
    p_no novo = malloc(sizeof(No));
    novo->pessoa = x;
    novo->ant = d->fim;
    novo->prox = NULL;
    if(d->fim == NULL){
        d->ini = novo;
    }
    else{
        d->fim->prox = novo;
    }
    d->fim = novo;
}

// Remover paciente do inicio da fila
void remove_inicio(p_deque d){
    p_no r = d->ini;
    d->ini = r->prox;
    if(d->ini == NULL){
        d->fim = NULL;
    }
    else{
        d->ini->ant = NULL;
    }
    free(r);
}

// Verifica se um deque está vazio
int vazia(p_deque fila){
    if(fila->ini == NULL && fila->fim == NULL)
        return 1;
    return 0;
}

int ordem_chegada(const void * a, const void * b){
    if((*(Paciente *)a).ordem == ((*(Paciente *)b).ordem))
        return 0;
    else
        if((*(Paciente*)a).ordem < (*(Paciente*)b).ordem)
            return -1;
        else
            return 1;
}

int main(){
    p_deque vetor_filas[9];
    for(int i = 0; i < 9; i++){
        p_deque fila = inicializa();
        vetor_filas[i] = fila;
    }

    int hora = 8;
    int min = 0;

    int ordem = 1;
    int teste = 1;
    char tipo[50];
    int atendimento = 0;
    Paciente pessoa;
    while(scanf("\"%[^\"]\" ", pessoa.nome) != EOF){
        
        do{
            teste = scanf("%s", tipo);
            if(teste >= 1){
                if(tipo[0] == 'n'){
                    pessoa.tipo = 1;
                    break;
                }
                else{
                    pessoa.tipo = 2;
                    break;
                }
            }
        } while(teste >= 1);

        pessoa.ordem = ordem;

        p_noint lista = criar_lista_atendimentos();
        do{
            teste = scanf("%d", &atendimento);
            if(teste >= 1)
                lista = adicionar_elemento_atendimentos(lista, atendimento);
        } while(teste >= 1);
        pessoa.atendimentos = copia_lista_atendimentos(lista);
        pessoa.atendimentos = inverter_lista_atendimentos(pessoa.atendimentos);
        pessoa.aux = pessoa.atendimentos;
        destruir_lista_atendimentos(lista);
        
        
        if(pessoa.tipo == 1){
            insere_fim(vetor_filas[pessoa.aux->dado - 1], pessoa);
        }
        else{
            insere_inicio(vetor_filas[pessoa.aux->dado - 1], pessoa);
        }
        ordem++;
    }

int num;
char ha_pessoas = 1;
Paciente lista_espera[38]; //38 é o máximo que podem haver na lista de espera
while(ha_pessoas){
    int num_espera = 0;
        
        min += 10;
        if(min == 60){
            hora += 1;
            min = 0;
        }

        for(int i = 0; i < 9; i++){
            if(i == 0){
                num = 10;
            }
            else if(i == 1){
                num = 2;
            }
            else if(i == 2){
                num = 5;
            }
            else if(i == 3){
                num = 3;
            }
            else if(i == 4){
                num = 4;
            }
            else if(i == 5){
                num = 7;
            }
            else if(i == 6){
                num = 2;
            }
            else if(i == 7){
                num = 1;
            }
            else{
                num = 4;
            }

            while(vazia(vetor_filas[i]) == 0 && num > 0){
                    if(vetor_filas[i]->ini->pessoa.aux->prox == NULL){
                        if(hora < 10){
                            printf("0%d:", hora);
                        }
                        else{
                            printf("%d:", hora);
                        }
                        if(min < 10){
                            printf("00 ");
                        }
                        else{
                            printf("%d ", min);
                        }
                        printf("%s\n", vetor_filas[i]->ini->pessoa.nome);
                        destruir_lista_atendimentos(vetor_filas[i]->ini->pessoa.atendimentos);
                        remove_inicio(vetor_filas[i]);
                        num -= 1;
                    }
                    else{
                        vetor_filas[i]->ini->pessoa.aux = vetor_filas[i]->ini->pessoa.aux->prox;
                        lista_espera[num_espera] = vetor_filas[i]->ini->pessoa;
                        remove_inicio(vetor_filas[i]);
                        num_espera += 1;
                        num -= 1;
                    }
            }
        }

        qsort(lista_espera, num_espera, sizeof(Paciente), ordem_chegada);
        
        if(num_espera > 0){
            for(int k = 0; k < num_espera; k++){
                if(lista_espera[k].tipo == 1){
                    insere_fim(vetor_filas[lista_espera[k].aux->dado - 1], lista_espera[k]);
                }
                else{
                    insere_inicio(vetor_filas[lista_espera[k].aux->dado - 1], lista_espera[k]);
                }
            }
        }

        ha_pessoas = 0;
        for(int k = 0; k < 9; k++){
            if(vetor_filas[k]->ini != NULL){
                ha_pessoas = 1;
                break;
            }
        }
    }
    for(int k = 0; k < 9; k++){
        destruir_fila(vetor_filas[k]);
    }
    return 0;
}



