#ifndef PROFESSOR_CARLOS_H
#define PROFESSOR_CARLOS_H
#define max_alunos 40
#define max_turmas 50
#define max_operacoes 50
#define max_str 15

typedef struct data {
    int dia;
    int mes;
    int ano;
} Data;

typedef struct aluno {
    Data nascimento;
    char nome[15];
    char sobrenome[15];
} Aluno;

typedef struct turma {
    Aluno alunos[50];
    int qtd;
} Turma;

// A funcao recebe dois textos e compara lexigraficamente,
// devolve 0 se o primeiro for menor, 1 se o primeiro for maior,
// e -1 se o primeiro for menor.
int compara_lex(char text1[], char text2[]);

// A funcao recebe um texto s e verifica se o mesmo é substring
// do nome.
int substring(char name[max_str], char s[max_str]);

// A funcao recebe todas as turma e a turma escolhida,
// retornando o aluno mais novo da turma escolhida.
Aluno procura_novo_na_turma(Turma t[], int qtd_turmas, int j);

// A funcao recebe todas as turmas e retorna o aluno mais novo dentre todas as turmas.
Aluno procura_novo_todas_turmas(Turma t[], int qtd_turmas);

// A funcao recebe todas as turma e o indice da turma escolhida,
// retornando o aluno mais velho da turma escolhida.
Aluno procura_velho_na_turma(Turma t[], int qtd_turmas, int j);

Aluno procura_velho_todas_turmas(Turma t[], int qtd_turmas);
// A funcao recebe todas as turmas e retorna o aluno mais velho dentre todas as turmas.

// A funcao recebe todoas as turmas e uma string,
// retornando a quantidade de alunos que a string aparece em seu nome.
int conta_substrings(Turma t[], int qtd_turmas, char str[]);

// Adiciona o aluno A na turma j, retornando a quantidade de alunos da turma j.
int add_aluno(Turma t[], Aluno A, int j);

// Remove o ultimo aluno adicionado na turma j,
// retornando a quantidade de alunos restante na turma j.
int remove_aluno(Turma t[], int j);

#endif
