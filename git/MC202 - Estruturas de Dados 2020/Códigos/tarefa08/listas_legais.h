enum Cor {RED, BLACK};

typedef struct No{
    unsigned long long int dado;
    int ocorrencias;
    enum Cor cor;
    struct No *esq, *dir;
} No;

typedef No * p_no;

//cria uma árvore
p_no criar_arvore(unsigned long long int dado, p_no esq, p_no dir);

//verifica se um número x está na árvore
int esta_na_arvore(p_no raiz, unsigned long long int dado, int count);

//incrementa a ocorrencia de um elemento que já está na árvore
void incrementar_ocorrencia(p_no raiz, unsigned long long int dado);

//imprime o número de ocorrencias de um número x
void num_ocorrencias(p_no raiz, unsigned long long int dado);

int percorre(p_no raiz);

//destroi a árvore
void destroi(p_no raiz);

int eh_vermelho(p_no x);

int eh_preto(p_no x);

p_no rotaciona_esq(p_no raiz);

p_no rotaciona_dir(p_no raiz);

void sobe_vermelho(p_no raiz);

p_no inserir_rec(p_no raiz, unsigned long long int dado);

p_no inserir_casca(p_no raiz, unsigned long long int dado);




