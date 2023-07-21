#define MAX 200

typedef struct No {
    char palavra[50];
   struct No * prox;
} No;

typedef No * p_no;

typedef struct{
    p_no vetor[MAX];
} Hash;

typedef Hash * p_hash;

//cria lista ligada
p_no criar_lista();

//insere elemento na lista ligada
p_no inserir_lista(p_no lista, char *palavra);

//destroi lista ligada
void destruir_lista(p_no lista);

p_hash criar_hash();

void destruir_hash(p_hash t);

int hash(char *palavra);

//insere na tabela hash
void inserir(p_hash t, char *palavra);

//busca a palavra no dicionário/tabela hash
int busca_dicionario(p_hash t, char *palavra);

//casos de palavras escritas com uma letra a menos
void letra_menos(p_hash t, char *palavra);

//casos de palavras escritas com uma letra a mais
void letra_mais(p_hash t, char *palavra);

//casos de palavras escritas com uma letra trocada
void letra_trocada(p_hash t, char *palavra);

