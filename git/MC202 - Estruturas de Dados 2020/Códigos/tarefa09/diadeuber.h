
typedef struct{
    char nome[50];
    double avaliacao;
    double local_x, local_y;
    double destino_x, destino_y;
} Cliente;

typedef struct{
    Cliente *v;
    int n, tamanho;
} FP;

typedef FP * p_fp;

//cria uma fila de prioridade
p_fp criar_filaprio(int tam);

void troca(Cliente *a, Cliente *b);

void sobe_no_heap(p_fp fprio, int k);

void desce_no_heap(p_fp fprio, int k);

void insere(p_fp fprio, Cliente pessoa);

Cliente extrai_maximo(p_fp fprio);

//ajusta a fila de prioridade depois que um cliente cancela uma corrida
void cancelamento(p_fp fprio, char nome[50]);

