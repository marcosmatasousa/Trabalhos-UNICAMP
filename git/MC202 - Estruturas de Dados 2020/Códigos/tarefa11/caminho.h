typedef struct No{
    int visitado;
    double coord_x, coord_y;
    struct No * prox;
} No;

typedef No * p_no;

typedef struct{
    p_no pokestops, lugias;
} Grafo;

typedef Grafo * p_grafo;


//cria uma lista ligada
p_no criar_lista();

//destroi uma lista ligada
void destruir_lista(p_no lista);

//adiciona uma pokestop ou um lugia
p_no adicionar_ponto(p_no lista, double coord_x, double coord_y);

//cria o grafo
p_grafo criar_grafo();

//destroi o grafo
void destruir_grafo(p_grafo g);

//reseta o status de visitado dos pontos
void desvisitar(p_no pokestops);

//calcula a distancia entre dois pontos
double distancia(double origem_x, double origem_y, double destino_x, double destino_y);

//verifica se há um possível caminho dada uma distancia X
int caminhos(double atual_x, double atual_y, p_no pokestops, p_no poke_aux, p_no lugias, p_no lugias_aux, int teto);



