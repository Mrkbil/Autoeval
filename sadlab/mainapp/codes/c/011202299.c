#include <stdio.h>

int main() {
    double num1, num2, num3;
    scanf("%lf", &num1);
    scanf("%lf", &num2);
    scanf("%lf", &num3);
    double sum = num1 + num2 + num3;
    printf("%.2f\n",sum);
    return 0;
}