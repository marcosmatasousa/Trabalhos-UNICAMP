#include <stdio.h>
#include "professor_carlos.h"

int compara_lex(char text1[], char text2[]) {
    int i;
    for (i = 0; text1[i] != '\0'; i++){
        
        if (text2[i] == '\0'){
            return 1;
        }
        if (text1[i] > text2[i]){
            return 1;
        }
        if (text1[i] < text2[i]){
            return -1;
        }
    }
    if (text2[i] != '\0')
        return -1;
    return 0; 
}

Aluno procura_novo_na_turma(Turma t[], int qtd_turmas, int j){
   Aluno mais_novo = t[j].alunos[0];
    for (int i = 1; i < qtd_turmas; i++){
        
        if (t[j].alunos[i].nascimento.ano > mais_novo.nascimento.ano){
            mais_novo = t[j].alunos[i];
        }
        else if(t[j].alunos[i].nascimento.ano == mais_novo.nascimento.ano){
            if (t[j].alunos[i].nascimento.mes > mais_novo.nascimento.mes){
                mais_novo = t[j].alunos[i];
            }
            else if(t[j].alunos[i].nascimento.mes == mais_novo.nascimento.mes){
                if (t[j].alunos[i].nascimento.dia > mais_novo.nascimento.dia){
                    mais_novo = t[j].alunos[i];
                }
                else if(t[j].alunos[i].nascimento.dia == mais_novo.nascimento.dia){
                    if (compara_lex(t[j].alunos[i].nome, mais_novo.nome) == -1){
                        mais_novo = t[j].alunos[i];
                    }
                    else if(compara_lex(t[j].alunos[i].nome, mais_novo.nome) == 0){
                        if(compara_lex(t[j].alunos[i].sobrenome, mais_novo.sobrenome) == -1){
                            mais_novo = t[j].alunos[i];
                        }
                    }
                }
            }
        }
    }
    return mais_novo;
}

Aluno procura_velho_na_turma(Turma t[], int qtd_turmas, int j){
    Aluno mais_velho = t[j].alunos[0];
    for (int i = 1; i < qtd_turmas; i++){
        
        if (t[j].alunos[i].nascimento.ano < mais_velho.nascimento.ano){
            mais_velho = t[j].alunos[i];
        }
        else if(t[j].alunos[i].nascimento.ano == mais_velho.nascimento.ano){
            if (t[j].alunos[i].nascimento.mes < mais_velho.nascimento.mes){
                mais_velho = t[j].alunos[i];
            }
            else if(t[j].alunos[i].nascimento.mes == mais_velho.nascimento.mes){
                if (t[j].alunos[i].nascimento.dia < mais_velho.nascimento.dia){
                    mais_velho = t[j].alunos[i];
                }
                else if(t[j].alunos[i].nascimento.dia == mais_velho.nascimento.dia){
                    if (compara_lex(t[j].alunos[i].nome, mais_velho.nome) == -1){
                        mais_velho = t[j].alunos[i];
                    }
                    else if(compara_lex(t[j].alunos[i].nome, mais_velho.nome) == 0){
                        if(compara_lex(t[j].alunos[i].sobrenome, mais_velho.sobrenome) == -1){
                            mais_velho = t[j].alunos[i];
                        }
                    }
                }
            }
        }
    }
    return mais_velho;
}

Aluno procura_velho_todas_turmas(Turma t[], int qtd_turmas) {
    Aluno velho_todos;
    for (int i = 0; i < qtd_turmas; i++){
        for (int k = 0; k < t[i].qtd; k++){

       if ((i == 0) && (k == 0)){
                velho_todos = t[i].alunos[k];
            }
            else if(t[i].alunos[k].nascimento.ano < velho_todos.nascimento.ano){
                velho_todos = t[i].alunos[k];
            }
            else if(t[i].alunos[k].nascimento.ano == velho_todos.nascimento.ano){
                if(t[i].alunos[k].nascimento.mes < velho_todos.nascimento.mes){
                    velho_todos = t[i].alunos[k];
                }
                else if(t[i].alunos[k].nascimento.mes == velho_todos.nascimento.mes){
                    if(t[i].alunos[k].nascimento.dia < velho_todos.nascimento.dia){
                        velho_todos = t[i].alunos[k];
                    }
                    else if(t[i].alunos[k].nascimento.dia == velho_todos.nascimento.dia){
                        if (compara_lex(t[i].alunos[k].nome, velho_todos.nome) == -1){
                            velho_todos = t[i].alunos[k];
                        }
                        else if(compara_lex(t[i].alunos[k].nome, velho_todos.nome) == 0){
                            if (compara_lex(t[i].alunos[k].sobrenome, velho_todos.sobrenome) == -1){
                                velho_todos = t[i].alunos[k];
                            }
                        }
                    }
                }
            }
        }
    }
    return velho_todos;
}

Aluno procura_novo_todas_turmas(Turma t[], int qtd_turmas){
    Aluno novo_todos;
    for (int i = 0; i < qtd_turmas; i++){
        for (int k = 0; k < t[i].qtd; k++){

            if ((i == 0) && (k == 0)){
                novo_todos = t[i].alunos[k];
            }
            else if(t[i].alunos[k].nascimento.ano > novo_todos.nascimento.ano){
                novo_todos = t[i].alunos[k];
            }
            else if(t[i].alunos[k].nascimento.ano == novo_todos.nascimento.ano){
                if(t[i].alunos[k].nascimento.mes > novo_todos.nascimento.mes){
                    novo_todos = t[i].alunos[k];
                }
                else if(t[i].alunos[k].nascimento.mes == novo_todos.nascimento.mes){
                    if(t[i].alunos[k].nascimento.dia > novo_todos.nascimento.dia){
                        novo_todos = t[i].alunos[k];
                    }
                    else if(t[i].alunos[k].nascimento.dia == novo_todos.nascimento.dia){
                        if (compara_lex(t[i].alunos[k].nome, novo_todos.nome) == -1){
                            novo_todos = t[i].alunos[k];
                        }
                        else if(compara_lex(t[i].alunos[k].nome, novo_todos.nome) == 0){
                            if (compara_lex(t[i].alunos[k].sobrenome, novo_todos.sobrenome) == -1){
                                novo_todos = t[i].alunos[k];
                            }
                        }
                    }
                }
            }
        }
    }
    return novo_todos;
}

int substring(char name[max_str], char s[max_str]){
    int len = 0;
    int contagem = 0;

    for (int i = 0; s[i] != '\0'; i++){
        len++;
    }
    for (int i = 0; name[i] != '\0'; i++){
        for (int j = 0; s[j] != '\0'; j++){
            if (name[i + j] == '\0'){
                contagem = 0;
                break;
            }
            if (name[i + j] == s[j]){
                contagem++;
            }
            else {
                contagem = 0;
                break;
            }
            if (contagem == len) {
                return 1;
            }
        } 
        if (contagem == len){
            return 1;
        }
    }
        return 0;
}


int conta_substrings (Turma t[], int qnt_turmas, char str[]){
    int contagem_alunos = 0;
    for (int i = 0; i < qnt_turmas; i++){
        for (int j = 0; j < t[i].qtd; j++){
            if (substring(t[i].alunos[j].nome, str) == 1){
                contagem_alunos++;
            }
        }
    } return contagem_alunos;
}

int add_aluno(Turma t[], Aluno A, int j){
    t[j].alunos[t[j].qtd] = A;
    t[j].qtd ++;
    return t[j].qtd;
}

int remove_aluno(Turma t[], int j){
    t[j].qtd -= 1;
    return t[j].qtd;
}