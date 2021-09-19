#include<stdio.h>

int main(){
    int k;
    int Year [8] = { 2002, 2012, 2040, 2031, 1936, 1971, 1996, 1981};
    int sum[8] = {};
    int l = 0;
    for(int i = 0;i < 8;i++){
        k = Year[i];
        if (k %4 == 0 && k %100 != 0 || (k%400)){
            sum[l] = k;
            l ++;
        }
    
    }
}