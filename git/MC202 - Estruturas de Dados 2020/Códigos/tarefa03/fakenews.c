#include <stdio.h>
#include <stdlib.h>
#include <math.h>

double calcula_media(double *nums, int m){
    double media = 0;
    for (int i = 0; i < m; i++){
        media += nums[i];
    }
    return media/m;    
}

double maximo(double *nums, int m){
    double max = nums[0];
    for (int i = 1; i < m; i++){
        if (nums[i] > max){
            max = nums[i];
        }
    }
    return max;
}

double minimo(double *nums, int m){
    double min = nums[0];
    for (int i = 1; i < m; i++){
        if (nums[i] < min){
            min = nums[i];
        }
    }
    return min;
}

double calcula_desv (double *nums, int m, double media){
    double dp = 0;
    for (int i = 0; i < m; i++){
        dp += pow(media - nums[i], 2);
    }
    dp = sqrt(dp/m);
    return dp;
}

typedef struct termo{
    char name[25];
    double max;
    double min;
    double media;
    double desvio;
} Termo;

void imprime_results(Termo *vetor, int tamanho){
    if (tamanho == 0){
        printf("\n");
    } else{
        for (int i = 0; i < tamanho; i++){
            if (i < tamanho - 1){
                printf("%s ", vetor[i].name);
            } else{
                printf("%s\n", vetor[i].name);
            }
        }
    }
}

int main() {
    int n, m;
    int bot = 0;  
    int surp = 0;
    int normal = 0;
    int local = 0;
    int irrelv = 0;
    

    scanf("%d %d", &n, &m);
    Termo *v, *lista_bot, *lista_surp, *lista_normal, *lista_local, *lista_irrelv;
    double *nums;

    v = malloc(n * sizeof(Termo));
    nums = malloc(m * sizeof(double));

    for (int i = 0; i < n; i++) {
        scanf("%s", v[i].name);

        for (int j = 0; j < m; j++){
            scanf("%lf", &nums[j]);
        }
        v[i].max = maximo(nums, m);
        v[i].min = minimo(nums, m);
        v[i].media = calcula_media(nums, m);
        v[i].desvio = calcula_desv(nums, m, v[i].media);

        if (v[i].media >= 60 && v[i].desvio > 15){
            bot++;
        }
        if (v[i].media >= 60 && v[i].desvio <= 15){
            surp++;
        }
        if (v[i].media < 60 && v[i].max >= 80 && v[i].min > 20){
            normal++;
        }
        if (v[i].media < 60 && v[i].max >= 80 && v[i].min <= 20){
            local++;
        }
        if (v[i].media < 60 && v[i].max < 80){
            irrelv++;
        }
    }
    free(nums);

    for (int i = 0; i < n; i++){
        printf("%s %.2lf %.2lf %.2lf %.2lf\n", v[i].name, v[i].max, 
        v[i].min, v[i].media, v[i].desvio);
    }

    lista_bot = (malloc(bot * sizeof(Termo)));
    lista_surp = (malloc(surp * sizeof(Termo)));
    lista_normal = (malloc(normal * sizeof(Termo)));
    lista_local = (malloc(local * sizeof(Termo)));
    lista_irrelv = (malloc(irrelv * sizeof(Termo)));

    bot = surp = normal = local = irrelv = 0;

    for (int i = 0; i < n; i++){
        if (v[i].media >= 60 && v[i].desvio > 15){
            lista_bot[bot] = v[i];
            bot++;
        }
        if (v[i].media >= 60 && v[i].desvio <= 15){
            lista_surp[surp] = v[i];
            surp++;
        }
        if (v[i].media < 60 && v[i].max >= 80 && v[i].min > 20){
            lista_normal[normal] = v[i];
            normal++;
        }
        if (v[i].media < 60 && v[i].max >= 80 && v[i].min <= 20){
            lista_local[local] = v[i];
            local++;
        }
        if (v[i].media < 60 && v[i].max < 80){
            lista_irrelv[irrelv] = v[i];
            irrelv++;
        }

    }
    free(v);

    printf("RESULTADO:\n");
    
    printf("Bot (%d): ", bot);
    imprime_results(lista_bot, bot);
    
    printf("Surpreendente (%d): ", surp);
    imprime_results(lista_surp, surp);

    printf("Normal (%d): ", normal);
    imprime_results(lista_normal, normal);

    printf("Local (%d): ", local);
    imprime_results(lista_local, local);

    printf("Irrelevante (%d): ", irrelv);
    imprime_results(lista_irrelv, irrelv);

    free(lista_bot);
    free(lista_surp);
    free(lista_normal);
    free(lista_local);
    free(lista_irrelv);
    
    return 0;
}