#include <stdio.h>
#include "professor_carlos.h"

int main(){
    int n;
    int k;
    int m;
    Aluno add;
    int operacao;
    int sala = 0;
    char substr[15];
    
    scanf("%d %d", &n, &k);
    Turma t[max_turmas];

    for (int i = 0; i < n; i ++){
        scanf("%d", &m);
        t[i].qtd = m;
        
        for (int j = 0; j < m; j++){
            scanf("%s %s %d %d %d", t[i].alunos[j].nome, t[i].alunos[j].sobrenome,
            &t[i].alunos[j].nascimento.dia, &t[i].alunos[j].nascimento.mes, 
            &t[i].alunos[j].nascimento.ano);
        }
            
    }
    for (int i = 0; i < k; i++){
        scanf("%d ", &operacao);
        if (operacao == 1 || operacao == 2){
            scanf("%d", &sala);
        }
        if (operacao == 1){
            printf("%s\n",procura_novo_na_turma(t, t[sala].qtd, sala).nome);
        }
        else if (operacao == 2){
            printf("%s\n", procura_velho_na_turma(t, t[sala].qtd, sala).sobrenome);
        }
        else if (operacao == 3){
            printf("%s\n", procura_velho_todas_turmas(t, n).nome);
        }
        else if (operacao == 4){
            printf("%s\n", procura_novo_todas_turmas(t ,n).sobrenome);
        }
        if (operacao == 5){
            scanf("%s", substr);
            printf("%d\n", conta_substrings(t, n, substr));
        }
        if (operacao == 6){
            scanf("%d %s %s %d %d %d", &sala, add.nome, add.sobrenome, &add.nascimento.dia,
            &add.nascimento.mes, &add.nascimento.ano);
            printf("%d\n",add_aluno(t, add, sala));
        }
        if (operacao == 7){
            scanf("%d", &sala);
            printf("%d\n", remove_aluno(t, sala));
        }
        
    }
    return 0;
}