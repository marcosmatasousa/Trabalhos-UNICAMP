#include <stdio.h>
#include <stdlib.h>

typedef struct No {
    int dado;
    struct No * prox;
} No;

typedef struct No * p_no;

p_no criar_lista(){
    return NULL;
}

void destruir_lista();

p_no copia_lista(p_no lista){
    p_no novo;
    if(lista == NULL){
        return NULL;
    }
    novo = malloc(sizeof(No));
    novo->dado = lista->dado;
    novo->prox = copia_lista(lista->prox);
    return novo;
}

p_no adicionar_elemento(p_no lista, int x){
    p_no novo;
    novo = malloc(sizeof(No));
    novo->dado = x;
    novo->prox = lista;
    return novo;
}

void destruir_lista(p_no lista){       
    if (lista != NULL){
        destruir_lista(lista->prox);
        free(lista);
    }
}

p_no inverter_lista(p_no lista) {
    p_no atual, ant, invertida = NULL;
    atual = lista;
    while(atual != NULL){
        ant = atual;
        atual = ant->prox;
        ant->prox = invertida;
        invertida = ant;
    }
    return invertida;
}

void imprime(p_no lista){
    int ok = 0;
    while(ok == 0){
        // Verificando a ocorrência de zeros.
        // Quando temos 0000, queremos imprimir apenas 0.
        if(lista->dado != 0){
            ok = 1;
        }
        else if(lista->dado == 0 && lista->prox == NULL){
            printf("%d", lista->dado);
            break;
        }
        else if(lista->dado == 0 && lista->prox != NULL){
            lista = lista->prox;
        }
    }
    if(ok == 1){
        while(lista != NULL){
            printf("%d", lista->dado);
            lista = lista->prox;
        }
    }
}

p_no soma(p_no lista1, p_no lista2, p_no lista_res){
    int valor = 0;
    int excede = 0;
    while(lista1 != NULL || lista2 != NULL){
        
        if(lista1 != NULL && lista2 != NULL){
            if(excede == 0){
                valor = lista1->dado + lista2->dado;
                if(valor >= 10 && (lista1->prox != NULL || lista2->prox != NULL)){
                    valor -= 10;
                    excede = 1;
                }
            } else if(excede == 1){
                valor = lista1->dado + lista2->dado + excede;
                excede = 0;
                if(valor >= 10 && (lista1->prox != NULL || lista2->prox != NULL)){
                    valor -= 10;
                    excede = 1;
                }
            }  
        }
        else if(lista1 != NULL && lista2 == NULL){
            if(excede == 0){
                valor = lista1->dado;
                if(valor >= 10 && (lista1->prox != NULL)){
                    valor -= 10;
                    excede = 1;
                }
            } else if(excede == 1){
                valor = lista1->dado + excede;
                excede = 0;
                if(valor >= 10 && (lista1->prox != NULL)){
                    valor -= 10;
                    excede = 1;
                }
            }
        }
        else if(lista1 == NULL && lista2 != NULL){
            if(excede == 0){
                valor = lista2->dado;
                if(valor >= 10 && (lista2->prox != NULL)){
                    valor -= 10;
                    excede = 1;
                }
            } else if(excede == 1){
                valor = lista2->dado + excede;
                excede = 0;
                if(valor >= 10 && (lista2->prox != NULL)){
                    valor -= 10;
                    excede = 1;
                }
            }
        }

        if (valor >= 10){
            excede = valor / 10;
            valor = valor % 10;
            lista_res = adicionar_elemento(lista_res, valor);
            lista_res = adicionar_elemento(lista_res, excede);
        }
        else{
            lista_res = adicionar_elemento(lista_res, valor);   
        }
        
        if(lista1 != NULL){
            lista1 = lista1->prox;
        }
        
        if (lista2 != NULL){
            lista2 = lista2->prox;
        }
    }
    return lista_res;
}

p_no subtracao(p_no lista1, p_no lista2, p_no aux1, p_no aux2, p_no aux11, p_no aux22, p_no lista_res){
    int valor = 0;
    int qtd1 = 0;
    int qtd2 = 0;
    int l2maiorquel1 = 0;

    // Da linha 154 até 187 temos uma verificação de qual
    // dos dois números é o maior.
    
    while((qtd1 == qtd2) && (aux1 != NULL || aux2 != NULL)){
        if (aux1 != NULL){
            qtd1++;
        }
        if (aux2 != NULL){
            qtd2++;
        }
        if (aux1 != NULL){
            aux1 = aux1->prox;
        }
        if (aux2 != NULL){
            aux2 = aux2->prox;
        }
        // Se um número X possui mais digitos que um número Y,
        // então X > Y
    }

    if(qtd2 > qtd1){
        l2maiorquel1 = 1;
    }

    if(qtd2 == qtd1){
        aux22 = inverter_lista(aux22);
        aux11 = inverter_lista(aux11);
        while((aux11 != NULL && aux22 != NULL) && l2maiorquel1 == 0){
            if(aux22->dado > aux11->dado){
                l2maiorquel1 = 1;
            }
            if(aux22->dado < aux11->dado){
                break;
            }
            if(aux22->dado == aux11->dado){
                aux11 = aux11->prox;
                aux22 = aux22->prox;
            } 
        }
    }
    
    if(l2maiorquel1 == 0){
        while(lista1 != NULL || lista2 != NULL){
            if(lista1 != NULL && lista2 != NULL){
                valor = lista1->dado - lista2->dado;
                if(valor < 0 && (lista1->prox != NULL)){
                    valor += 10;
                    lista1->prox->dado -= 1;
                }
            }
            else if(lista1 != NULL && lista2 == NULL){
                valor = lista1->dado;
            }
            lista_res = adicionar_elemento(lista_res, valor);
        
            if(lista1 != NULL){
            lista1 = lista1->prox;
            }

            if(lista2 != NULL){
            lista2 = lista2->prox;
            }
    }
    return lista_res;
    }
    else{
        while(lista1 != NULL || lista2 != NULL){
            if(lista1 != NULL && lista2 != NULL){
                valor = lista2->dado - lista1->dado;
                if(valor < 0 && (lista2->prox != NULL)){
                    valor += 10;
                    lista2->prox->dado -= 1;
                }
            }
            else if(lista2 != NULL && lista1 == NULL){
                valor = lista2->dado;
            }
            lista_res = adicionar_elemento(lista_res, valor);
        
            if(lista1 != NULL){
                lista1 = lista1->prox;
            }

            if(lista2 != NULL){
                lista2 = lista2->prox;
            }
        }
    return lista_res;
    }
}

p_no mult(p_no aux1, p_no aux2, p_no lista_res, int i, int j){
    int valor = 0;
    int excede = 0;
    while(aux1 != NULL){
        
        // Adicionando zeros no número apenas se estamos na segunda mult ou adiante.
        if(i > 0){
            if(j == 0){
                j = 1;
                for(int n = 0; n < i; n++){
                    lista_res = adicionar_elemento(lista_res, 0);
                }   
            }
        }

        // Se a multiplicação anterior é < 10
        if(excede == 0){
            valor = aux2->dado * aux1->dado;
            if(valor >= 10 && aux1->prox != NULL){
                excede = valor / 10;
                valor = valor % 10;
                lista_res = adicionar_elemento(lista_res, valor);   
            }
            else if(valor >= 10 && aux1->prox == NULL){
                excede = valor / 10;
                valor = valor % 10;
                lista_res = adicionar_elemento(lista_res, valor);
                lista_res = adicionar_elemento(lista_res, excede);
            }
            else{
                lista_res = adicionar_elemento(lista_res, valor); 
            }
    
        }
        // Se a multiplicação anterior >= 10
        else if(excede != 0){
            valor = aux2->dado * aux1->dado + excede;
            excede = 0;
            if(valor >= 10 && aux1->prox != NULL){
                excede = valor / 10;
                valor = valor % 10;
                lista_res = adicionar_elemento(lista_res, valor);
               
            }
            else if(valor >= 10 && aux1->prox == NULL){
                excede = valor / 10;
                valor = valor % 10;
                lista_res = adicionar_elemento(lista_res, valor);
                lista_res = adicionar_elemento(lista_res, excede);
                
            }
            else{
                lista_res = adicionar_elemento(lista_res, valor);
            }
        }
        aux1 = aux1->prox;
    }
    return lista_res;
}

int main() {
    int n;
    char op, num;
    p_no lista1, lista2, lista_resultado;
    scanf("%d\n", &n);
    
    for(int i = 0; i < n; i++){
        lista1 = criar_lista();
        lista2 = criar_lista();
        lista_resultado = criar_lista();
        scanf("%c\n", &op);

        // Leitura num1
        do {
            scanf("%c", &num);
            if(num != ' '){
                num -= '0';
                lista1 = adicionar_elemento(lista1, num);
            }
        } while (num != ' ');

        // Leitura num2
        do {
            scanf("%c", &num);
            if (num != '\n'){
                num -= '0';
                lista2 = adicionar_elemento(lista2, num);
            } 
        } while(num != '\n');
        
        // Soma
        if(op == '+'){ 
            lista_resultado = soma(lista1, lista2, lista_resultado);
            imprime(lista_resultado);
            printf("\n");
            destruir_lista(lista_resultado);
            destruir_lista(lista1);
            destruir_lista(lista2);
        }

        //Subtração
        if(op == '-'){
            // os auxiliares servem para verificar qual dos dois números é maior.
            p_no aux1 = criar_lista();
            p_no aux2 = criar_lista();
            p_no aux22 = criar_lista();
            p_no aux11 = criar_lista();
            aux1 = copia_lista(lista1);
            aux2 = copia_lista(lista2);
            aux22 = copia_lista(lista2);
            aux11 = copia_lista(lista1);
            lista_resultado = subtracao(lista1, lista2, aux1, aux2, aux11, aux22, lista_resultado);
            imprime(lista_resultado);
            printf("\n");
            destruir_lista(aux1);
            destruir_lista(aux11);
            destruir_lista(aux2);
            destruir_lista(aux22);
            destruir_lista(lista_resultado);
            destruir_lista(lista1);
            destruir_lista(lista2);
        }

        // Multiplicação
        else if(op == '*'){
            int i;
            p_no aux1;
            p_no aux2 = lista2;
            p_no lista_res2 = criar_lista();    // lista na qual adicionaremos da segunda mult adiante
            p_no lista_resF = criar_lista();    // lista na qual adicionaremos a soma de duas multiplicações 
            for(i = 0; aux2 != NULL; i++){
                int j = 0;
                aux1 = lista1;
                if(i == 0){
                    lista_resultado = mult(aux1, aux2, lista_resultado, i, j);
                }
                else{
                    lista_res2 = mult(aux1, aux2, lista_res2, i, j);
                }
                if(i >= 1){ 
                    lista_resultado = inverter_lista(lista_resultado);
                    lista_res2 = inverter_lista(lista_res2);
                    lista_resF = soma(lista_resultado, lista_res2, lista_resF);
                    destruir_lista(lista_resultado);
                    destruir_lista(lista_res2);
                    lista_res2 = criar_lista();
                    lista_resultado = copia_lista(lista_resF);
                    destruir_lista(lista_resF);
                    lista_resF = criar_lista();
                }
                aux2 = aux2->prox;
            }
            imprime(lista_resultado);
            printf("\n");
            destruir_lista(lista_resultado);
            destruir_lista(lista1);
            destruir_lista(lista2);
        } 
    }
}