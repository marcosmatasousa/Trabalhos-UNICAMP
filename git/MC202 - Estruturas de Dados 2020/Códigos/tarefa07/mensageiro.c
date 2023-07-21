#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define MAX 1000

typedef struct No{
    int dado;
    char texto[MAX];
    struct No *esq, *dir;
} No;

typedef No *p_no;

void destruir_arvore(p_no raiz){
    if (raiz != NULL){
        destruir_arvore(raiz->esq);
        destruir_arvore(raiz->dir);
        free(raiz);
    }
}

p_no inserir(p_no raiz, int dado, char texto[]){
    if (raiz == NULL){
        p_no novo = malloc(sizeof(No));
        novo->esq = novo->dir = NULL;
        novo->dado = dado;
        strcpy(novo->texto, texto);
        return novo;
    }
    if (dado < raiz->dado){
        raiz->esq = inserir(raiz->esq, dado, texto);
    }
    if (dado > raiz->dado){
        raiz->dir = inserir(raiz->dir, dado, texto);
    }
    return raiz;
}

void remover_sucessor(p_no raiz){
    p_no min = raiz->dir;
    p_no pai = raiz;
    while(min->esq != NULL){
        pai = min;
        min = min->esq;
    }
    if(pai->esq == min){
        pai->esq = min->dir;
    }
    else{
        pai->dir = min->dir;
    }
    raiz->dado = min->dado;
    strcpy(raiz->texto, min->texto);
    free(min);
}

p_no remover(p_no raiz, int dado){
    if(raiz == NULL){
        return NULL;
    }
    if(dado < raiz->dado){
        raiz->esq = remover(raiz->esq, dado);
    }
    else if(dado > raiz->dado){
        raiz->dir = remover(raiz->dir, dado);
    }
    else if(raiz->esq == NULL){
        p_no aux = raiz->dir;
        free(raiz);
        return aux;
    }
    else if(raiz->dir == NULL){
        p_no aux = raiz->esq;
        free(raiz);
        return aux;
    }
    else{
        remover_sucessor(raiz);
    }
    return raiz;
}

// imprime o conteúdo da árvore in-ordem
void print_arvore(p_no raiz){
    if (raiz != NULL){
        print_arvore(raiz->esq);
        printf("%s", raiz->texto);
        print_arvore(raiz->dir);
    }
}

// dado um número x, busca o nó cujo número é x
p_no busca(p_no raiz, int x){
    if (raiz == NULL || raiz->dado == x){
        return raiz;
    }
    if(x < raiz->dado){
        return busca(raiz->esq, x);
    }
    return busca(raiz->dir, x);
}

p_no busca_segundo_no(p_no raiz, p_no no_atual, int primeiro_fix, int guardiao);

// fixa o primeiro nó
p_no busca_primeiro_no(p_no raiz, p_no no_atual, int guardiao){
    if(no_atual == NULL){
        return NULL;
    }
    p_no aux;
    if((aux = busca_primeiro_no(raiz, no_atual->esq, guardiao)) != NULL){
        return aux;
    }
    if((aux = busca_segundo_no(raiz, raiz, no_atual->dado, guardiao)) != NULL){
        return aux;
    }
    if((aux = busca_primeiro_no(raiz, no_atual->dir, guardiao)) != NULL){
        return aux;
    }
    return NULL;
}

// fixa o segundo nó
p_no busca_segundo_no(p_no raiz, p_no no_atual, int primeiro_fix, int guardiao){
    if(no_atual == NULL ){
        return NULL;
    }
    p_no aux;
    if((aux = busca_segundo_no(raiz, no_atual->esq, primeiro_fix, guardiao)) != NULL){
        return aux;
    }
    // busca o restante para o complemento da soma do guardião
    if(no_atual->dado != primeiro_fix && guardiao - (primeiro_fix + no_atual->dado) > 0){
        p_no terceiro_no = busca(raiz, guardiao - (primeiro_fix + no_atual->dado));
        if(terceiro_no != NULL){
            char token_texto[MAX];
            p_no primeiro_no = busca(raiz, primeiro_fix);
            strcpy(token_texto, primeiro_no->texto);
            strcat(token_texto, no_atual->texto);
            strcat(token_texto, terceiro_no->texto);
            int remover1 = no_atual->dado;
            int remover2 = terceiro_no->dado;
            raiz = remover(raiz, primeiro_fix);
            raiz = remover(raiz, remover1);
            raiz = remover(raiz, remover2);
            raiz = inserir(raiz, guardiao, token_texto);
            return raiz;
        } 
    }
    if((aux = busca_segundo_no(raiz, no_atual->dir, primeiro_fix, guardiao)) != NULL){
        return aux;
    }
    return NULL;
}

int main(){
    int num_cartoes, num_autoridades, num_token, guardiao;
    char texto[MAX];
    p_no arvore_cartoes;

    while (scanf("%d %d", &num_cartoes, &num_autoridades) == 2){
        arvore_cartoes = NULL;
        for (int i = 0; i < num_cartoes; i++){
            scanf("%d ", &num_token);
            scanf("\"%[^\"]\"", texto);
            arvore_cartoes = inserir(arvore_cartoes, num_token, texto);
        }

        for (int j = 0; j < num_autoridades; j++){
            scanf("%d", &guardiao);
            arvore_cartoes = busca_primeiro_no(arvore_cartoes, arvore_cartoes, guardiao); 
        }
        print_arvore(arvore_cartoes);
        printf("\n");
        destruir_arvore(arvore_cartoes);
    }
    return 0;
}